import random
from html.entities import html5

# HTML5 named character references
# https://docs.python.org/3/library/html.entities.html#html.entities.html5
HTML5_CHARS = {html5[key]: key for key in html5}

ENTITIES = {
    "d": "#",  # decimal
    "x": "#x",  # hexadecimal lowercase
    "X": "#x",  # hexadecimal uppercase
}


def evade(value):
    s = ""
    for char in value:

        # HTML5 named character references
        if char in HTML5_CHARS and random.randint(0, 1):
            name = HTML5_CHARS[char]
            s += "&{}".format(name)
        else:

            # Decimal and hexadecimal references
            cp = ord(char)
            choice = random.choice(list(ENTITIES.items()))
            form = choice[1]
            fill = "0"
            width = random.randint(0, 4)
            tipe = choice[0]

            # Format Specification Mini-Language
            # https://docs.python.org/3/library/string.html#formatspec
            s += "&{form}{:{fill}{width}{type}};".format(
                cp, form=form, fill=fill, width=width, type=tipe
            )

    return s
