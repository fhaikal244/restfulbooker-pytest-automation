# Restful Booker API Automation 🐍

![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
[![CI](https://github.com/fhaikal244/restfulbooker-pytest-automation/actions/workflows/pytest.yml/badge.svg)](https://github.com/fhaikal244/restfulbooker-pytest-automation/actions/workflows/pytest.yml)
![Allure Report](https://img.shields.io/badge/Allure-Report-orange?style=for-the-badge)

API Automation Framework built from scratch using Pytest & Requests with Data Driven approach.

---

## 🛠️ Tech Stack
- **Pytest** — Test Framework
- **Requests** — API Testing
- **Allure** — Test Reporting
- **GitHub Actions** — CI/CD

---

## 📁 Project Structure

```plaintext
├── .github/workflows/    # CI/CD pipeline
├── tests/                # Test cases
│   ├── test_auth.py
│   └── test_booking.py
├── data/                 # JSON test data
├── utils/                # API helper
├── configs/              # Configuration
├── conftest.py           # Pytest fixtures
├── pytest.ini            # Pytest config
├── requirements.txt      # Dependencies
├── run.bat               # Run all + report
├── test.bat              # Run tests only
└── report.bat            # Generate report
```

---

## ✅ Test Coverage

### Auth Module
| TC | Test Case | Status |
|---|---|---|
| TC001 | Get token with valid credentials | ✅ |
| TC002 | Get token with invalid credentials | ✅ |

### Booking Module
| TC | Test Case | Status |
|---|---|---|
| TC001 | Get all bookings | ✅ |
| TC002 | Create new booking | ✅ |
| TC003 | Get booking by ID | ✅ |
| TC004 | Update booking | ✅ |
| TC005 | Partial update booking | ✅ |
| TC006 | Delete booking | ✅ |

---

## 🎯 Design Pattern
- **Data Driven Testing** — test data from JSON files
- **Helper Class** — reusable API helper
- **Fixtures** — reusable setup & teardown
- **OOP** — encapsulation & reusability

---

## 🚀 Getting Started

### Prerequisites
```plaintext
Python 3.11+
pip
Allure CLI
```

### Installation
```bash
# Clone repo
git clone https://github.com/fhaikal244/restfulbooker-pytest-automation.git

# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Tests

```bash
# Run all tests + generate report
.\run.bat

# Run tests only
.\test.bat

# Generate report only
.\report.bat

# Run specific test
pytest tests/ -k "test_get_all_bookings" -v
```

## 📊 Test Report

| Report | Link |
|---|---|
| 🔗 Live Allure Report | [View Here](https://fhaikal244.github.io/restfulbooker-pytest-automation) |

> Auto-updated on every push to master 🚀