from PIL import Image, ImageOps
# Pillow
import sys
from time import perf_counter

darkmode = True
depth = 2

def imgtotxt(img):
    imgdata = ImageOps.grayscale(img)
    if not darkmode:
        imgdata = ImageOps.invert(imgdata)

    if depth == 2:
        chlist = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    elif depth == 1:
        chlist = " .iOE%@"
    inc = 255 / len(chlist)
    # chlist = {0: " ", 36: ".", 72: "i", 108: "O", 144: "E", 180: "%", 216: "@"}
    chr = ""
    pix = imgdata.getdata()
    with open(f"{img.filename}.txt", "a") as txt:
        for i, item in enumerate(pix):
            for j, ch in enumerate(chlist):
                    if item >= (j*inc):
                            chr = ch
            if i % img.width == 0 and i != 0:
                txt.write("\n")
            txt.write(f"{chr}  ")


def main():
    try:
        if sys.argv[1] == "/?":
            print(
                "Syntax:\npython img.py [image_path] [resolution]\nimage_path = Path of the image file.\nresolution = resolution of the output (values from 0 to 3, max res = 3).")
            exit(0)
        imgname = sys.argv[1]
    except Exception as e:
        print("Image path not specified\nType 'python img.py /?' for help")
        exit(0)
    image = Image.open(imgname)
    if len(sys.argv) == 2:
        res = 300
    else:
        if int(sys.argv[2]) > 3 or int(sys.argv[2]) < 0:
            print("Resolution value should be between 0 and 3")
            exit(0)
        res = float(sys.argv[2]) * 100
        print(res)

    maxsize = (res, res)
    image.thumbnail(maxsize, Image.ANTIALIAS)
    with open(f"{image.filename}.txt", "w") as f:
        f.write(f"{image.filename}\n")

    print("Creating textfile...")
    s = perf_counter()
    imgtotxt(image)
    e = perf_counter()
    print(f"Completed in {e-s} seconds")

# 19/2/2022
# Aswin Koroth
if __name__ == "__main__":
   main()





