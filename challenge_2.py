"""
Challenge 2: Fixed XOR
"""
import binascii
import sys

def fixed_xor(a, b):
    a_bytes = binascii.unhexlify(a)
    b_bytes = binascii.unhexlify(b)

    if len(a_bytes) != len(b_bytes):
        print("Error: Buffer length mismatch.")
        sys.exit(1)

    return bytes([x ^ y for x,y in zip(a_bytes,b_bytes)])
    


if __name__ == "__main__":

    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"

    expected = "746865206b696420646f6e277420706c6179"
    # Converts output to hex string
    output = fixed_xor(a,b).hex()

    print(f"{output = }")
    print(f"{expected = }")

    if output != expected:
        print("FAIL - Does not match expected output!")
    else:
        print("PASS")