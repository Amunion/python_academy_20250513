# soubor muj_modul.py
def hlavni_funkce():
    funkce_1()
    funkce_2()
    funkce_3()

def funkce_1():
    print("Spouštění první funkce...")

def funkce_2():
    """Funkce, kterou potřebuješ."""
    print("Spouštění druhé funkce...")

def funkce_3():
    print("Spouštění třetí funkce...")

if __name__ == "__main__":
    print("Nahrávání celého modulu...")
    hlavni_funkce()
else:
    print(__name__)
