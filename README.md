# Bookstore Application

This project provides a simple model for representing books and coffee items in a bookstore environment. It demonstrates basic Object-Oriented Programming (OOP) concepts in Python, including classes, properties, and validation.

## Features

### Book Class
- **Attributes**: `title`, `page_count`
- **Validation**: Ensures `page_count` is an integer.
- **Methods**: `turn_page()` prints a reading message.

### Coffee Class
- **Attributes**: `size`, `price`
- **Validation**: Ensures `size` is either "Small", "Medium", or "Large".
- **Methods**: `tip()` increases the price by 1 and prints a thank-you message.

## Setup

1. Install dependencies:
   ```bash
   pipenv install
   ```
2. Enter the virtual environment:
   ```bash
   pipenv shell
   ```

## Running Tests

To run all tests:
```bash
pytest
```

To run specific tests:
```bash
pytest lib/testing/book_test.py
pytest lib/testing/coffee_test.py
```
