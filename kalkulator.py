def input_lub_wyjdz(prompt):
    out = input(prompt)
    if out.lower() == "exit":
        print("Żegnam!")
        exit()

print("~ Kalkulator ~")
print("Aby wyjść, wpisz \"exit\".")
while True:
    print("---")
    liczby = []
    for i in range(2):
        while True:
            l = input_lub_wyjdz(f"Liczba {i + 1}: ")
            try:
                l = float(l)
                break
            except:
                print("To nie liczba!")
        liczby.append(l)
    while True:
        operacja = input_lub_wyjdz("Operacja (+-*/^): ")
        if operacja in "+-*/^":
            break
        else:
            print("Nieznana operacja!")
    if operacja == "+":
        wynik = liczby[0] + liczby[1]
    elif operacja == "-":
        wynik = liczby[0] - liczby[1]
    elif operacja == "*":
        wynik = liczby[0] * liczby[1]
    elif operacja == "/":
        wynik = liczby[0] / liczby[1]
    elif operacja == "^":
        wynik = liczby[0] ** liczby[1]
    print(f"Wynik: {wynik:g}")
