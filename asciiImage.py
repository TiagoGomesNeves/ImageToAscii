from PIL import Image
import sys


def getAscii(brightness):
    segments = '".`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'
    segment_index = (brightness / 255.0) * (len(segments) - 1)
    character = segments[int(round(segment_index, 0))]

    return character


def main():
    try:
        image = Image.open(sys.argv[1]).convert("L")
        image = image.resize((128, 128), Image.LANCZOS)
    except FileNotFoundError:
        print("Image not Found")
        return

    asciiImage = []
    width = image.width
    height = image.height
    for y in range(height):
        asciiRow = []
        for x in range(width):
            brightness = 255 - image.getpixel((x, y))
            asciiRow.append(getAscii(brightness))

        asciiImage.append(("").join(asciiRow))

    for row in asciiImage:
        print(row)


if __name__ == "__main__":
    main()
