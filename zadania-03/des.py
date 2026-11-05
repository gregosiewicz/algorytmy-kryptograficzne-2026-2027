from des_tables import IP, IP_INV, E, P, PC1, PC2, SHIFTS, S_BOXES


def permute(value: int, table: tuple[int, ...], input_bits: int) -> int:
    """Wybiera bity według tablicy; pozycje numerowane od 1, od MSB."""
    raise NotImplementedError("Uzupełnij permute")


def rotate_left_28(value: int, shift: int) -> int:
    """Rotacja w lewo w obrębie 28 bitów."""
    raise NotImplementedError("Uzupełnij rotate_left_28")


def generate_subkeys(key: bytes) -> tuple[int, ...]:
    """Zwraca 16 podkluczy, każdy jako 48-bitową liczbę całkowitą."""
    if len(key) != 8:
        raise ValueError("Klucz DES musi mieć 8 bajtów")
    raise NotImplementedError("Uzupełnij generate_subkeys")


def feistel(right: int, subkey: int) -> int:
    """Funkcja rundy: 32-bitowe right i 48-bitowy subkey -> 32 bity."""
    raise NotImplementedError("Uzupełnij feistel")


def crypt_block(block: bytes, subkeys: tuple[int, ...]) -> bytes:
    """Przetwarza blok według podanej kolejności 16 podkluczy."""
    if len(block) != 8:
        raise ValueError("Blok DES musi mieć 8 bajtów")
    if len(subkeys) != 16:
        raise ValueError("DES wymaga 16 podkluczy")
    raise NotImplementedError("Uzupełnij crypt_block")


def encrypt_block(key: bytes, block: bytes) -> bytes:
    return crypt_block(block, generate_subkeys(key))


def decrypt_block(key: bytes, block: bytes) -> bytes:
    return crypt_block(block, generate_subkeys(key)[::-1])


def self_check() -> None:
    """Porównuje wyniki z PyCryptodome."""
    from secrets import token_bytes
    from Crypto.Cipher import DES

    key = bytes.fromhex("133457799BBCDFF1")
    plaintext = bytes.fromhex("0123456789ABCDEF")
    expected = bytes.fromhex("85E813540F0AB405")
    assert encrypt_block(key, plaintext) == expected
    assert decrypt_block(key, expected) == plaintext
    print("Stały przykład: OK")

    examples = [(bytes(8), bytes(8)), (b"\xff" * 8, b"\xff" * 8)]
    examples += [(token_bytes(8), token_bytes(8)) for _ in range(100)]
    for key, plaintext in examples:
        reference = DES.new(key, DES.MODE_ECB)
        ciphertext = encrypt_block(key, plaintext)
        assert ciphertext == reference.encrypt(plaintext), "Błąd szyfrowania"
        assert decrypt_block(key, ciphertext) == plaintext, "Błąd deszyfrowania"
        arbitrary_ciphertext = token_bytes(8)
        assert decrypt_block(key, arbitrary_ciphertext) == reference.decrypt(
            arbitrary_ciphertext
        ), "Deszyfrowanie niezgodne z PyCryptodome"
    print(f"Porównanie z PyCryptodome ({len(examples)} przykładów): OK")


if __name__ == "__main__":
    self_check()
