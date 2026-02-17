def encode_short_code(num):
    """Convert a number to base62"""
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return base62[0]
    encoded = ""
    while num > 0:
        encoded = base62[num % 62] + encoded
        num //= 62
    return encoded


def decode_short_code(code):
    """Convert a base62 short code back to a number (ID)"""
    base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = 0
    for char in code:
        num = num * 62 + base62.index(char)
    return num