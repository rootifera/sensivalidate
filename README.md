
  

# Sensivalidate

  

`Sensivalidate` is a Python package designed to help identify sensitive data in text, including credit card numbers, UK bank account numbers, UK sort codes, and UK postcodes. It uses regular expressions for pattern matching, and performs real validation for credit card numbers using the `creditcard` Python package.

  

## Features

  

-  **Credit Card Validation**: Validates credit card numbers by checking for valid formats and using the `creditcard` package to verify the card's authenticity.

-  **UK Bank Account Number Detection**: Identifies UK bank account numbers (8-digit numbers).

-  **UK Sort Code Detection**: Detects UK sort codes in formats like `xx-xx-xx`, `xxxxxxxx`, and `xx xx xx`.

-  **UK Postcode Detection**: Matches UK postcodes based on standard patterns.

  

**Note**: The package performs pattern matching for bank account numbers, sort codes, and postcodes, but only credit card numbers are validated for authenticity.

  

## Installation

  

You can install the package using pip:

  

```bash

pip install sensivalidate

```

  

Or, if you've downloaded the package:

  

```bash

pip install sensivalidate-0.1.tar.gz

```

  

## Usage

  

```python

from sensivalidate import is_sensitive_data

result = is_sensitive_data("your text here")

if result:
	print("Sensitive data detected.")
else:
	print("No sensitive data found.")

```

  

The `is_sensitive_data` function checks the provided text for sensitive data and returns `True` if any of the following are detected:

- Valid credit card number

- UK bank account number

- UK sort code

- UK postcode

  

## Code Overview

  

-  **`_is_credit_card(text)`**: Detects and validates credit card numbers using regex and the `creditcard` package.

-  **`_is_uk_bank_account_and_sort_code(text)`**: Matches UK bank account numbers and sort codes.

-  **`_is_uk_postcode(text)`**: Matches UK postcodes.

-  **`is_sensitive_data(text)`**: The main function that checks for sensitive data by calling the individual validator functions.

  

## Contributing

  

Feel free to fork this repository and contribute. If you find any bugs or have ideas for improvements, please create an issue or submit a pull request.

  

## License

  

This project is licensed under the MIT License.