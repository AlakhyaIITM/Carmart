from flask import current_app

def allowed_file(filename):
    """
    Check if a given filename has an allowed extension.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    if not filename or '.' not in filename:
        return False
    extension = filename.rsplit('.', 1)[1].lower()
    return extension in current_app.config.get('ALLOWED_EXTENSIONS', [])

def format_inr(value):
    """
    Format a numeric value as Indian Rupees (INR) with commas.

    Args:
        value (int or str): The value to format.

    Returns:
        str: The formatted value with the INR symbol.
    """
    try:
        value = int(value)
        return f"₹{value:,}"
    except (ValueError, TypeError):
        return f"₹{value}"
