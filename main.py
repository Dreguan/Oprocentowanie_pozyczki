print("Podaj kwotę początkową pożyczki: ")
kwota_pozyczki = int(input())
print("Podaj oprocentowanie: ")
oprocentowanie = int(input())
print("Podaj kwotę jednej raty: ")
rata = int(input())
stopa = float(1.592824484)
pozostala_kwota = (1 + (( stopa + oprocentowanie ) / 1200 )) * kwota_pozyczki - rata

ile_mniej = kwota_pozyczki - pozostala_kwota

print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(pozostala_kwota, ile_mniej))


