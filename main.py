print("Podaj kwotę początkową pożyczki: ")
kwota_pozyczki = int(input())
print("Podaj oprocentowanie: ")
oprocentowanie = int(input())
print("Podaj kwotę jednej raty: ")
rata = int(input())
stopa = float(1.592824484)
pozostala_kwota = (1 + (( stopa + oprocentowanie ) / 1200 )) * kwota_pozyczki - rata
print("Twoja pozostała kwota kredytu to {}.".format(pozostala_kwota))
