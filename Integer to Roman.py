x=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in x:
            while num >= i:
                roman += r
                num -= i

    return roman

# test 
n=int(input("Enter any number to change in Roman Number: "))
print(num2roman(n))