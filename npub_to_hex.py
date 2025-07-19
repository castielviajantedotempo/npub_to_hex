import sys
import bech32
from base64 import b32decode
from base64 import b16encode


def hex_to_bech32(key_str: str, prefix='npub'):
    as_int = [int(key_str[i:i+2], 16) for i in range(0, len(key_str), 2)]
    data = bech32.convertbits(as_int, 8, 5)
    return bech32.bech32_encode(prefix, data)

def add_padding(base32_len):
    bits = base32_len * 5
    padding_size = (8 - (bits % 8)) % 8
    return padding_size

def bech32_to_hex(npub_key):
    """
    Converts a Nostr npub key to its hexadecimal representation.
    """
    try:
        B32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
        hrp, data = bech32.bech32_decode(npub_key)
        b32_data = [B32[index] for index in data]
        data_str = "".join(b32_data)
        data_length = len(data_str)
        data_str += "=" * add_padding(data_length)
        decoded_data = b32decode(data_str)  # this is bech32.b32decode
        b16_encoded_data = b16encode(decoded_data)
        hex_str = b16_encoded_data.decode("utf-8").lower()
        return hex_str 
    except Exception as e:
        return f"Error converting npub to hex: {e}"
    
def main():
    print("Usage npub_to_hex.py <npub...>")
    if len(sys.argv) > 1:
        arg_str = sys.argv[1]
        if 'npub' in arg_str or 'nsec' in arg_str:
            print(bech32_to_hex(arg_str))
        else:
            print(hex_to_bech32(arg_str))

if __name__ =='__main__':
    main()
