from input_validator import InputValidator

# Usage examples
if InputValidator.is_empty(username):
    # Handle the error

if not InputValidator.is_numeric(age):
    # Handle the error

if not InputValidator.is_valid_email(email):
    # Handle the error

if not InputValidator.is_valid_username(username):
    # Handle the error

if not InputValidator.has_min_length(password, 8):
    # Handle the error

if not InputValidator.is_alpha(name):
    # Handle the error

if not InputValidator.is_digit(age):
    # Handle the error

if not InputValidator.is_alpha_numeric(username):
    # Handle the error

if not InputValidator.is_strong_password(password):
    # Handle the error
