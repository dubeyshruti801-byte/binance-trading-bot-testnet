# AI Trading Bot — Binance Futures Testnet

## 📌 Overview

This project is a modular **CLI-based AI Trading Bot** built in Python that interacts with Binance Futures Testnet API to place orders.

The project demonstrates:

* Clean backend architecture
* API integration
* CLI design
* Logging & validation
* Production-style folder structure

---

## 🧱 Project Architecture

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
│
├── project_files/
│   ├── requirements.txt
│   ├── README.md
│   └── logs/
```

---

## ⚙️ Features

* Binance Futures Testnet integration
* HMAC SHA256 request signing
* CLI-based order placement
* Structured logging
* Modular production-style architecture
* Input validation

---

## 🔑 Environment Setup

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```

Use **Binance Futures Testnet** keys only.

---

## ▶️ Installation

Create virtual environment:

```
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r project_files/requirements.txt
```

---

## 🚀 How to Run

Example:

```
python cli.py BTCUSDT BUY MARKET 0.001
```

Arguments:

* SYMBOL → Trading pair (BTCUSDT)
* SIDE → BUY / SELL
* ORDER_TYPE → MARKET
* QUANTITY → Order size

---

## 🧪 Sample Output

```
===== ORDER REQUEST =====
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001
=========================
```

Logs capture request and response for debugging.

---

## 📝 Logging

Logs are stored in:

```
project_files/logs/
```

They include:

* Request payload
* API response
* Errors

This demonstrates production-ready debugging practice.

---

## ⚠️ Notes

* Tested on Binance Futures Testnet
* Requires valid Testnet API keys
* Focus is architecture & API integration (not strategy)

---

## 📚 Tech Stack

* Python
* Requests
* Typer (CLI)
* python-dotenv
* Logging

---

## 🎯 Learning Goals

* API integration
* CLI application design
* Secure request signing
* Real-world backend structure
* Production logging

---

## 👩‍💻 Author

Shruti Dubey
