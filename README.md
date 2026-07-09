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
```bash
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

---

## 🌐 Target Application

| | |
|---|---|
| URL | https://restful-booker.herokuapp.com |
| Docs | https://restful-booker.herokuapp.com/apidoc |

---

## 📊 CI/CD

Automated testing runs on every push via GitHub Actions.