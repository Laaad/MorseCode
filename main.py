from morse_code_chart import morse_code_dict

message = input('What do you want me to transalte into the Morse code for you?')
decoded_message = ''

for character in message:
    try:
        decoded_message += morse_code_dict[character.upper()]+' '
    except KeyError:
        decoded_message += morse_code_dict[character]+' '

print(decoded_message)
