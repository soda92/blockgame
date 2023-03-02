from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
IMG_Dir = CURRENT_DIR.parent.parent.joinpath("resources")
IMG_Path = IMG_Dir.joinpath("girl.jpeg")
X_Splits = 4
