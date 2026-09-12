# 💰 Spendly — Personal Expense & Income Tracker

A lightweight personal finance web app built with **Flask** and **SQLite**. Track your daily expenses, log your monthly salary, and instantly see your **balance** — all in Indian Rupees (₹).

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.0-green?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Table of Contents

- [What is Spendly?](#-what-is-spendly)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Why SQLite?](#-why-sqlite)
- [Project Structure](#-project-structure)
- [How the App Works](#-how-the-app-works)
- [How the Database Works](#-how-the-database-works)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Data Model](#-data-model)
- [Route Reference](#-route-reference)
- [Screenshots](#-screenshots)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 What is Spendly?

**Spendly** is a self-hosted personal finance tracker. Unlike spreadsheets, it:

- Automatically **calculates** your monthly and all-time balance
- Separates **income** (money in) from **expenses** (money out)
- Groups expenses by **category** with visual progress bars
- Lets you **compare months** side-by-side with a month picker
- Runs entirely **on your machine** — no cloud, no signup, no tracking

Built as a learning project to demonstrate a clean **Flask + SQLAlchemy + SQLite** stack with the **app factory pattern**.

---

## ✨ Features

### Core
- 💸 **Expense tracking** — Add, edit, delete expenses with 10 categories
- 💰 **Income tracking** — Log salary, freelance, bonuses, gifts
- ⚖️ **Balance calculation** — Automatic `income − expenses` per month
- 📅 **Month picker** — Navigate any month from a dropdown
- 📊 **Category breakdown** — See where your money goes with progress bars
- 🇮🇳 **INR-first** — All amounts in ₹ (Indian Rupees)

### Technical
- 🏭 **App factory pattern** — Clean, testable Flask setup
- 🔵 **Blueprints** — Modular route organization
- 💾 **Decimal precision** — No floating-point errors on money
- ✅ **Server-side validation** — Can't be bypassed
- 🔒 **CSRF-safe deletes** — POST-only, with confirmation
- 📱 **Responsive design** — Works on mobile, tablet, desktop
- 🎨 **Custom CSS** — No framework bloat

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Language** | Python 3.9+ | Backend logic |
| **Framework** | Flask 3.1.0 | HTTP routing, templating |
| **ORM** | Flask-SQLAlchemy 3.1.1 | Database abstraction |
| **Database** | SQLite 3 | Data persistence |
| **Templating** | Jinja2 | HTML rendering |
| **Frontend** | HTML5, CSS3, vanilla JS | UI |
| **Config** | python-dotenv | Environment variables |
| **Fonts** | DM Sans, Space Grotesk | Typography |

---

## 🤔 Why SQLite?

SQLite was chosen deliberately for this project. Here's why:

### ✅ Advantages for This Project

| Reason | Explanation |
|--------|-------------|
| **Zero configuration** | No separate server to install, start, or manage. The DB is a single file: `instance/expenses.db` |
| **Single-user** | Personal finance tracking is inherently single-user. No concurrent writes needed |
| **Portable** | Copy `expenses.db` and you have a full backup. Move it between machines trivially |
| **Perfect for prototyping** | No migrations, no connection strings, no credentials |
| **Built into Python** | `sqlite3` module ships with Python — no `pip install` needed at the DB level |
| **ACID-compliant** | Full transaction support (money data requires this) |
| **Fast enough** | Reading 10,000 rows is instant; writing is < 1ms |
| **Free forever** | No hosting costs, no limits |

### ❌ When SQLite Would NOT Be Suitable

- **Multi-user concurrent writes** (e.g., a SaaS with thousands of users) → Use PostgreSQL
- **Large datasets** (> 1 TB) → Use PostgreSQL or MySQL
- **Distributed/replicated systems** → Use PostgreSQL with replicas
- **Complex analytics** → Use a data warehouse (BigQuery, Snowflake)

### 🔄 Migration Path

If Spendly ever grows beyond single-user, migrating is straightforward because **SQLAlchemy abstracts the DB**:

```python
# Currently (SQLite)
SQLALCHEMY_DATABASE_URI = "sqlite:///instance/expenses.db"

# Switch to PostgreSQL (just change this line)
SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/spendly"
