def main(first,last):
    """
    Given two strings, first_name and last_name, return a single string in the format "last, first".
    Args:
        first: str
        last: str
    Returns:
        str: return answer.
    """
    d = first + ' ' + last
    return d

print(main('Farruxjon,', 'Ravshanov'))