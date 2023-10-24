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

binary_str = input("Enter a binary string: ")
hex_result = binary_to_hex(binary_str)
print("Hexadecimal: ", hex_result)
