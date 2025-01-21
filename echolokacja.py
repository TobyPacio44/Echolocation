import math
import tkinter as tk
from tkinter import messagebox

# Parametry
default_predkosc_dzwieku = 343  # m/s
default_czas_powrotu_echa = 0.05 
default_emitowana_czestotliwosc = 50000  # Hz
default_otrzymana_czestotliwosc = 51000  # Hz
default_predkosc_nietoperza = 0  # m/s

# Oblicza odległość od obiektu na podstawie czasu powrotu echa
def oblicz_pozycje(predkosc_dzwieku, czas_powrotu_echa):

    return predkosc_dzwieku * czas_powrotu_echa / 2

# Oblicza prędkość obiektu na podstawie efektu Dopplera.
def oblicz_predkosc_obiektu(predkosc_dzwieku, emitowana_czestotliwosc, otrzymana_czestotliwosc):
    
    return predkosc_dzwieku * ((otrzymana_czestotliwosc - emitowana_czestotliwosc) / emitowana_czestotliwosc)

# Oblicza prędkość względną obiektu względem nietoperza.
def oblicz_predkosc_wzgledem_nietoperza(predkosc_dzwieku, emitowana_czestotliwosc, otrzymana_czestotliwosc, predkosc_nietoperza):

    return predkosc_dzwieku - ((predkosc_dzwieku + predkosc_nietoperza) * emitowana_czestotliwosc / otrzymana_czestotliwosc)

# Funkcja do obsługi przycisku

def wykonaj_obliczenia():
    try:
        predkosc_dzwieku = float(entry_predkosc_dzwieku.get())
        czas_powrotu_echa = float(entry_czas_powrotu_echa.get())
        emitowana_czestotliwosc = float(entry_emitowana_czestotliwosc.get())
        otrzymana_czestotliwosc = float(entry_otrzymana_czestotliwosc.get())
        predkosc_nietoperza = float(entry_predkosc_nietoperza.get())

        odleglosc = oblicz_pozycje(predkosc_dzwieku, czas_powrotu_echa)
        predkosc_obiektu = oblicz_predkosc_obiektu(predkosc_dzwieku, emitowana_czestotliwosc, otrzymana_czestotliwosc)

        if predkosc_nietoperza > 0:
            predkosc_wzgledem = oblicz_predkosc_wzgledem_nietoperza(predkosc_dzwieku, emitowana_czestotliwosc, otrzymana_czestotliwosc, predkosc_nietoperza)
            messagebox.showinfo("Wyniki", f"Odległość od obiektu: {odleglosc:.2f} m\nPrędkość względna obiektu: {predkosc_wzgledem:.2f} m/s")
        else:
            messagebox.showinfo("Wyniki", f"Odległość od obiektu: {odleglosc:.2f} m\nPrędkość obiektu: {predkosc_obiektu:.2f} m/s")
    except ValueError:
        messagebox.showerror("Błąd", "Upewnij się, że wszystkie pola zawierają poprawne wartości numeryczne.")

# Tworzenie GUI
root = tk.Tk()
root.title("Echolokacja Nietoperza")

# Pola wejściowe i etykiety
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Prędkość dźwięku (m/s):").grid(row=0, column=0, sticky="w")
entry_predkosc_dzwieku = tk.Entry(frame)
entry_predkosc_dzwieku.grid(row=0, column=1)
entry_predkosc_dzwieku.insert(0, str(default_predkosc_dzwieku))

tk.Label(frame, text="Czas powrotu echa (s):").grid(row=1, column=0, sticky="w")
entry_czas_powrotu_echa = tk.Entry(frame)
entry_czas_powrotu_echa.grid(row=1, column=1)
entry_czas_powrotu_echa.insert(0, str(default_czas_powrotu_echa))

tk.Label(frame, text="Emitowana częstotliwość (Hz):").grid(row=2, column=0, sticky="w")
entry_emitowana_czestotliwosc = tk.Entry(frame)
entry_emitowana_czestotliwosc.grid(row=2, column=1)
entry_emitowana_czestotliwosc.insert(0, str(default_emitowana_czestotliwosc))

tk.Label(frame, text="Otrzymana częstotliwość (Hz):").grid(row=3, column=0, sticky="w")
entry_otrzymana_czestotliwosc = tk.Entry(frame)
entry_otrzymana_czestotliwosc.grid(row=3, column=1)
entry_otrzymana_czestotliwosc.insert(0, str(default_otrzymana_czestotliwosc))

tk.Label(frame, text="Prędkość nietoperza (m/s):").grid(row=4, column=0, sticky="w")
entry_predkosc_nietoperza = tk.Entry(frame)
entry_predkosc_nietoperza.grid(row=4, column=1)
entry_predkosc_nietoperza.insert(0, str(default_predkosc_nietoperza))

# Przycisk
button = tk.Button(root, text="Oblicz", command=wykonaj_obliczenia)
button.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()
