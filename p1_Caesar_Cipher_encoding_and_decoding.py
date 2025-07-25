def caesar_cipher(text, shift, encode=True):
    result = ""
    for i in text:
        if i.isalpha():
            
            if i.isupper():
                base = ord('A')
            else:
                base = ord('a')


            if encode:
                direction = shift
            else:
                direction = -shift

            shifted = (ord(i) - base + direction) % 26
            result += chr(base + shifted)
        else:
            result += i
    return result

message = input("Enter the message: ")
shift_value = int(input("Enter the shift value (number of positions): "))
operation = int(input("Enter 1 to encode or 0 to decode: "))

# Check if operation is encode (1) or decode (0)
if operation == 1:
    result = caesar_cipher(message, shift_value, encode=True)
    print("Encoded Message:", result)
elif operation == 0:
    result = caesar_cipher(message, shift_value, encode=False)
    print("Decoded Message:", result)
else:
    print("Invalid input! Please enter 1 to encode or 0 to decode.")
