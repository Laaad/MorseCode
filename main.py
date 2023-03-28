from morse_code_chart import morse_code_dict

message = input('What do you want me to transalte into the Morse code for you?')
decoded_message = ''
for character in message:
    for key in morse_code_dict:
        if character.upper() == key:
            decoded_message += morse_code_dict[key]
            decoded_message += " "
print(decoded_message)


