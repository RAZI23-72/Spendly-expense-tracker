"""Seed Spendly with 13 months of Indian financial data."""
from datetime import date
from decimal import Decimal
from app import create_app
from app.extensions import db
from app.models import Expense, Income


def d(y, m, day):
    return date(y, m, day)


def r(amount):
    return Decimal(str(amount))


INCOME_DATA = [
    ("Monthly salary", 55000, "Salary", d(2025, 9, 1), "September paycheck"),
    ("Freelance project", 12000, "Freelance", d(2025, 9, 18), "Logo design work"),
    ("Monthly salary", 55000, "Salary", d(2025, 10, 1), "October paycheck"),
    ("Diwali bonus", 15000, "Bonus", d(2025, 10, 15), "Festival bonus"),
    ("Monthly salary", 55000, "Salary", d(2025, 11, 1), "November paycheck"),
    ("Monthly salary", 55000, "Salary", d(2025, 12, 1), "December paycheck"),
    ("Freelance project", 8000, "Freelance", d(2025, 12, 20), "Website revamp"),
    ("Monthly salary", 55000, "Salary", d(2026, 1, 1), "January paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 2, 1), "February paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 3, 1), "March paycheck"),
    ("Annual performance bonus", 20000, "Bonus", d(2026, 3, 25), "FY-end bonus"),
    ("Monthly salary", 55000, "Salary", d(2026, 4, 1), "April paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 5, 1), "May paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 6, 1), "June paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 7, 1), "July paycheck"),
    ("Monthly salary", 55000, "Salary", d(2026, 8, 1), "August paycheck"),
    ("Freelance project", 10000, "Freelance", d(2026, 8, 22), "App consulting"),
    ("Monthly salary", 55000, "Salary", d(2026, 9, 1), "September paycheck"),
]


EXPENSE_DATA = [
    ("House rent", 18000, "Housing", d(2025, 9, 1), "Monthly rent"),
    ("Electricity bill", 850, "Utilities", d(2025, 9, 5), "September power"),
    ("Grocery shopping", 3200, "Food", d(2025, 9, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2025, 9, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2025, 9, 10), "Jio monthly plan"),
    ("Grocery shopping", 2800, "Food", d(2025, 9, 13), "Weekly groceries"),
    ("Dinner out", 1200, "Food", d(2025, 9, 15), "Weekend dinner"),
    ("Gym membership", 1500, "Healthcare", d(2025, 9, 18), "Monthly gym"),
    ("Grocery shopping", 3100, "Food", d(2025, 9, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2025, 9, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2025, 9, 25), "Broadband"),
    ("Grocery shopping", 2900, "Food", d(2025, 9, 27), "Weekly groceries"),
    ("Movie tickets", 800, "Entertainment", d(2025, 9, 28), "PVR outing"),
    ("Pharmacy", 400, "Healthcare", d(2025, 9, 29), "Medicines"),
    ("House rent", 18000, "Housing", d(2025, 10, 1), "Monthly rent"),
    ("Electricity bill", 900, "Utilities", d(2025, 10, 5), "October power"),
    ("Diwali shopping", 12000, "Shopping", d(2025, 10, 12), "Festival clothes + gifts"),
    ("Sweets & dry fruits", 3500, "Food", d(2025, 10, 13), "Diwali treats"),
    ("Grocery shopping", 3000, "Food", d(2025, 10, 8), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2025, 10, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2025, 10, 10), "Jio monthly"),
    ("Dinner out", 1500, "Food", d(2025, 10, 14), "Diwali dinner"),
    ("Grocery shopping", 3200, "Food", d(2025, 10, 20), "Weekly groceries"),
    ("Petrol", 2600, "Transportation", d(2025, 10, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2025, 10, 25), "Broadband"),
    ("Grocery shopping", 2900, "Food", d(2025, 10, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2025, 10, 18), "Monthly gym"),
    ("Pharmacy", 650, "Healthcare", d(2025, 10, 29), "Medicines"),
    ("House rent", 18000, "Housing", d(2025, 11, 1), "Monthly rent"),
    ("Electricity bill", 780, "Utilities", d(2025, 11, 5), "November power"),
    ("Grocery shopping", 3100, "Food", d(2025, 11, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2025, 11, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2025, 11, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2025, 11, 13), "Weekly groceries"),
    ("Doctor visit", 1000, "Healthcare", d(2025, 11, 15), "General checkup"),
    ("Grocery shopping", 3200, "Food", d(2025, 11, 20), "Weekly groceries"),
    ("Petrol", 2400, "Transportation", d(2025, 11, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2025, 11, 25), "Broadband"),
    ("Grocery shopping", 2800, "Food", d(2025, 11, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2025, 11, 18), "Monthly gym"),
    ("Book purchase", 800, "Education", d(2025, 11, 28), "Fiction novel"),
    ("Restaurant", 1200, "Food", d(2025, 11, 30), "Family dinner"),
    ("House rent", 18000, "Housing", d(2025, 12, 1), "Monthly rent"),
    ("Electricity bill", 950, "Utilities", d(2025, 12, 5), "December power"),
    ("Grocery shopping", 3300, "Food", d(2025, 12, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2025, 12, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2025, 12, 10), "Jio monthly"),
    ("Christmas party", 2500, "Entertainment", d(2025, 12, 24), "Office party"),
    ("Grocery shopping", 3100, "Food", d(2025, 12, 13), "Weekly groceries"),
    ("New Year shopping", 4500, "Shopping", d(2025, 12, 30), "Party clothes"),
    ("Grocery shopping", 3000, "Food", d(2025, 12, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2025, 12, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2025, 12, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2025, 12, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2025, 12, 18), "Monthly gym"),
    ("Gifts", 4200, "Shopping", d(2025, 12, 23), "Christmas gifts"),
    ("House rent", 18000, "Housing", d(2026, 1, 1), "Monthly rent"),
    ("Electricity bill", 820, "Utilities", d(2026, 1, 5), "January power"),
    ("Grocery shopping", 3200, "Food", d(2026, 1, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 1, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 1, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 1, 13), "Weekly groceries"),
    ("New Year resolution gym", 3500, "Healthcare", d(2026, 1, 15), "3-month gym plan"),
    ("Grocery shopping", 3100, "Food", d(2026, 1, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2026, 1, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 1, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 1, 27), "Weekly groceries"),
    ("Movie tickets", 800, "Entertainment", d(2026, 1, 26), "Republic Day movie"),
    ("Restaurant", 1200, "Food", d(2026, 1, 31), "Family dinner"),
    ("House rent", 18000, "Housing", d(2026, 2, 1), "Monthly rent"),
    ("Electricity bill", 760, "Utilities", d(2026, 2, 5), "February power"),
    ("Grocery shopping", 3100, "Food", d(2026, 2, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 2, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 2, 10), "Jio monthly"),
    ("Valentine's dinner", 2200, "Food", d(2026, 2, 14), "Special date"),
    ("Grocery shopping", 2900, "Food", d(2026, 2, 13), "Weekly groceries"),
    ("Gift for spouse", 3000, "Shopping", d(2026, 2, 14), "Valentine gift"),
    ("Grocery shopping", 3100, "Food", d(2026, 2, 20), "Weekly groceries"),
    ("Petrol", 2400, "Transportation", d(2026, 2, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 2, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 2, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 2, 18), "Monthly gym"),
    ("House rent", 18000, "Housing", d(2026, 3, 1), "Monthly rent"),
    ("Electricity bill", 850, "Utilities", d(2026, 3, 5), "March power"),
    ("Grocery shopping", 3200, "Food", d(2026, 3, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 3, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 3, 10), "Jio monthly"),
    ("Holi colors & sweets", 1800, "Shopping", d(2026, 3, 13), "Holi celebration"),
    ("Grocery shopping", 2900, "Food", d(2026, 3, 13), "Weekly groceries"),
    ("Holi party", 1500, "Entertainment", d(2026, 3, 14), "Friends gathering"),
    ("Grocery shopping", 3100, "Food", d(2026, 3, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2026, 3, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 3, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 3, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 3, 18), "Monthly gym"),
    ("Annual insurance", 8000, "Healthcare", d(2026, 3, 30), "Health insurance premium"),
    ("House rent", 18000, "Housing", d(2026, 4, 1), "Monthly rent"),
    ("Electricity bill", 920, "Utilities", d(2026, 4, 5), "April power (AC)"),
    ("Grocery shopping", 3200, "Food", d(2026, 4, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 4, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 4, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 4, 13), "Weekly groceries"),
    ("Summer clothes", 3500, "Shopping", d(2026, 4, 15), "New summer wardrobe"),
    ("Grocery shopping", 3100, "Food", d(2026, 4, 20), "Weekly groceries"),
    ("Petrol", 2600, "Transportation", d(2026, 4, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 4, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 4, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 4, 18), "Monthly gym"),
    ("Weekend trip", 4000, "Travel", d(2026, 4, 28), "Lonavala getaway"),
    ("House rent", 18000, "Housing", d(2026, 5, 1), "Monthly rent"),
    ("Electricity bill", 1100, "Utilities", d(2026, 5, 5), "May power (AC heavy)"),
    ("Grocery shopping", 3100, "Food", d(2026, 5, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 5, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 5, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 5, 13), "Weekly groceries"),
    ("Ice cream & cold drinks", 800, "Food", d(2026, 5, 15), "Summer treats"),
    ("Grocery shopping", 3100, "Food", d(2026, 5, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2026, 5, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 5, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 5, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 5, 18), "Monthly gym"),
    ("Air cooler", 5500, "Shopping", d(2026, 5, 12), "Summer appliance"),
    ("House rent", 18000, "Housing", d(2026, 6, 1), "Monthly rent"),
    ("Electricity bill", 1250, "Utilities", d(2026, 6, 5), "June power (AC)"),
    ("Grocery shopping", 3200, "Food", d(2026, 6, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 6, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 6, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 6, 13), "Weekly groceries"),
    ("Monsoon umbrella", 700, "Shopping", d(2026, 6, 15), "Rainy season prep"),
    ("Grocery shopping", 3100, "Food", d(2026, 6, 20), "Weekly groceries"),
    ("Petrol", 2600, "Transportation", d(2026, 6, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 6, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 6, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 6, 18), "Monthly gym"),
    ("Weekend getaway", 8000, "Travel", d(2026, 6, 28), "Goa trip"),
    ("House rent", 18000, "Housing", d(2026, 7, 1), "Monthly rent"),
    ("Electricity bill", 1150, "Utilities", d(2026, 7, 5), "July power"),
    ("Grocery shopping", 3100, "Food", d(2026, 7, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 7, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 7, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 7, 13), "Weekly groceries"),
    ("Monsoon shopping", 2000, "Shopping", d(2026, 7, 15), "Raincoat + shoes"),
    ("Grocery shopping", 3100, "Food", d(2026, 7, 20), "Weekly groceries"),
    ("Petrol", 2500, "Transportation", d(2026, 7, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 7, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 7, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 7, 18), "Monthly gym"),
    ("Doctor visit", 1200, "Healthcare", d(2026, 7, 30), "Monsoon fever checkup"),
    ("House rent", 18000, "Housing", d(2026, 8, 1), "Monthly rent"),
    ("Electricity bill", 1050, "Utilities", d(2026, 8, 5), "August power"),
    ("Grocery shopping", 3200, "Food", d(2026, 8, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 8, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 8, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 8, 13), "Weekly groceries"),
    ("Raksha Bandhan gifts", 2500, "Shopping", d(2026, 8, 15), "Gifts for siblings"),
    ("Grocery shopping", 3100, "Food", d(2026, 8, 20), "Weekly groceries"),
    ("Petrol", 2600, "Transportation", d(2026, 8, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 8, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 8, 27), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 8, 18), "Monthly gym"),
    ("Independence Day outing", 800, "Entertainment", d(2026, 8, 15), "Friends picnic"),
    ("Restaurant", 1200, "Food", d(2026, 8, 31), "Month-end dinner"),
    ("House rent", 18000, "Housing", d(2026, 9, 1), "Monthly rent"),
    ("Electricity bill", 1050, "Utilities", d(2026, 9, 5), "September power"),
    ("Grocery shopping", 3200, "Food", d(2026, 9, 6), "Weekly groceries"),
    ("Metro card recharge", 500, "Transportation", d(2026, 9, 8), "Monthly transit"),
    ("Mobile recharge", 399, "Utilities", d(2026, 9, 10), "Jio monthly"),
    ("Grocery shopping", 2900, "Food", d(2026, 9, 13), "Weekly groceries"),
    ("Gym membership", 1500, "Healthcare", d(2026, 9, 18), "Monthly gym"),
    ("Grocery shopping", 3100, "Food", d(2026, 9, 20), "Weekly groceries"),
    ("Petrol", 2600, "Transportation", d(2026, 9, 22), "Car fuel"),
    ("Internet bill", 999, "Utilities", d(2026, 9, 25), "Broadband"),
    ("Grocery shopping", 2950, "Food", d(2026, 9, 27), "Weekly groceries"),
    ("Coffee with friend", 450, "Food", d(2026, 9, 29), "Cafe catch-up"),
]


def seed():
    app = create_app()
    with app.app_context():
        print("Clearing existing data...")
        db.session.query(Expense).delete()
        db.session.query(Income).delete()
        db.session.commit()

        print(f"Adding {len(INCOME_DATA)} income entries...")
        for title, amount, source, inc_date, notes in INCOME_DATA:
            db.session.add(Income(title=title, amount=r(amount), source=source, income_date=inc_date, notes=notes))

        print(f"Adding {len(EXPENSE_DATA)} expense entries...")
        for title, amount, category, exp_date, notes in EXPENSE_DATA:
            db.session.add(Expense(title=title, amount=r(amount), category=category, expense_date=exp_date, notes=notes))

        db.session.commit()

        total_income = sum(i[1] for i in INCOME_DATA)
        total_expense = sum(e[1] for e in EXPENSE_DATA)

        print("\n" + "=" * 50)
        print("  SEED COMPLETE")
        print("=" * 50)
        print(f"  Income entries : {len(INCOME_DATA)}")
        print(f"  Expense entries: {len(EXPENSE_DATA)}")
        print(f"  Total income   : Rs.{total_income:,.2f}")
        print(f"  Total expenses : Rs.{total_expense:,.2f}")
        print(f"  Net balance    : Rs.{total_income - total_expense:,.2f}")
        print("=" * 50)


if __name__ == "__main__":
    seed()