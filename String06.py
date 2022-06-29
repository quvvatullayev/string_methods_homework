from curses.ascii import isdigit


def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    s = str(s)
    return s.isdigit()