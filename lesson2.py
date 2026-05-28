try:
    number = int(input("Son kiriting: "))
    print(f"Siz kiritgan son: {number}")
except ValueError:
    print("Xato! Bu son emas!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
finally:
    print("Har doim ishlaydi")