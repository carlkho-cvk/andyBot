from hentai import Hentai, Format, Option


# make a request to nhentai.net
chosenDoujin = Hentai(177013)

# True
Hentai.exists(chosenDoujin.id)

# ['https://i.nhentai.net/galleries/987560/1.jpg', ... ]
print(chosenDoujin.image_urls)

for option in Option.all():
    print(option.name)