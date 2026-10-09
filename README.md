# OWASP Juice Shop Security Automation

A security-focused SDET portfolio project using Python, Pytest, Playwright, Requests, Allure, and GitHub Actions.

## Tech Stack

- Python 3.11
- Pytest
- Playwright
- Requests for API testing
- Page Object Model (POM)
- Allure reporting
- GitHub Actions CI/CD

## Automated Test Coverage

| Area | Coverage |
|---|---|
| UI smoke testing | Homepage loads |
| UI authentication | Login page and invalid login |
| Product API | Product search and empty results |
| Authentication API | Invalid credentials |
| Authorization API | Unauthenticated basket access |
| Input validation | HTML-like and long search inputs |
| Token validation | Malformed token and unsupported authorization scheme |

## Project Structure

```text
juice-shop-security-automation/
├── .github/workflows/tests.yml
├── api/
│   ├── __init__.py
│   └── client.py
├── pages/
│   ├── home_page.py
│   └── login_page.py
├── tests/
│   ├── ui/
│   ├── api/
│   └── security/
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
