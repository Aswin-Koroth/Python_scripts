import cv2 as cv
import os
import numpy as np
IMG_PATH = "crop.png"
IMG_NAME = IMG_PATH.split('\\')[-1].split('/')[-1].split('.')[0]
print()

AMG = {
            "main": [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 3]],
            "glass": [[1, 2],[1, 3]]
           }

def darken(img):
    if os.path.exists(f'{IMG_NAME}_dark.png'):
        return
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = [img[i, j][0]//4, img[i, j][1]//4, img[i, j][2]//4]
    cv.imwrite(f'{IMG_NAME}_dark.png', img)

def main():
    img = cv.imread(IMG_PATH)
    darken(img.copy())
    # print(img.shape)

    # print(all(img[1990,11] == img[1998,1]))


    # amg = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 3]]
    # im = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # im = cv.cvtColor(im, cv.COLOR_GRAY2BGR)
    im = cv.imread(f'{IMG_NAME}_dark.png')
    for i in range((img.shape[0]-5)-1):
        print("i = ", i)
        for j in range((img.shape[1]-4)-1):
            first = True
            ct = 0
            for c in AMG['main']:
                if first:
                    cmain = img[i+c[0],j+c[1]]
                    # cglass =
                    # print("======", cmain)
                if all(img[i+c[0], j+c[1]] == cmain):
                    # im[i+c[0], j+c[1]] = img[i+c[0], j+c[1]]
                    ct += 1

                first = False
            if ct == len(AMG['main']):
                for c in AMG['main']:
                    im[i + c[0], j + c[1]] = img[i + c[0], j + c[1]]
                    # print(f"found at loc {i},{j}")


    cv.imshow(IMG_NAME, im)
    cv.imwrite(f"{IMG_NAME.split('.')[0]}_final.png", im)
    cv.waitKey(0)
    # img[0,0] = [255,255,255] 193,58,73

    # print(img[0,0])
    # cv.imshow('img', cv.resize(img, (0,0), fy=0.4, fx=0.4))
    # cv.waitKey(0)

main()
