def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    new_list = []
    index_list = []
    new_word = list(s)
    counter = 0
    for letter in s:
        if letter.lower() in 'aeiou':
            new_list.append(letter)
            index_list.append(new_word.index(letter, counter))
            counter = new_word.index(letter, counter)+1
    new_list.reverse()
    counter = 0
    while counter < len(new_list):
        new_word.pop(index_list[counter])
        new_word.insert(index_list[counter], new_list[counter])
        counter += 1
    return ''.join(new_word)