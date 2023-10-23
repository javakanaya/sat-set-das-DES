import table as t

def permute(source, table):
    result = ""
    for i in table:
        result += source[i - 1]
    return result

def left_shift_binary(binary_str, n):
    return binary_str[n:] + binary_str[:n]

def binary_xor(bin_str1, bin_str2):
    # Ensure both binary strings have the same length
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)

    result = ''
    for i in range(max_len):
        if bin_str1[i] == bin_str2[i]:
            result += '0'
        else:
            result += '1'

    return result

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0000"

    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2

    while len(binary_str) < 4:
        binary_str = '0' + binary_str

    return binary_str

def generateKeys(key):
    round_keys = []

    # 64 bits to 56 bits
    pc1_key =  permute(key, t.pc1)

    left = pc1_key[0:28]
    right  = pc1_key[28:56]

    for i in range(0, 16):
        left = left_shift_binary(left, t.shift_round[i])
        right = left_shift_binary(right, t.shift_round[i])

        # 56 bits to 48 bits
        round_key = permute(left + right, t.pc2)

        round_keys.append(round_key)

    return round_keys

def encrypt(plaintext, round_keys):
    # initial permutation
    ip_plaintext = permute(plaintext, t.initial_perm)
    
    left = ip_plaintext[0:32]
    right  = ip_plaintext[32:64]
    for i in range(0, 16):
        # right 32 bit to 48 bit
        right_expanded = permute(right, t.exp_perm)

        right_xored = binary_xor(right_expanded, round_keys[i])

        # back from right 48 bit to 32 bit
        right_sboxed = ""
        for j in range(0, 48, 6):
            chunk = right_xored[j:j + 6]
            row = int(chunk[0] + chunk[5], 2)
            col = int(chunk[1:5], 2)
            
            # Get the value from the S-Box
            right_sboxed += decimal_to_binary(t.sbox_perm[j//6][row][col])

        right_pboxed = permute(right_sboxed, t.pbox_perm)
        right_result = binary_xor(left, right_pboxed)


        left = right
        right = right_result

    cipher_text = permute((right + left), t.inverse_initial_perm)
    return cipher_text
        

def decrypt(ciphertext, round_keys):
    rev_round_keys = round_keys[::-1]
    return encrypt(ciphertext, rev_round_keys)

    