"""Szyfrowanie i deszyfrowanie pojedynczego bloku AES-128."""

AES_MODULUS = 0x11B
RCON = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)
MIX_COLUMNS_MATRIX = (
    (0x02, 0x03, 0x01, 0x01),
    (0x01, 0x02, 0x03, 0x01),
    (0x01, 0x01, 0x02, 0x03),
    (0x03, 0x01, 0x01, 0x02),
)


def poly_multiply(a, b):
    # Out: iloczyn wielomianów nad GF(2).
    pass


def poly_divmod(dividend, divisor):
    # Out: iloraz i reszta
    pass


def gf_multiply(a, b):
    # Out: iloczyn wielomianów w GF(2^8)
    pass

def gf_inverse(a):
    # Out: odwrotność w GF(2^8)
    pass


def sbox_byte(a):
    # Out: S-boxa AES(a)
    pass


def sub_bytes(data):
    # Out: ciąg wartości S-box
    pass


def rot_word(word):
    # Out: przesunięcie w lewo o 1 bajt
    pass


def expand_key(key):
    # Out: 11 kluczy po 16 bajtów, od K0 do K10
    pass


def shift_rows(state):
    # Out: przesunięcie wierszy
    pass


def mix_columns(state):
    # Out: stan po MixColumns
    pass


def round_states(block, round_keys, use_mix_columns=True):
    # Out: kolejne stany po początkowym XOR i po każdej z 10 rund
    pass


def encrypt_block(key, block):
    # Out: zaszyfrowany blok
    pass


def decrypt_block(key, block):
    # Out: odszyfrowany blok
    pass


def self_check():
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    block = bytes.fromhex("00112233445566778899aabbccddeeff")
    expected = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
    if encrypt_block(key, block) != expected:
        print("Stały przykład szyfrowania: BŁĄD")
        return
    print("Stały przykład szyfrowania: OK")
    if decrypt_block(key, expected) != block:
        print("Stały przykład deszyfrowania: BŁĄD")
        return
    print("Stały przykład deszyfrowania: OK")

    from secrets import token_bytes
    from Crypto.Cipher import AES

    zero = bytes(16)
    ones = b"\xff" * 16
    examples = [(zero, zero), (ones, ones)]
    for _ in range(100):
        examples.append((token_bytes(16), token_bytes(16)))

    for key, block in examples:
        reference = AES.new(key, AES.MODE_ECB)
        if encrypt_block(key, block) != reference.encrypt(block):
            print("Szyfrowanie niezgodne z PyCryptodome")
            print("Klucz", key.hex())
            print("Blok", block.hex())
            return
        if decrypt_block(key, block) != reference.decrypt(block):
            print("Deszyfrowanie niezgodne z PyCryptodome")
            print("Klucz", key.hex())
            print("Szyfrogram", block.hex())
            return
    print(f"Porównanie z PyCryptodome ({len(examples)} przykładów): OK")


if __name__ == "__main__":
    self_check()
