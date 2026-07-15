def highlight(text, color_name):
    """
    Returns text wrapped in ANSI escape codes to change its background color.
    Background colors available: red, green, yellow, blue, purple, cyan.
    """
    # Notice these use 100+ numbers instead of 90+!
    codes = {
        "red": "\033[101m",
        "green": "\033[102m",
        "yellow": "\033[103m",
        "blue": "\033[104m",
        "purple": "\033[105m",
        "cyan": "\033[106m",
        "end": "\033[0m"  # Always reset to normal!
    }
    
    selected_code = codes.get(color_name.lower(), "")
    
    if selected_code:
        return f"{selected_code}{text}{codes['end']}"
    return text
