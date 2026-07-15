def color(text, color_name):
    """
    Returns text wrapped in ANSI escape codes to change its color.
    Colors available: red, green, yellow, blue, purple, cyan.
    """
    codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "end": "\033[0m"
    }
    
    selected_code = codes.get(color_name.lower(), "")
    if selected_code:
        return f"{selected_code}{text}{codes['end']}"
    return text
