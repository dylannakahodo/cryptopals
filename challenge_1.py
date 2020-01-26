"""
Challenge 1: Convert Hex to Base64
"""

import binascii
from base64 import b64encode

def hex_to_b64(hex_string):
    hex_bytes = binascii.unhexlify(hex_string)
    return b64encode(hex_bytes)

if __name__ == "__main__":
    input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    
    # Converts bytes to base64 string
    output = hex_to_b64(input_string).decode()

    print(f"Output = {output}")
    print(f"Expected Output = {expected_output}")

    if output != expected_output:
        print("FAIL - Output does not match")
    else:
        print("PASS")