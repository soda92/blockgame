from PIL import Image
from pathlib import Path

CURRENT = Path(__file__).resolve().parent
RES_DIR = CURRENT.parent.joinpath("resources")

import os
files = os.listdir(str(RES_DIR))
files = [RES_DIR.joinpath(fn) for fn in files]
DEST_DIR = RES_DIR.joinpath("converted")
if not DEST_DIR.exists():
    os.mkdir(str(DEST_DIR))

for file in files:
    if not file.is_file(): continue
    im = Image.open(file)
    fn_noext = os.path.splitext(file.name)[0]
    im_png = fn_noext + ".png"
    im_png = DEST_DIR.joinpath(im_png)
    im.save(str(im_png))
