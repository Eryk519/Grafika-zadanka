from PIL import Image
import numpy as np


print("Zadanie 1")
obraz= Image.open("inicjaly.bmp")
obraz.show()
print("tryb", obraz.mode)
print("format", obraz.format)
print("rozmiar", obraz.size)

t_obraz = np.asarray(obraz)
print("typ danych tablicy", t_obraz.dtype)
print("rozmiar tablicy", t_obraz.shape)
print("***************************************")


def wstaw_obraz(t_obraz,wsp,h_m,w_m):
    h0, w0 = t_obraz.shape
    print(h0, w0)
    t = (int(wsp * h0), int(wsp * w0))
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(int(h_m), int(h_m) + h0):
        for j in range(int(w_m), int(w_m) + w0):
            tab[i][j] = t_obraz[i - int(h_m)][j - int(w_m)]
    tab = tab.astype(bool)
    obraz_wstawiany = Image.fromarray(tab)
    return obraz_wstawiany

obraz_wstawiany = wstaw_obraz(t_obraz,2,60,70)
obraz_wstawiany.show()


