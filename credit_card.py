def credit(num):
    num = str(int(num))
    digit = len(num)

    if num[:1] == '4':
        return 'Visa'

    if num[:4] == '6011':
        return 'Discover'
    if num[:2] == '37' or num[:2] == '34':
        return 'AMEX'
    if num[:2] == '51' or num[:2] == '52' or num[:2] == '53'or num[:2] == '54' or num[:2] == '55':
        return 'MasterCard'
    if digit <= 16:
        return 'Invalid'

print(credit(5938488484844))
