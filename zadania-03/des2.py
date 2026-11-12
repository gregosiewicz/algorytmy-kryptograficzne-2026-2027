from des import encrypt_block, decrypt_block


def key_from_index(index, bits):
    """Zastępuje bits najmłodszych bitów wzorca wartością index."""
    base = 0x123456789ABCDE
    key = (base & ~((1 << bits) - 1)) | index

    # Każde 7 bitów uzupełniamy bitem nieparzystej parzystości.
    result = bytearray()
    for shift in range(49, -1, -7):
        seven_bits = (key >> shift) & 0x7F
        parity = 1 - seven_bits.bit_count() % 2
        result.append((seven_bits << 1) | parity)
    return bytes(result)


def double_encrypt(key1, key2, block):
    return encrypt_block(key2, encrypt_block(key1, block))


def double_decrypt(key1, key2, block):
    return decrypt_block(key1, decrypt_block(key2, block))


def check_keys(key1, key2, pairs):
    for plaintext, ciphertext in pairs:
        if double_encrypt(key1, key2, plaintext) != ciphertext:
            return False
    return True


def decrypt_message(key1, key2, ciphertext):
    plaintext = b""
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i + 8]
        plaintext += double_decrypt(key1, key2, block)
    return plaintext
