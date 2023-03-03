from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
IMG_Dir = CURRENT_DIR.parent.parent.joinpath("resources").joinpath("converted")
IMG_Path = IMG_Dir.joinpath("girl.png")
X_Splits = 4
