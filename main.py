import des 

def text_to_binary(text):
    binary_result = ""
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_result += binary_char

    # Ensure the binary string is a multiple of 64 bits
    while len(binary_result) % 64 != 0:
        binary_result += '0'

    return [binary_result[i:i+64] for i in range(0, len(binary_result), 64)]

def binary_to_text(binary_list):
    binary_str = ''.join(binary_list)
    text = ""
    for i in range(0, len(binary_str), 8):
        char_binary = binary_str[i:i+8]
        char = chr(int(char_binary, 2))
        text += char
    return text

def binary_to_hex(binary_str):
    hex_result = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]  # Extract 8 bits at a time
        decimal_value = int(byte, 2)
        hex_value = format(decimal_value, '02X')  # Ensure each hex digit has 2 digits
        hex_result += hex_value + ' '
    
    # Remove the trailing space
    hex_result = hex_result.rstrip()
    
    return hex_result

if __name__ == "__main__":
    while True:
        plaintext = input("Enter a 64-bit binary string: ")
        if len(plaintext) % 8 == 0:
            break
        else:
            print("Input is not a valid 64-bit binary string. Please try again.")

    bin_plaintext = text_to_binary(plaintext)

    while True:
        key = input("Enter a 64-bit DES key (in string format): ")
        if len(key) == 8:
            break
        else:
            print("The key should be exactly 64 bits in length (8 characters).")

    bin_key = text_to_binary(key)[0]
    print("DES Key (Binary):", bin_key)
    print("DES Key (Hex):", binary_to_hex(bin_key))
    round_keys = des.generateKeys(bin_key)

    chipertext = ""
    for chunk in bin_plaintext:
        result = des.encrypt(chunk, round_keys)
        chipertext += result

    c_ct = binary_to_text(chipertext)
    h_ct = binary_to_hex(chipertext)
    print("Converted Text:", c_ct)
    print("Converted Text (in hex):", h_ct)

    bin_chipertext = text_to_binary(c_ct)
    result_plaintext = ""
    for chunk in bin_chipertext:
        result = des.decrypt(chunk, round_keys)
        result_plaintext += result

    print("Back to original plain Text:", binary_to_text(result_plaintext))



