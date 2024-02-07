# Language dictionary for encoding
langdict = {'æ': 0, 'ä': 1, 'â': 2, 'å': 3, 'ă': 4, 'ạ': 5, 'ą': 6, 'a': 7,
            '€': 8, 'ę': 9, 'ê': 10, 'ĕ': 11, 'ė': 12, 'ë': 13, '¬': 14, 'e': 15}

# Decode from 4-bit codepage
def dccp(encoded_str):
    decoded_text = ""
    for i in range(0, len(encoded_str), 2):  # Process two hexadecimal digits at a time
        hex_value = encoded_str[i:i+2]
        int_value = int(hex_value, 16)  # Convert hex to int
        for key, value in langdict.items():  # Find matching value in langdict
            if value == int_value:
                decoded_text += key
                break
    return decoded_text

# Encode to 4-bit codepage
def encp(str_to_encode):
    encoded_text = ""
    for char in str_to_encode:
        if char in langdict:
            encoded_text += format(langdict[char], '02x')  # Convert to hex and format with leading zeros
    return encoded_text

# Example usage
if __name__ == '__main__':
    test_str = "a€"
    encoded = encp(test_str)
    print(f"Encoded: {encoded}")
    decoded = dccp(encoded)
    print(f"Decoded: {decoded}")
