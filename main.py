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

if __name__ == "__main__":
    input_text = input("Enter a string: ")

    binary_chunks = text_to_binary(input_text)
    print("Binary Chunks:")
    for chunk in binary_chunks:
        print(chunk)

    while True:
        key_input = input("Enter a 64-bit DES key (in string format): ")
        if len(key_input) == 8:
            key_binary = text_to_binary(key_input)[0]
            print("DES Key (Binary):", key_binary)
            break
        else:
            print("The key should be exactly 64 bits in length (8 characters).")

    output_text = binary_to_text(binary_chunks)
    print("Converted Text:", output_text)


