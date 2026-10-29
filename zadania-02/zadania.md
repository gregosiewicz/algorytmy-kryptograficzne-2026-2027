## Zadanie 1

Tego samego klucza `k` użyto do zaszyfrowania ośmiu wiadomości szyfrem
jednorazowym (OTP). Odszyfruj wszystkie wiadomości.

*Wskazówka*: Wszystkie teksty jawne zawierają wyłącznie małe litery i
spacje. Zastanów się, co dzieje się z literami w kodzie ASCII, gdy
xorujemy je ze spacją. Wykorzystaj też fakt, że w tekstach angielskich
często pojawia się słowo `the`.

Szyfrogramy wiadomości w formacie szesnastkowym:
```
01:
fa313f179908743aeda9361b304d9aba31eaeb498908373869a362b303ba10b9
96a999ab61c4124f1efad632612f0d0f77dbd5729746

02:
f93c7a5b9e016168fde1324b2b5a8cbf74e1a51d9505727667bd36a00aad15b9
92a49aa92485155d0fed84667d22484762dbd56f80

03:
fa313f1789026527fbfd77042e1f81a431aeb85c8708632f2cbb24e316a01eb9
84b791a126c054491ee9952e6c2e0d137adf877698586aa5

04:
fe353f568802352afbe0390c604b9da974eaa45e9400723878a762b70de80ff1
83e597a327cc175e5bea93206638484766d2c23b944460a397632101dd078eeb

05:
fa313f179808742be1a9250e365690bb31eaeb49890837316db927e303a61fb9
92ad9dab61d11c5e5bfc9327646a5a0666d9cf7e9d0171bf9b2d3048cd0a84

06:
fa313f1788137a3ae4a9341e341f81a431aea754860563252cb536e316a01eb9
92ad9da435c0061b1ae692667d22484762d6c662d9446bb39b69

07:
ae2d3252db047d2defa9240e324990a874faa358c11e78237cf435ab0ba41eb9
92ad9de523c41a5f5bf89a27702f494773c8c86e974525a396686651c81d80

08:
ef3f2e5289477624e8fa244b345790ec27fabe59840363252ca437b742bc13fc
c6a797aa2ad6545215a8822e6c6a4106709ac97e985325a396686646c81b8e
```

## Zadanie 2

Polecenie przelewu jest zapisywane w kodzie ASCII w uproszczonym formacie:
```
odbiorca=ddddddd;kwota=dddddddd
```
Pole `odbiorca` zawiera siedmiocyfrowy numer konta. Pole `kwota` zawiera
kwotę zapisaną za pomocą dokładnie ośmiu cyfr, z zerami wiodącymi.
Każde `d` oznacza jedną cyfrę. Przykładowo kwota `1234` jest zapisywana
jako `00001234`.

Program `bank` symuluje przechwycenie i wykonanie zlecenia przelewu.
Przy każdym uruchomieniu losuje czterocyfrową kwotę oraz świeży klucz
szyfru jednorazowego (OTP). Następnie szyfruje zlecenie i wypisuje
przechwycony szyfrogram w formacie szesnastkowym. Wiadomo, że przelew
jest skierowany na konto `4328625`. Dokładna kwota oraz klucz są nieznane.

Napisz program, który zmodyfikuje otrzymany szyfrogram tak, aby po
odszyfrowaniu:

- przelew był skierowany na Twoje konto o numerze `5128765`,
- kwota miała postać `0009xxxx`, gdzie `xxxx` to cztery cyfry pierwotnej
  kwoty, np. kwota `1234` zmieniłaby się w `91234`, zapisaną jako
  `00091234`.

Pozostałe znaki wiadomości mają pozostać bez zmian. Wypisz zmodyfikowany
szyfrogram w formacie szesnastkowym i przekaż go do nadal uruchomionego
programu `bank`.

Wersje programu dla systemów Linux i Windows (x86-64) oraz macOS
(Intel i Apple Silicon) znajdują się w katalogu `bank`.

Uruchom program bez argumentów:

Linux:
```sh
./bank/bank-linux-x86_64
```

Windows (PowerShell):
```powershell
.\bank\bank-windows-x86_64.exe
```

macOS (Intel i Apple Silicon):
```sh
./bank/bank-macos-universal
```

Skopiuj wyświetlony szyfrogram do swojego programu, a wynik jego działania
wklej do oczekującego programu `bank`.

Każde uruchomienie przyjmuje tylko jeden szyfrogram do wykonania.
Po jego odszyfrowaniu program wykonuje przelew, jeśli wiadomość ma
poprawny format, i pokazuje, czy cel zadania został osiągnięty.
Dopiero wtedy ujawnia kwotę pierwotnego zlecenia. Następnie kończy sesję.
Ponowne uruchomienie generuje nową kwotę i nowy klucz.

## Zadanie 3

System powiadomień co kilka sekund rozsyła ten sam komunikat,
zaszyfrowany szyfrem jednorazowym (OTP). Do każdego zaszyfrowania losuje
nowy, niezależny klucz o długości wiadomości.

Generator kluczy ma jednak wadę: każdy bit klucza przyjmuje wartość `1`
z prawdopodobieństwem `0.55`, a wartość `0` z prawdopodobieństwem `0.45`.
Wszystkie losowania bitów, również pomiędzy różnymi kluczami, są
niezależne.

W pliku [dane/03.txt](dane/03.txt) znajduje się 3001 przechwyconych
szyfrogramów tego samego komunikatu. Każdy wiersz zawiera jeden szyfrogram
zapisany szesnastkowo. Wiadomość jest tekstem w kodzie ASCII.

1. Odtwórz treść komunikatu bez znajomości któregokolwiek z kluczy.
2. Powtórz atak, korzystając tylko z pierwszych 25, 100 i 500 szyfrogramów.
