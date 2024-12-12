print("Welcome to Caesar Cipher program\n")

def caesar_cipher(text,shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift_direction = shift if action == "e" else -shift
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result+= char
    return result

def main():
    action = input("Please select an option\n 'e for encryption\n 'd' for decryption :: ").lower()
    while action not in ["e", "d"]:
        print("Invalid Selection !!!!!\n Please select 'e' or 'd'.....")
        action = input("Please select an option\n 'e for encryption\n 'd' for decryption :: ").lower()
    message = input("Enter a message to encrypt/decrypt :: ")
    shift = int(input("Enter Shift Value :: "))

    result =  caesar_cipher(message, shift, action)
    action_word = "Encrypted" if action == 'e' else "Decrypted"
    print(f"\n{action_word} Message : {result}")


if __name__ == "__main__":
    main()
