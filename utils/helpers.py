import re
from datetime import datetime

def validateEmail(email: str) -> bool:
    """Validates an email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def formatDate(date_str: str, format: str = "%Y-%m-%d") -> datetime:
    """Formats a date string into a datetime object."""
    return datetime.strptime(date_str, format)
