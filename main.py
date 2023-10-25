import des 

if __name__ == "__main__":
    while True:
        plaintext = input("Enter a 64-bit binary string (in ASCII format): ")
        if len(plaintext) % 8 == 0:
            break
        else:
            print("Input is not a valid 64-bit binary string. Please try again.")

    bin_plaintext = des.text_to_binary(plaintext)

    while True:
        key = input("Enter a 64-bit DES key (in ASCII format): ")
        if len(key) == 8:
            break
        else:
            print("The key should be exactly 64 bits in length (8 characters).")

    bin_key = des.text_to_binary(key)[0]
    # print("DES Key (Binary):", bin_key)
    print("DES Key (Hex):", des.binary_to_hex(bin_key))
    round_keys = des.generateKeys(bin_key)


    print("Encrypting")
    chipertext = ""
    for chunk in bin_plaintext:
        result = des.encrypt(chunk, round_keys)
        chipertext += result

    c_ct = des.binary_to_text(chipertext)
    h_ct = des.binary_to_hex(chipertext)
    print("Converted Text:", c_ct)
    print("Converted Text (in hex):", h_ct)

    bin_chipertext = des.text_to_binary(c_ct)
    print("Decrypting")
    result_plaintext = ""
    for chunk in bin_chipertext:
        result = des.decrypt(chunk, round_keys)
        result_plaintext += result

    # print(des.binary_to_text(des.decrypt('1000101111011011001000001100010101011000010010111010101111100101', round_keys)))

    print("Back to original plain Text:", des.binary_to_text(result_plaintext))



