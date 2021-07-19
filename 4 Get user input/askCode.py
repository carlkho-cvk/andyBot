from hentai import Hentai, Format, Option

# ask for H-code
code = input("Code?")

# convert code to integer, since str/s won't work
convertToInt = int(code)

# request h
doujin = Hentai(code)

# verify if true
print("Requested is: " + doujin.title(Format.Pretty))