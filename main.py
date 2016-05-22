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
maps[one][four] = {}
maps[one][four][one] = "d"
maps[one][four][two] = "`"
maps[one][four][three] = "~"
maps[one][four][four] = "1"
maps[one][four][five] = "2"
maps[one][five] = {}
maps[one][five][one] = "e"
maps[one][five][two] = ")"
maps[one][five][three] = "-"
maps[one][five][four] = "+"
maps[one][five][five] = "="

maps[two] = {}
maps[two][one] = "f"
maps[two][two] = "g"
maps[two][three] = "h"
maps[two][four] = {}
maps[two][four][one] = "i"
maps[two][four][two] = "3"
maps[two][four][three] = "4"
maps[two][four][four] = "5"
maps[two][four][five] = "6"
maps[two][five] = {}
maps[two][five][one] = "j"
maps[two][five][two] = "^"
maps[two][five][three] = "&"
maps[two][five][four] = "*"
maps[two][five][five] = "("

maps[three] = {}
maps[three][one] = "k"
maps[three][two] = "l"
maps[three][three] = "m"
maps[three][four] = {}
maps[three][four][one] = "n"
maps[three][four][two] = "7"
maps[three][four][three] = "8"
maps[three][four][four] = "9"
maps[three][four][five] = "0"
maps[three][five] = {}
maps[three][five][one] = "o"
maps[three][five][two] = "!"
maps[three][five][three] = "@"
maps[three][five][four] = "#"
maps[three][five][five] = "$"

maps[four] = {}
maps[four][one] = "p"
maps[four][two] = "q"
maps[four][three] = "r"
maps[four][four] = {}
maps[four][four][one] = "_"
maps[four][four][two] = "{"
maps[four][four][three] = "}"
maps[four][four][four] = "["
maps[four][four][five] = "]"
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
maps[five][four] = {}
maps[five][four][one] = "w"
maps[five][four][two] = "|"
maps[five][four][three] = "\\"
maps[five][four][four] = ":"
maps[five][four][five] = "\""
maps[five][five] = {}
maps[five][five][one] = "x"
maps[five][five][two] = "y"
maps[five][five][three] = "z"
maps[five][five][four] = " "
maps[five][five][five] = "?"


thestring = ""


while True:
    key = ord(getch())
    key1 = ord(getch())
    if (str(key1) == five) or (str(key1) == four):
        key2 = ord(getch())
        thestring = (maps[str(key)][str(key1)][str(key2)])
        sys.stdout.write(thestring)
    else:
        thestring = (maps[str(key)][str(key1)])
        sys.stdout.write(thestring)
