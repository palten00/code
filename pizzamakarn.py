print("***** hej och välkommen till pizzamakarn *****")
print("1. skriv in ditt val av topping")
print("2. skriv ut ditt val av topping")
print("3. avsluta och beställ pizzan.")
topping =""
meny = 0
while meny != 3:
    print("1. skriv in ditt val av topping")
    print("2. skriv ut ditt val av topping")
    print("3. avsluta och beställ pizzan.")
    try:
        meny = int(input("gör ett val från menyn "))
    except:
        print("du måste ange en siffra ")

    if meny == 1:
        topping += input("skriv in den topping du önskar ") + ", "
    elif meny == 2:
        print("din valda topping är: ", topping)
    elif meny == 3: 
        print("tack och hej")
    else:
        print("du hade inte gjort ett korrekt val, prova igen")