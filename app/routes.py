from calendar import month_name
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for,
)
from sqlalchemy import func

from .extensions import db
from .models import Expense, Income          # ← import Income


main = Blueprint("main", __name__)


EXPENSE_CATEGORIES = [
    "Food", "Transportation", "Housing", "Utilities", "Healthcare",
    "Entertainment", "Shopping", "Travel", "Education", "Other",
]

INCOME_SOURCES = [                            # ← NEW
    "Salary", "Freelance", "Bonus", "Investment", "Gift", "Other",
]


def parse_amount(value):
    try:
        amount = Decimal(value)
        if amount <= 0:
            raise InvalidOperation
        return amount
    except (InvalidOperation, TypeError, ValueError):
        return None


def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


# ============================================================
# DASHBOARD — now includes income & balance
# ============================================================
@main.route("/")
def dashboard():
    current_date = date.today()

    selected_month = request.args.get(
        "month", default=current_date.strftime("%Y-%m")
    )

    try:
        selected_year, selected_month_number = map(int, selected_month.split("-"))
        if not 1 <= selected_month_number <= 12:
            raise ValueError
    except ValueError:
        selected_year = current_date.year
        selected_month_number = current_date.month
        selected_month = current_date.strftime("%Y-%m")

    # --- Expenses (same as before) ---
    expenses = (
        Expense.query
        .filter(func.strftime("%Y-%m", Expense.expense_date) == selected_month)
        .order_by(Expense.expense_date.desc(), Expense.id.desc())
        .all()
    )

    monthly_expenses = sum(
        (e.amount_decimal for e in expenses), Decimal("0")
    )

    category_totals = (
        db.session.query(Expense.category, func.sum(Expense.amount))
        .filter(func.strftime("%Y-%m", Expense.expense_date) == selected_month)
        .group_by(Expense.category)
        .order_by(func.sum(Expense.amount).desc())
        .all()
    )

    # --- Incomes (NEW) ---
    incomes = (
        Income.query
        .filter(func.strftime("%Y-%m", Income.income_date) == selected_month)
        .order_by(Income.income_date.desc(), Income.id.desc())
        .all()
    )

    monthly_income = sum(
        (i.amount_decimal for i in incomes), Decimal("0")
    )

    # --- Balance (NEW) ---
    balance = monthly_income - monthly_expenses

    # --- All-time totals (NEW) ---
    all_time_expenses = db.session.query(
        func.coalesce(func.sum(Expense.amount), 0)
    ).scalar() or Decimal("0")

    all_time_income = db.session.query(
        func.coalesce(func.sum(Income.amount), 0)
    ).scalar() or Decimal("0")

    all_time_balance = Decimal(all_time_income) - Decimal(all_time_expenses)

    return render_template(
        "dashboard.html",
        expenses=expenses,
        incomes=incomes,                              # ← new
        monthly_expenses=monthly_expenses,            # ← renamed
        monthly_income=monthly_income,                # ← new
        balance=balance,                              # ← new
        all_time_expenses=Decimal(all_time_expenses), # ← renamed
        all_time_income=Decimal(all_time_income),     # ← new
        all_time_balance=all_time_balance,            # ← new
        category_totals=category_totals,
        selected_month=selected_month,
        selected_month_label=f"{month_name[selected_month_number]} {selected_year}",
    )


# ============================================================
# EXPENSE ROUTES (unchanged, just CATEGORIES → EXPENSE_CATEGORIES)
# ============================================================
@main.route("/expenses/new", methods=["GET", "POST"])
def create_expense():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount = parse_amount(request.form.get("amount"))
        category = request.form.get("category", "").strip()
        expense_date = parse_date(request.form.get("expense_date"))
        notes = request.form.get("notes", "").strip()

        errors = []
        if not title:                            errors.append("Title is required.")
        if amount is None:                       errors.append("Amount must be greater than zero.")
        if category not in EXPENSE_CATEGORIES:   errors.append("Please select a valid category.")
        if expense_date is None:                 errors.append("Please provide a valid date.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "expense_form.html", expense=None,
                categories=EXPENSE_CATEGORIES, form=request.form,
            )

        expense = Expense(
            title=title, amount=amount, category=category,
            expense_date=expense_date, notes=notes or None,
        )
        db.session.add(expense)
        db.session.commit()
        flash("Expense added successfully.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template(
        "expense_form.html", expense=None,
        categories=EXPENSE_CATEGORIES,
        form={"expense_date": date.today().isoformat()},
    )


@main.route("/expenses/<int:expense_id>/edit", methods=["GET", "POST"])
def edit_expense(expense_id):
    expense = db.get_or_404(Expense, expense_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount = parse_amount(request.form.get("amount"))
        category = request.form.get("category", "").strip()
        expense_date = parse_date(request.form.get("expense_date"))
        notes = request.form.get("notes", "").strip()

        errors = []
        if not title:                            errors.append("Title is required.")
        if amount is None:                       errors.append("Amount must be greater than zero.")
        if category not in EXPENSE_CATEGORIES:   errors.append("Please select a valid category.")
        if expense_date is None:                 errors.append("Please provide a valid date.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "expense_form.html", expense=expense,
                categories=EXPENSE_CATEGORIES, form=request.form,
            )

        expense.title = title
        expense.amount = amount
        expense.category = category
        expense.expense_date = expense_date
        expense.notes = notes or None
        db.session.commit()

        flash("Expense updated successfully.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template(
        "expense_form.html", expense=expense,
        categories=EXPENSE_CATEGORIES, form=None,
    )


@main.post("/expenses/<int:expense_id>/delete")
def delete_expense(expense_id):
    expense = db.get_or_404(Expense, expense_id)
    db.session.delete(expense)
    db.session.commit()
    flash("Expense deleted successfully.", "success")
    return redirect(url_for("main.dashboard"))


# ============================================================
# INCOME ROUTES (NEW)
# ============================================================
@main.route("/incomes/new", methods=["GET", "POST"])
def create_income():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount = parse_amount(request.form.get("amount"))
        source = request.form.get("source", "").strip()
        income_date = parse_date(request.form.get("income_date"))
        notes = request.form.get("notes", "").strip()

        errors = []
        if not title:                          errors.append("Title is required.")
        if amount is None:                     errors.append("Amount must be greater than zero.")
        if source not in INCOME_SOURCES:       errors.append("Please select a valid source.")
        if income_date is None:                errors.append("Please provide a valid date.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "income_form.html", income=None,
                sources=INCOME_SOURCES, form=request.form,
            )

        income = Income(
            title=title, amount=amount, source=source,
            income_date=income_date, notes=notes or None,
        )
        db.session.add(income)
        db.session.commit()
        flash("Income added successfully.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template(
        "income_form.html", income=None, sources=INCOME_SOURCES,
        form={"income_date": date.today().isoformat()},
    )


@main.route("/incomes/<int:income_id>/edit", methods=["GET", "POST"])
def edit_income(income_id):
    income = db.get_or_404(Income, income_id)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        amount = parse_amount(request.form.get("amount"))
        source = request.form.get("source", "").strip()
        income_date = parse_date(request.form.get("income_date"))
        notes = request.form.get("notes", "").strip()

        errors = []
        if not title:                          errors.append("Title is required.")
        if amount is None:                     errors.append("Amount must be greater than zero.")
        if source not in INCOME_SOURCES:       errors.append("Please select a valid source.")
        if income_date is None:                errors.append("Please provide a valid date.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "income_form.html", income=income,
                sources=INCOME_SOURCES, form=request.form,
            )

        income.title = title
        income.amount = amount
        income.source = source
        income.income_date = income_date
        income.notes = notes or None
        db.session.commit()

        flash("Income updated successfully.", "success")
        return redirect(url_for("main.dashboard"))

    return render_template(
        "income_form.html", income=income,
        sources=INCOME_SOURCES, form=None,
    )


@main.post("/incomes/<int:income_id>/delete")
def delete_income(income_id):
    income = db.get_or_404(Income, income_id)
    db.session.delete(income)
    db.session.commit()
    flash("Income deleted successfully.", "success")
    return redirect(url_for("main.dashboard"))


@main.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404