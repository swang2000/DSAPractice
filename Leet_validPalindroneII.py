def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    temp = ''.join([x for x in list(s.lower()) if x != ' '])
    return temp == temp[::-1]

a= "A man, a plan, a canal: Panama"
isPalindrome(a)