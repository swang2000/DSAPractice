def plusOne(digits):
    plus = 1
    for i in range(len(digits)-1,-1, -1):
        plus, dig = divmod(plus + digits[i], 10)
        digits[i] = dig
    return digits


plusOne([1,2,3])


