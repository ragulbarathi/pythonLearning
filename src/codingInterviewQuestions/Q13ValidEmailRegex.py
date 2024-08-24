import re

# Regex pattern for validating an email
email_regex = re.compile(
    r"^(?=.{1,254})(?=.{1,64}@.{1,255}$)(?:(?!\.)[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\\x20-\x21\x23-\x5b\x5d-\x7e]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?!\.)[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*|\[(?:(?:[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(?:[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\])$"
)


def is_valid_email(email: str) -> bool:
    return re.match(email_regex, email) is not None


# Test the function
test_email = "example@example.com"
print(is_valid_email(test_email))  # Output: True
