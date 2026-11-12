## Zadanie 1

Uzupełnij implementację DES w pliku [des.py](des.py). Wszystkie tablice
permutacji, rozszerzenia, wyboru bitów, przesunięcia oraz S-boxy są już
wpisane w pliku [des_tables.py](des_tables.py). Nie zmieniaj tych tablic.

Uzupełnij pięć funkcji:

```python
def permute(value: int, table: tuple[int, ...], input_bits: int) -> int:
    ...

def rotate_left_28(value: int, shift: int) -> int:
    ...

def generate_subkeys(key: bytes) -> tuple[int, ...]:
    ...

def feistel(right: int, subkey: int) -> int:
    ...

def crypt_block(block: bytes, subkeys: tuple[int, ...]) -> bytes:
    ...
```

Gotowe funkcje `encrypt_block(key, block)` i `decrypt_block(key, block)`
korzystają z powyższych funkcji. Deszyfrowanie przetwarza podklucze
w odwrotnej kolejności. Klucz i blok mają po 8 bajtów. Wewnątrz algorytmu
operuj na liczbach całkowitych. Konwersje między `bytes` i `int` wykonuj
w porządku big-endian.

## Zadanie 2

W 2DES blok jest szyfrowany dwukrotnie, dwoma niezależnie wybieranymi
kluczami:

```text
C = E_K2(E_K1(P))
```

Złam przykład 2DES metodą brute force oraz metodą meet-in-the-middle.
W obu atakach wykorzystaj pełny DES z zadania 1: wszystkie 16 rund,
oryginalne S-boxy i permutacje.

Ograniczamy jedynie przestrzeń kluczy. Każdy z dwóch kluczy ma `2^b`
możliwości. Gotowa funkcja `key_from_index(index, bits)` w pliku
[des2.py](des2.py) zamienia indeks od `0` do `2^b - 1` na klucz DES.
Zmiennych jest `b` bitów spośród 56 bitów efektywnego klucza; pozostałe
bity mają stałe, znane wartości. Funkcja dodaje też bity parzystości.
Różne indeksy oznaczają różne efektywne klucze. Do tworzenia kandydatów
używaj tej funkcji w obu atakach.

W pliku [dane_02.py](dane_02.py) znajdują się:

- `BITS = 9`: po 512 możliwych kluczy dla `K1` i `K2`,
- `PAIRS`: dwie znane pary tekst jawny–szyfrogram jako lista par obiektów
  `bytes`, zaszyfrowane tą samą parą kluczy,
- `MESSAGE`: dodatkowa zaszyfrowana wiadomość ASCII jako `bytes`.

Zaimportuj dane i funkcje pomocnicze:

```python
from dane_02 import BITS, PAIRS, MESSAGE
from des2 import key_from_index, check_keys, decrypt_message
```

**Część A: brute force**

Napisz funkcję `brute_force(bits, pairs)`, która sprawdza pary indeksów
w następującej kolejności:

```text
(0, 0), (0, 1), ..., (0, 511),
(1, 0), (1, 1), ..., (1, 511),
...
(511, 0), ..., (511, 511).
```

**Część B: meet-in-the-middle**

Napisz funkcję `meet_in_the_middle(bits, pairs)`. Wykorzystaj zależność:

```text
E_K1(P1) = D_K2(C1)
```

**Sprawdzenie i porównanie**

Po każdym ataku zamień znalezione indeksy na klucze i sprawdź:

```python
key1 = key_from_index(index1, BITS)
key2 = key_from_index(index2, BITS)
assert check_keys(key1, key2, PAIRS)

message = decrypt_message(key1, key2, MESSAGE)
print(message.rstrip(b" ").decode("ascii"))
```

Oba ataki rozpoznają sukces automatycznie przez dokładne porównanie
bloków. Odczyt dodatkowej wiadomości jest końcowym efektem ataku.
Jej bloki zaszyfrowano niezależnie tymi samymi kluczami 2DES, a przed
szyfrowaniem dodano na końcu spacje do wielokrotności 8 bajtów.

Dla obu metod wypisz:

- znalezione indeksy i klucze,
- czas ataku zmierzony przez `time.perf_counter()`,
- liczbę operacji szyfrowania i deszyfrowania pojedynczego bloku DES,
- liczbę sprawdzonych par kluczy,
- liczbę indeksów zapisanych w tablicy wartości pośrednich.

## Zadanie 3

Zbadaj działanie DES dla klucza zapisanego szesnastkowo jako:

```text
0101010101010101
```

Korzystając z implementacji z zadania 1:

1. Wygeneruj i wypisz wszystkie 16 podkluczy rundowych jako liczby
   szesnastkowe o długości 12 cyfr. Ile różnych podkluczy otrzymujesz?
2. Dla bloku zerowego, bloku złożonego z samych jedynek oraz co najmniej
   100 losowych bloków sprawdź, co daje **dwukrotne szyfrowanie** tym
   samym kluczem: `encrypt_block(key, encrypt_block(key, block))`.
   Wypisz, w ilu przypadkach wynik jest równy blokowi wejściowemu.
3. Wyjaśnij wyniki, odwołując się do działania `PC1`, rotacji połówek
   klucza i kolejności podkluczy przy deszyfrowaniu. Czy obserwowana
   własność zachodzi dla każdego bloku? Uzasadnij odpowiedź na podstawie
   algorytmu, a nie tylko przeprowadzonych prób.
4. Jaki szyfrogram da 2DES, jeśli `K1` i `K2` będą równe podanemu
   kluczowi? Czy sam fakt dwukrotnego szyfrowania gwarantuje wzmocnienie
   ochrony?

## Materiały

- Specyfikacja DES: [FIPS 46-3](https://csrc.nist.gov/files/pubs/fips/46-3/final/docs/fips46-3.pdf).
- Dokumentacja PyCryptodome: [https://www.pycryptodome.org/src/cipher/des](https://www.pycryptodome.org/src/cipher/des).
