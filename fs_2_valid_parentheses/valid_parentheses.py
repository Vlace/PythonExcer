def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left_paren = parens[0]
    right_paren = parens[len(parens)-1]
    if len(parens) % 2 != 0:
        return False
    if left_paren == ')':
        return False
    if right_paren == '(':
        return False
    return True