# OWASP Juice Shop Security Automation

A security-focused SDET portfolio project built with Python, Pytest, Playwright, Requests, Allure, and GitHub Actions. The framework automates UI and API checks against the intentionally vulnerable OWASP Juice Shop application.

**Repository:** [juice-shop-security-automation](https://github.com/NancyVerma21/juice-shop-security-automation)

## Project Objectives

- Automate repeatable UI, API, and security-focused checks.
- Validate authentication and authorization behavior.
- Exercise input-validation scenarios.
- Capture automated test results and failure evidence.
- Run tests locally and through GitHub Actions CI.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Test automation language |
| Pytest | Test execution and organization |
| Playwright | Browser automation |
| Requests | HTTP API testing |
| Page Object Model (POM) | Organize reusable UI interactions |
| Allure | Test reporting |
| GitHub Actions | Continuous integration |
| Git | Version control |

## Automated Test Coverage

| Test area | Coverage |
|---|---|
| UI smoke testing | Homepage loading |
| UI authentication | Login page and invalid login |
| Product API | Product search and no-match search |
| Authentication API | Invalid credentials |
| Authorization API | Unauthenticated basket access |
| Input validation | HTML-like and long search inputs |
| Token validation | Malformed tokens and unsupported authorization schemes |

These tests exercise selected behaviors; they are not a complete penetration test or a guarantee that the application is secure.

## Project Structure

```text
juice-shop-security-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── api/
│   ├── __init__.py
│   └── client.py
├── pages/
│   ├── home_page.py
│   └── login_page.py
├── tests/
│   ├── ui/
│   │   ├── test_smoke.py
│   │   └── test_login.py
│   ├── api/
│   │   ├── test_products_api.py
│   │   └── test_auth_api.py
│   └── security/
│       ├── test_input_validation.py
│       └── test_session_security.py
├── screenshots/
├── traces/
├── test-results/
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

Install the following before running the tests:

- Python 3.11
- Node.js compatible with the Juice Shop version used locally
- Git
- Visual Studio Code (recommended)

The commands below use Windows PowerShell.

## Run Locally

### 1. Start OWASP Juice Shop

The target application must be running before you execute the tests.

Open a separate PowerShell terminal and run:

```powershell
cd C:\Users\hp\Desktop\juice-shop
npm start
```

Wait until the terminal displays a message indicating that the server is listening on port 3000.

Keep this terminal open.

Open the application in your browser:

http://localhost:3000

### 2. Open the automation project

Open a second PowerShell terminal:

```powershell
cd C:\Users\hp\Desktop\juice-shop-security-automation
```

Activate the existing virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### 4. Run all tests

```powershell
pytest
```

### 5. Run individual test groups

UI tests:

```powershell
pytest tests/ui
```

API tests:

```powershell
pytest tests/api
```

Security-focused tests:

```powershell
pytest tests/security
```

Run browser tests with a visible Chromium window:

```powershell
pytest tests/ui --headed
```

## Allure Reporting

Generate Allure result files while running the tests:

```powershell
pytest --alluredir=allure-results
```

The results are saved in the `allure-results` directory.

To open an interactive Allure report, install the Allure command-line tool and its required Java runtime if they are not already installed. Then run:

```powershell
allure serve allure-results
```

## Continuous Integration

The GitHub Actions workflow is located at:

`.github/workflows/tests.yml`

It is configured to:

- Run on pushes and pull requests targeting `main` or `master`.
- Support manual execution through `workflow_dispatch`.
- Set up Python and install the project dependencies.
- Start a containerized Juice Shop instance.
- Install Playwright Chromium.
- Wait for the application to become available.
- Execute the automated test suite.
- Upload Allure results and available test evidence as workflow artifacts.

Check the **Actions** tab in the GitHub repository to review workflow runs and their logs.

## Test Evidence

The project includes directories for screenshots, Playwright traces, and test results. Evidence is generated when the relevant test or configuration produces it; an empty directory does not mean evidence has been captured.

Allure result files can be generated using the command in the reporting section.

## Troubleshooting

**Connection refused or timeout**

Make sure Juice Shop is running at `http://localhost:3000` and that port 3000 is available.

**ModuleNotFoundError**

Activate the project's `.venv` and install dependencies using `python -m pip install -r requirements.txt`.

**Playwright browser error**

Run `python -m playwright install chromium` inside the activated virtual environment.

**Allure command not recognized**

Install the Allure CLI and ensure its executable is available on your PATH.

**GitHub Actions failure**

Open the failed workflow run in the Actions tab and inspect the first failing step.

## Responsible Testing

This project targets a local instance of OWASP Juice Shop, an intentionally vulnerable application designed for security education. Run security tests only against systems you own or are explicitly authorized to test.

## Author

**Nancy Verma**

GitHub: [NancyVerma21](https://github.com/NancyVerma21)

---

*Built as a hands-on SDET portfolio project to demonstrate UI automation, API testing, security-focused test design, reporting, and CI workflows.*