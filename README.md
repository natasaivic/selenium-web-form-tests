# Selenium Web Form Tests

A portfolio project showcasing end-to-end UI automation of the Selenium web form using Python, Selenium WebDriver, and Pytest. The tests are structured using the Page Object Model (POM) to ensure maintainability, scalability, and readability.

## Features

This project covers:
- Input fields (text, password, textarea)
- Dropdowns and datalist
- File upload functionality
- Checkbox and radio button interactions
- Color, date, and range input testing
- Form submission validation
- Disabled and read-only fields handling

## Requirements

- Python 3.8+
- Chrome/Firefox browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/selenium-web-form-tests.git
cd selenium-web-form-tests
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

Generate HTML report:
```bash
pytest --html=reports/report.html
```
