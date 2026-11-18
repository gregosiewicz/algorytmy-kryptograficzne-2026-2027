## Zadanie 1. Implementacja AES-128

Uzupełnij funkcje oznaczone `pass` w pliku [aes.py](aes.py). Klucz, blok
i stan to obiekty `bytes` o długości 16.

## Zadanie 2. Dokąd dotrze jeden bit?

Sprawdzimy, jak zmiana jednego bitu bloku rozchodzi się po stanie AES.
We wszystkich próbach używaj tego samego klucza i bloku, a klucze rundowe
wyznacz tylko raz:

```python
from aes import expand_key, round_states

key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
block = bytes.fromhex("00112233445566778899aabbccddeeff")
round_keys = expand_key(key)
```

Funkcja `round_states` zwraca 11 stanów: stan `0` to wynik początkowego
XOR-u z `K0`, a stany `1`--`10` to wyniki kolejnych rund. Każdą próbę
wykonaj w dwóch wariantach:

- z MixColumns: `round_states(block, round_keys)`,
- bez MixColumns: `round_states(block, round_keys, use_mix_columns=False)`.

1. Odwróć najmłodszy bit pierwszego bajtu bloku. W obu wariantach porównaj
   stany obu bloków po XOR-ze z `K0` oraz po rundach 1 i 2. Wynik pokaż na
   planszach 4 × 4: `#` oznacza bajt zmieniony, `.` bajt bez zmian. Bajt
   w wierszu `r` i kolumnie `c` ma w stanie indeks `4*c + r` (numeracja
   od zera). Na przykład zmiana tylko bajtu o indeksie `0` wygląda tak:

   ```text
   # . . .
   . . . .
   . . . .
   . . . .
   ```

2. Wykonaj 128 prób: w każdej odwróć inny pojedynczy bit oryginalnego
   bloku. Dla każdego z 11 stanów i obu wariantów podaj średnią liczbę
   różniących się **bitów** (w tabeli lub na wykresie). Liczbę różnych
   bitów w bajtach `a` i `b` daje `(a ^ b).bit_count()`.
3. Która operacja przenosi różnicę do innej kolumny? Która rozszerza ją
   na więcej bajtów?

## Zadanie 3. Co widać po zaszyfrowaniu obrazu?

Obraz [mozaika.png](dane/mozaika.png) ma 256 × 128 pikseli w skali
szarości, po jednym bajcie na piksel. Piksele odczytasz biblioteką Pillow
(`python3 -m pip install Pillow`):

```python
from PIL import Image

obraz = Image.open("dane/mozaika.png")
piksele = obraz.tobytes()
```

Podziel piksele na 16-bajtowe bloki `P[1], P[2], ...` i zaszyfruj je
w trybach ECB i CBC funkcją `encrypt_block(key, block)` z kluczem
z zadania 2. Przez `E_K` oznaczamy szyfrowanie jednego bloku:

```text
ECB   C[i] = E_K(P[i])
CBC   C[i] = E_K(P[i] XOR C[i-1]),   C[0] = IV
```

W CBC przyjmij `IV = 101112131415161718191a1b1c1d1e1f`. Dla każdego trybu
sklej bloki `C[1], C[2], ...` w jeden ciąg bajtów i zapisz go jako obraz:

```python
Image.frombytes("L", obraz.size, piksele_ecb).save("ecb.png")
Image.frombytes("L", obraz.size, piksele_cbc).save("cbc.png")
```

1. Pokaż oryginał i oba szyfrogramy. Ile różnych bloków ma każdy z trzech
   obrazów? Co z pierwotnego wzoru widać po szyfrowaniu? Wyjaśnij to tym,
   jak ECB i CBC szyfrują równe bloki.
2. Odwróć najmłodszy bit pierwszego piksela w wierszu `64` (wiersze
   liczymy od zera). Przewidź, które bloki szyfrogramu się zmienią,
   a potem sprawdź to w obu trybach przy tym samym kluczu i IV.

## Materiały

- Specyfikacja AES: [FIPS 197 (2023)](https://csrc.nist.gov/pubs/fips/197/final).
