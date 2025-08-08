# Selenium Web Form Tests

A comprehensive portfolio project demonstrating professional end-to-end UI automation testing of web forms using Python, Selenium WebDriver, and Pytest. The test suite employs modular architecture and industry best practices to ensure maintainability, scalability, and reliability.

## Architecture Overview

This project implements a **modular test structure** where each test file focuses on specific form element categories, promoting code reusability and maintainability through shared fixtures and clear separation of concerns.

## Test Coverage

### Core Form Elements
- **Text Inputs** (`test_text_inputs.py`)
  - Standard text fields with input validation
  - Password fields with secure data handling  
  - Multi-line textarea with content verification

- **Form Selection Controls** (`test_selection_controls.py`)
  - Independent checkbox interactions (checked and default states)
  - Mutually exclusive radio button group behavior
  - HTML `<select>` dropdowns with multiple selection methods (by text and value)
  - HTML `<datalist>` autocomplete inputs with dynamic suggestions

- **Advanced Input Types** (`test_input_types.py`)
  - Color picker with hex value validation
  - Date picker with format verification
  - Range slider with dynamic value changes
  - File upload with temporary file handling

- **Field State Validation** (`test_field_states.py`)
  - Disabled field interaction prevention
  - Read-only field modification restrictions

- **End-to-End Testing** (`test_form_submission.py`)
  - Complete form workflow with all field types
  - Form submission and success message validation

## Technical Implementation

### Key Features
- **Centralized Configuration**: Shared WebDriver fixtures in `conftest.py` eliminate code duplication
- **Automatic Driver Management**: WebDriver-Manager handles browser driver installation
- **Error Handling**: Try-catch-finally blocks ensure proper resource cleanup
- **Cross-browser Support**: Chrome WebDriver with extensible configuration
- **Detailed Reporting**: Console output and HTML test reports

### Test Structure Benefits
- **Modularity**: Each test file handles specific form element types
- **Independence**: Tests can run individually or as a complete suite  
- **Maintainability**: Changes to specific elements only affect relevant test files
- **Scalability**: Easy to add new test categories without affecting existing tests

## Requirements

- **Python**: 3.8 or higher
- **Browser**: Chrome (automatically managed)
- **Dependencies**: Listed in `requirements.txt`

## Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/selenium-web-form-tests.git
cd selenium-web-form-tests
```

### 2. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

### Execute All Tests
```bash
pytest
```

### Run Specific Test Categories
```bash
# Text input tests only
pytest test_cases/test_text_inputs.py

# Form selection control tests only  
pytest test_cases/test_selection_controls.py

# Advanced input type tests
pytest test_cases/test_input_types.py
```

### Generate Detailed Reports
```bash
# HTML report with detailed results
pytest --html=reports/report.html

# Verbose console output
pytest -v

# Show test execution details
pytest -s
```

## Project Structure
```
selenium-web-form-tests/
├── test_cases/
│   ├── test_first_test.py           # Basic form submission test (original)
│   ├── test_text_inputs.py          # Text, password, textarea
│   ├── test_selection_controls.py   # Checkboxes, radio buttons, dropdowns
│   ├── test_advanced_input_types.py # Color, date, range, file inputs
│   ├── test_field_states.py         # Disabled and readonly validation
│   └── test_form_submission.py      # Complete end-to-end workflow
├── conftest.py                  # Shared test fixtures
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```
