def összeadás(x, y):
    return x + y


def kivonás(x, y):
    return x - y


def szorzás(x,y):
    return x * y


def osztás(x,y):
    if y == 0:
        return "Nullával való osztás nem megengedett!"
    return x / y

while True:
    print("Válassz műveletet:")
    print("1. Összeadás")
    print("2. Kivonás")
    print("3. Szorzás")
    print("4. Osztás")
    print("5. Kilépés")

    választás = input("Válassz egy opciót (1/2/3/4/5):")

    if választás == '5':
        print("Érvénytelen választás")
        continue

    szám1 = float(input("Add meg az első számot: "))
    szám2 = float(input("Add meg a második számot: "))

    if választás == '1':
        print("Eredmény: ", összeadás(szám1, szám2))

    elif választás == '2':
        print("Eredmény: ", kivonás(szám1, szám2))

    elif választás == '3':
        print("Eredmény: ", szorzás(szám1, szám2))

    elif választás == '4':
        print("Eredmény: ", osztás(szám1, szám2))

