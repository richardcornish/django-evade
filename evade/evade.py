import random
from html.entities import html5

HTML5_CHARS = {html5[key]: key for key in html5}

ENTITIES = {
    "d": "#",  # decimal
    "x": "#x",  # hexadecimal lowercase
    "X": "#x",  # hexadecimal uppercase
}


def evade(value):
    s = ""
    for char in value:

        # Named entities require simpler syntax
        if char in HTML5_CHARS and random.randint(0, 1):
            name = HTML5_CHARS[char]
            s += "&{}".format(name)
        else:
            cp = ord(char)
            choice = random.choice(list(ENTITIES.items()))
            form = choice[1]
            fill = "0"
            width = random.randint(0, 4)
            tipe = choice[0]
            s += "&{form}{:{fill}{width}{type}};".format(
                cp, form=form, fill=fill, width=width, type=tipe
            )
    return s
