# 📈 BrokerLab Paper Trading

A Python-based paper trading platform designed to simulate the core operations of a brokerage system, including order execution, portfolio tracking, market data integration, and risk management.

---

## 🧠 About the Project

BrokerLab is a backend-focused financial simulation platform that allows users to trade assets in a **virtual environment**, without using real money.

The goal is to replicate real brokerage workflows such as:
- order placement
- portfolio management
- trade execution
- profit and loss tracking
- risk validation

This project was built as a portfolio piece to demonstrate skills in **backend development, financial systems, and API design**.

---

## ⚙️ Features

- 🔐 User authentication (JWT)
- 💰 Virtual account balance
- 📊 Real-time market data (via API)
- 🛒 Simulated buy and sell orders (paper trading)
- 📈 Portfolio tracking (positions, P&L)
- ⚠️ Risk validation (balance and position checks)
- 📉 Performance analysis
- 📊 Dashboard (Streamlit)

---

## 🧱 Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite / PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (python-jose)
- **Market Data:** yfinance
- **Dashboard:** Streamlit
- **Data Visualization:** Plotly

---

## 🏗️ Architecture

```text
User
 ↓
FastAPI Backend
 ├── Auth Service
 ├── Market Data Service
 ├── Order Execution Engine
 ├── Portfolio Service
 └── Risk Management Service
 ↓
Database (SQLite/PostgreSQL)
 ↓
External Market Data API (yfinance)
