#3.2CaesarCode.py
plaincode = "python is an excellent language"
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end='')
    else:
        print(p, end='')
