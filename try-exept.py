import datetime

import datetime
def write_logo(error):
    with open("logo.txt", "a") as file:
        file.write(f"{error} {datetime.datetime.now()}\n")
while True:
    try:
        a = int(input("A"))
        b = 100
        c = b / a
        print(f"Try C = {c}")
    except ValueError as va:
        write_logo(va)
        a, b = 1, 10
        c = b / a
        print("Введите число а не это!")
    except ZeroDivisionError as zd:
        write_logo(zd)
        print("на 0 делить?")
        break
    else:
        print("ELSE")
    finally:
        print("FINALLY")

