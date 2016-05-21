from getch import getch

variable = ""

keys = [52, 114, 102, 99, 32]
one = str(keys[0])
two = str(keys[1])
three = str(keys[2])
four = str(keys[3])
five = str(keys[4])

maps = {}

maps[one] = {}
maps[one][one] = "a"
maps[one][two] = "b"
maps[one][three] = "c"
maps[one][four] = "d"
maps[one][five] = "e"

maps[two] = {}
maps[two][one] = "f"
maps[two][three] = "g"
maps[two][three] = "h"
maps[two][four] = "i"
maps[two][five] = "j"

maps[three] = {}
maps[three][one] = "k"
maps[three][two] = "l"
maps[three][three] = "m"
maps[three][four] = "n"
maps[three][five] = "o"

maps[four] = {}
maps[four][one] = "p"
maps[four][two] = "q"
maps[four][three] = "r"
maps[four][five] = "s"

maps[five] = {}
maps[five][one] = "t"
maps[five][two] = "u"
maps[five][three] = "v"
maps[five][four] = "w"
maps[five][five] = {}
maps[five][five][one] = "x"
maps[five][five][two] = "y"
maps[five][five][three] = "z"
maps[five][five][four] = " "



while True:
    key = ord(getch())
    if str(key) in keys:
        key1 = ord(getch())
        if str(key1) in keys:
            print(maps[str(key)][str(key1)])
