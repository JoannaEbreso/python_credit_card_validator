def getDigit(number_string):
    if len(number_string) == 2:
        digit_sum = int(number_string[0]) + int(number_string[1])
    else:
        digit_sum = int(number_string)

    return digit_sum

def isValid(creditCardNumber):
    creditCardNumber_string = str(creditCardNumber)
    reversed_creditCardNumber = creditCardNumber_string[::-1]
    index = 0
    doubled_reversed_ccn = ""
    for digit in reversed_creditCardNumber:
        if index%2 == 1:
            doubled_digit = int(reversed_creditCardNumber[index])**2
            doubled_digit_string = str(doubled_digit)
            two_digit_sum_string = str(getDigit(doubled_digit_string))
            doubled_reversed_ccn += two_digit_sum_string
            index += 1
        else:
            doubled_reversed_ccn += digit
            index += 1


