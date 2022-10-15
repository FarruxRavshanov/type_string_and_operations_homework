def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    a = x1
    b = x2
    c = x3
    d = f"[{a}, {b}, {c}]"
    return d

print(main(3, 4, 5))