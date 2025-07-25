def indian_currency_format(amount):
    amount_str = f"{amount:.4f}".rstrip('0').rstrip('.')
    
    if '.' in amount_str:
        integer_part, decimal_part = amount_str.split('.')
    else:
        integer_part, decimal_part = amount_str, ''
    
    if len(integer_part) > 3:
        post = integer_part[-3:]
        pre = integer_part[:-3]
    else:
        pre = ''
        post = integer_part

    parts = []
    i = len(pre)
    while i > 0:
        start = max(i - 2, 0)
        parts.append(pre[start:i])
        i -= 2

    parts.reverse()

    if parts:
        formatted = ','.join(parts) + ',' + post
    else:
        formatted = post

    if decimal_part:
        return formatted + '.' + decimal_part
    else:
        return formatted

amount = input("Enter amount: ")
try:
    value = float(amount)
    print("Formatted Indian Currency:", indian_currency_format(value))
except ValueError:
    print("Please enter a valid number.")
