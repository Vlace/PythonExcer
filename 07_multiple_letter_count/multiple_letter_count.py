def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict_letters = {}
    for letter in phrase:
        if f'{letter}' in dict_letters:
            count = dict_letters.get(letter) + 1
            dict_letters[letter] = count
            
        else:
            dict_letters[letter] = 1
    return dict_letters