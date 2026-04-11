## Requirements

- Python 3.11+
- Docker
- just
- uv

# 💰 Telegram Expense Tracker Bot

A simple Telegram bot for tracking personal expenses with categories, history, and editing features.

---

## 🎯 Goal

A chat-based expense tracker where users can:

- add expenses via text input
- manage categories (CRUD)
- view expenses by date
- edit or delete expenses via buttons

---

## 🧩 Core Features

## 🗂 Categories (CRUD)

Users can:

- create categories
- rename categories
- delete categories

⚠️ Deleting a category does NOT delete expenses.  
Old expenses remain in history.

---

## 💸 Add Expense

Format:

<category> <amount> [description]

Examples:

food 500  
coffee 800 starbucks latte  
taxi 1200 bolt ride home  

---

## 📊 View Expenses

### Commands:

/today → today's expenses  
/expenses → expenses grouped by date  

---

### Output example:

📊 11 April 2026

food: 1500  
coffee: 800  
taxi: 1200  

Total: 3500  

---

## ✏️ Edit Expenses

Each expense has an Edit button.

### Editable fields:

- category
- amount
- description
- delete expense

---

### Example UI:

☕ coffee 800 — starbucks latte  
[ Edit ]

After click:

Edit Expense:

[ Change category ]  
[ Change amount ]  
[ Change description ]  
[ Delete ]

---

## 🗄 Data Model

### Expense

- id  
- user_id  
- category_id  
- amount  
- description (optional)  
- created_at  

---

### Category

- id  
- user_id  
- name  
- created_at  

---

## ⚙️ Architecture

bot.py → Telegram handlers  
expenses.py → expense logic (CRUD)  
categories.py → category logic (CRUD)  
parser.py → input parsing  
db.py → database layer  

---

## 🧠 Concept

A minimal chat-first personal finance tracker with structured input, category management, and inline editing via Telegram buttons.