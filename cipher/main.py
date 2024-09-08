#cipher

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True
def encrypt(orignal_text, shift_amt):
    cipher_string = ""
    for letter in orignal_text:
        shifted_pos = alphabet.index(letter) + shift_amt
        cipher_string += alphabet[shifted_pos]
    return(cipher_string)
def decrypt(encrypt_text, shift_amt):
    decrypt_str = ""
    for letter in encrypt_text:
        shifted_pos = alphabet.index(letter) - shift_amt
        decrypt_str += alphabet[shifted_pos]
    return(decrypt_str)

while running:
    
    dir = input("type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    if dir == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        result = encrypt(text, shift)
        print(f"Here is your encoded message: {result}")
        encode_again = input("Would you like to run again? Y/N?\n").capitalize()
        if encode_again == "Y":
            running = True
        else:
            running = False      
    elif dir == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))        
        result = decrypt(text, shift)
        print(f"Here is your decoded message: {result}")
        encode_again = input("Would you like to run again? Y/N?\n").capitalize()
        if encode_again == "Y":
            running = True
        else:
            running = False
    else:
        print("Invaild Option")