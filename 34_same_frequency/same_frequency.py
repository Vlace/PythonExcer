def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_string = str(num1)
    num2_string = str(num2)
    num1_count = {}
    num2_count = {}
    for num in num1_string:
        if num in num1_count:
            sum = num1_count.get(num)
            sum += 1
            num1_count[num] = sum
        else:
            num1_count[num] = 1
    for num in num2_string:
        if num in num2_count:
            sum = num2_count.get(num)
            sum += 1
            num2_count[num] = sum
        else:
            num2_count[num] = 1
    for key in num1_count.keys():
        if num1_count.get(key) != num2_count.get(key):
            return False
    return True