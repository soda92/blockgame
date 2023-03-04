from PIL import Image, UnidentifiedImageError
from pathlib import Path

CURRENT = Path(__file__).resolve().parent
RES_DIR = CURRENT.parent.joinpath("resources")
DEST_DIR = RES_DIR.joinpath("converted")
DEST_DIR.mkdir(exist_ok=True)

files = RES_DIR.glob("*")
files = list(filter(Path.is_file, files))


for file in files:
    try:
        im = Image.open(file)
    except UnidentifiedImageError:
        continue
    else:
        im_png = file.stem + ".png"
        im_png = DEST_DIR.joinpath(im_png)
        im.save(im_png)
