import enum


class ColorSquare(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    LIGHT_BLUE = 4
    YELLOW = 5
    ROSE = 6
    WHITE = 7
    NONE = 0


# Image
r, v, b, l, j, o, f, n = (
    ColorSquare.RED,
    ColorSquare.GREEN,
    ColorSquare.BLUE,
    ColorSquare.LIGHT_BLUE,
    ColorSquare.YELLOW,
    ColorSquare.ROSE,
    ColorSquare.WHITE,
    ColorSquare.NONE,
)


mapping = [
    [r, v, r, v, b, l, b, l, r, v, f, f, v, j, j, b, o, r, v, r],
    [o, j, j, b, o, r, o, r, j, b, f, f, b, r, v, l, v, j, j, b],
    [b, l, o, l, j, v, j, v, o, l, f, f, l, o, o, r, b, l, l, o],
    [r, v, f, f, r, v, j, b, j, b, b, l, v, j, r, v, j, b, b, l],
    [j, b, f, f, o, j, l, o, l, v, o, r, b, r, j, b, l, v, o, r],
    [o, l, f, f, b, l, v, r, o, r, j, v, l, o, o, l, o, r, j, v],
    [f, f, b, l, j, b, r, v, f, f, v, j, j, b, r, v, j, b, b, l],
    [f, f, o, r, l, v, j, b, f, f, b, r, l, v, j, b, l, o, j, o],
    [f, f, v, j, o, r, o, l, f, f, l, o, o, r, l, o, v, r, r, v],
    [j, b, o, r, b, l, v, j, j, b, j, b, f, f, o, r, f, f, j, b],
    [v, l, v, j, o, r, b, r, l, o, l, v, f, f, v, j, f, f, l, o],
    [o, r, b, l, j, v, l, o, v, r, o, r, f, f, b, l, f, f, r, v],
    [o, r, b, l, b, l, v, j, b, l, f, f, r, v, r, v, f, f, j, v],
    [v, j, j, o, o, r, b, r, j, o, f, f, j, o, j, b, f, f, b, l],
    [b, l, r, v, j, v, l, o, r, v, f, f, b, l, o, l, f, f, o, r],
    [o, r, f, f, j, v, v, j, v, r, j, b, r, v, f, f, r, v, r, v],
    [v, j, f, f, b, l, b, r, j, b, l, v, j, b, f, f, j, b, j, o],
    [b, l, f, f, o, r, l, o, l, o, o, r, o, l, f, f, o, l, b, l],
    [v, j, b, l, r, v, r, v, f, f, r, v, j, b, j, b, b, l, f, f],
    [b, r, o, r, j, b, j, b, f, f, j, o, l, o, l, v, o, r, f, f],
    [l, o, j, v, o, l, o, l, f, f, b, l, v, r, o, r, j, v, f, f],
    [j, v, r, v, f, f, j, b, b, l, j, b, r, v, b, l, j, b, f, f],
    [b, l, j, b, f, f, l, v, o, r, v, l, j, b, j, o, l, o, f, f],
    [o, r, o, l, f, f, o, r, v, j, o, r, o, l, r, v, v, r, f, f],
    [b, l, r, v, b, l, o, r, f, f, j, v, r, v, f, f, b, l, r, v],
    [r, j, j, b, j, o, v, j, f, f, b, l, j, b, f, f, j, o, j, b],
    [r, v, o, l, r, v, b, l, f, f, o, r, o, l, f, f, r, v, o, l],
    [b, l, b, l, j, v, b, l, o, r, b, l, f, f, r, v, r, v, f, f],
    [o, j, o, r, b, l, o, r, v, j, o, r, f, f, j, o, j, b, f, f],
    [r, v, v, j, o, r, j, v, b, l, j, v, f, f, b, l, o, l, f, f],
    [j, v, o, r, f, f, j, b, b, l, j, v, b, l, v, j, j, b, j, v],
    [b, l, v, j, f, f, v, l, o, r, b, l, o, r, b, r, l, o, b, l],
    [o, r, b, l, f, f, o, r, v, j, o, r, j, v, l, o, r, v, o, r],
    [v, j, r, v, o, r, b, l, v, j, j, b, j, b, f, f, v, r, b, l],
    [b, r, o, j, v, j, o, r, b, r, l, o, l, v, f, f, j, b, j, o],
    [l, o, b, l, b, l, j, v, l, o, v, r, o, r, f, f, l, o, r, v],
    [o, r, j, b, v, j, v, j, b, j, b, l, r, v, f, f, r, v, r, v],
    [v, j, l, o, r, b, b, r, l, o, o, r, j, b, f, f, j, o, j, b],
    [b, l, r, v, l, o, l, o, r, v, v, j, o, l, f, f, b, l, o, l],
    [f, f, j, v, v, j, j, b, o, r, v, r, r, v, n, n, n, n, n, n],
    [f, f, b, l, b, r, v, l, v, j, j, b, j, b, n, n, n, n, n, n],
    [f, f, o, r, l, o, o, r, b, l, l, o, o, l, n, n, n, n, n, n],
]

hexahue_alphabet = {
    "A": [o, r, v, j, b, l],
    "B": [r, o, v, j, b, l],
    "C": [r, v, o, j, b, l],
    "D": [r, v, j, o, b, l],
    "E": [r, v, j, b, o, l],
    "F": [r, v, j, b, l, o],
    "G": [v, r, j, b, l, o],
    "H": [v, j, r, b, l, o],
    "I": [v, j, b, r, l, o],
    "J": [v, j, b, l, r, o],
    "K": [v, j, b, l, o, r],
    "L": [j, v, b, l, o, r],
    "M": [j, b, v, l, o, r],
    "N": [j, b, l, v, o, r],
    "O": [j, b, l, o, v, r],
    "P": [j, b, l, o, r, v],
    "Q": [b, j, l, o, r, v],
    "R": [b, l, j, o, r, v],
    "S": [b, l, o, j, r, v],
    "T": [b, l, o, r, j, v],
    "U": [b, l, o, r, v, j],
    "V": [l, b, o, r, v, j],
    "W": [l, o, b, r, v, j],
    "X": [l, o, r, b, v, j],
    "Y": [l, o, r, v, b, j],
    "Z": [l, o, r, v, j, b],
    " ": [f, f, f, f, f, f],
    None: [n, n, n, n, n, n],
}


class HexahueDimensions(enum.Enum):
    height = 3
    width = 2
    size = height * width


class Image(enum.Enum):
    height = 524
    width = 524
    size = 524 * 524
    columns = len(mapping[0])
    rows = len(mapping)
    hexahue_columns = columns // HexahueDimensions.width.value
    hexahue_rows = rows // HexahueDimensions.height.value
    hexahue_size = hexahue_columns * hexahue_rows


def get_hexahue_letter(data):
    for key, val in hexahue_alphabet.items():
        if val == data:
            return key or ""


def get_hexahue_sequence(index):
    column = index % Image.hexahue_columns.value
    row = index // Image.hexahue_columns.value
    return [
        mapping[row * HexahueDimensions.height.value + i][
            column * HexahueDimensions.width.value + j
        ]
        for i in range(HexahueDimensions.height.value)
        for j in range(HexahueDimensions.width.value)
    ]


def hexahue_main():
    for i in range(Image.hexahue_size.value):
        yield get_hexahue_letter(get_hexahue_sequence(i))


def main():
    print("Step 1 - Hexahue\n")
    for i in hexahue_main():
        print(i, end="")
    print("\n")


if __name__ == "__main__":
    main()