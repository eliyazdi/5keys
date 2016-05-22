from getch import getch
import sys

variable = ""
keys = []

if sys.argv[1] == "machine":
    keys = [52, 114, 102, 99, 32]
elif sys.argv[1] == "human":
    keys = [106, 107, 108, 59, 32]
else:
    keys = [106, 107, 108, 59, 32]

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
maps[two][two] = "g"
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
maps[four][five] = {}
maps[four][five][one] = "s"
maps[four][five][two] = "."
maps[four][five][three] = ","
maps[four][five][four] = "/"
maps[four][five][five] = ";"

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


thestring = ""


while True:
    key = ord(getch())
    key1 = ord(getch())
    if ((str(key) == five) and (str(key1) == five)) or ((str(key) == four) and (str(key1) == four)):
        key2 = ord(getch())
        thestring+=(maps[str(key)][str(key1)][str(key2)])
        print(thestring)
    else:
        thestring+=(maps[str(key)][str(key1)])
        print(thestring)
