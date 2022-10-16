from PIL import Image  # Python Imaging Library
import numpy as np

print("Zad 2")
obrazek = Image.open("inicjaly.bmp")
obrazek.show()
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

print("Zad 3 - zapisanie do pliku tekstowego")
obrazek_dane = np.asarray(obrazek)
dane_int = obrazek_dane * 1
t2_text = open('inicjaly.txt', 'w')
for rows in dane_int:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')

t2_text.close()

print("Zad 4")
dane_obrazka = np.asarray(obrazek)
print("Informacje o tablicy obrazka:")
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)
print("pierwszy wyraz:", dane_obrazka[30][50])
print("drugi wyraz:", dane_obrazka[40][90])
print("trzeci wyraz:", dane_obrazka[0][99])
print("***************************************")
print(dane_obrazka)

t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
t2 = np.loadtxt("inicjaly.txt", dtype=np.int_)

print("Zad 5")
print("typ danych tablicy t1:", t1.dtype)
print("rozmiar tablicy t1 :", t1.shape)
print("wymiar tablicy t1 :", t1.ndim)

print("typ danych tablicy t2:", t2.dtype)
print("rozmiar tablicy t2 :", t2.shape)
print("wymiar tablicy t2 :", t2.ndim)

print("Zad 6")
nowa_t2 = np.loadtxt("inicjaly.txt", dtype=np.int_)
print("--- nowa_t2 -----------")
print(nowa_t2)
print("----- t2 ---------")
print(t2)
porownanie2 = t2 == nowa_t2
print("Porownanie tablicy")
print(porownanie2)

print("Zad 6 dalej")
ob_i1 = Image.fromarray(t2)
print("tryb:", ob_i1.mode)
print("format:", ob_i1.format)
print("rozmiar:", ob_i1.size)
ob_i1.show()