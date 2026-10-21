import random
import string

def parol_doret(uzynlyk):
    # Harplary, sanlary we ýörite nyşanlary bir ýere jemleýäris
    nyşanlar = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
    # Taslamaly (random) usulda parol döredýäris
    parol = ''.join(random.choice(nyşanlar) for i in range(uzynlyk))
    return parol

print("=== HOWPSUZ PAROL DÖREDIJI ===")
print("Müşderiler üçin howpsuzlyk ilkinji orunda durýar!\n")

try:
    # Ulanyjydan paroluň uzynlygyny soraýarys
    ulanyjy_sayy = int(input("Paroluň uzynlygyny giriziň (meselem: 12): "))
    
    if ulanyjy_sayy < 6:
        print("Howpsuzlyk üçin azyndan 6 nyşan gerek!")
    else:
        netije = parol_doret(ulanyjy_sayy)
        print(f"\nSiziň döredilen paroluňyz: \n---> {netije} <---")
        print("\nBu paroly kopiýalap, öz hasabyňyzda ulanyp bilersiňiz.")
except ValueError:
    print("Ýalňyşlyk! Haýyş, diňe san giriziň.")
