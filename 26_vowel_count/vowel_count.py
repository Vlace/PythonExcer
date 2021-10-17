def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase_lower = phrase.lower()
    letter_map = {}
    for letter in phrase_lower:
        if letter in 'aeiou':
            if letter_map.get(letter) != None:
                sum = letter_map.get(letter)
                sum += 1
                letter_map[letter] = sum
            else:
                letter_map[letter]=1
    return letter_map
