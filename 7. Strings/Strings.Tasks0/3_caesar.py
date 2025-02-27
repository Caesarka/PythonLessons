print('Let\'s encrypt your message using the Caesar cipher')
text = input('Enter your text: ')
shift = int(input('Enter shift value for your cipher: '))
shift_direction = input('Enter tthe direction in which you would like to shift the symbols, left/right: ')
encrypt_text = ''
if shift_direction == 'left':
    for ch in text:
        if ord(ch) in range(0, 65) or ord(ch) in range(91, 97) or ord(ch) in range(123, 128):
            encrypt_text += chr(ord(ch))
        elif ord(ch) - shift in range(0, 65) and ord(ch) in range(65, 91):
            encrypt_text += chr(91 - (shift - (ord(ch) - 65))) 
        elif ord(ch) - shift in range(70, 97) and ord(ch) in range(97, 123):
            encrypt_text += chr(123 - (shift - (ord(ch) - 97)))
        else:
            encrypt_text += chr(ord(ch) - shift)
elif shift_direction == 'right':
    for ch in text:
        if ord(ch) in range(0, 65) or ord(ch) in range(91, 97) or ord(ch) in range(123, 128):
            encrypt_text += chr(ord(ch))
        elif ord(ch) + shift in range(91, 128) and ord(ch) in range(65, 91):
            encrypt_text += chr(64 + (shift - (90 - ord(ch)))) 
        elif ord(ch) + shift in range(123, 128) and ord(ch) in range(97, 123):
            encrypt_text += chr(96 + (shift - (122 - ord(ch))))
        else:
            encrypt_text += chr(ord(ch) + shift)
print(encrypt_text)