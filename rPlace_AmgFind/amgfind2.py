import cv2 as cv
import os

IMG_PATH = "crop.png"
IMG_NAME = os.path.basename(IMG_PATH).split('.')[0]

AMG = [
        {
            "name": "Normal Right",
            "body": [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 3]],
            "eye": [[1, 3], [1, 2]],
            "extra": [[0, 0], [3, 0], [4, 0], [4, 2]]
        },
        {
            "name": "Normal Left",
            "body": [[0, 0], [0, 1], [0, 2], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [4, 0], [4, 2]],
            "eye": [[1, 0], [1, 1]],
            "extra": [[0, 3], [3, 3], [4, 1], [4, 3]]
        },
        {
            "name": "Short Right",
            "body": [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [2, 3], [3, 1], [3, 3]],
            "eye": [[1, 3],[1, 2]],
            "extra": [[0, 0], [3, 0], [3, 2]]
        },
        {
            "name": "Short left",
            "body": [[0, 0], [0, 1], [0, 2], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 2]],
            "eye": [[1, 0], [1, 1]],
            "extra": [[0, 3], [3, 1], [3, 3]]
        },
        {
            "name": "No_Bag Short Right",
            "body": [[0, 1], [0, 2], [0, 3], [1, 1], [2, 1], [2, 2], [2, 3], [3, 1], [3, 3]],
            "eye": [[1, 3], [1, 2]],
            "extra": [[0, 0], [1, 0], [2, 0], [3, 0], [3, 2], [4, 1], [4, 3]]
        },
        {
            "name": "No_Bag Short left",
            "body": [[0, 0], [0, 1], [0, 2], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]],
            "eye": [[1, 0], [1, 1]],
            "extra": [[0, 3], [3, 1], [3, 3], [1, 3], [2, 3]]
        }
      ]




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
    im = cv.imread(f'{IMG_NAME}_dark.png')
    count = 0
    for i in range((img.shape[0]-5)+1):
        print("i = ", i)
        for j in range((img.shape[1]-4)+1):

            for a in AMG:
                bcount = 0
                gcount = 0
                ecount = 0

                first = True
                brk = 0
                # acc = 1
                error = 0
                reg = img[i:i + 5, j:j + 4]
                for o in (a['body']+a['eye']+a['extra']):
                    temp = reg[o[0], o[1]]
                    if first:
                        body_color = reg[a['body'][1][0], a['body'][1][1]]
                        eye_color = reg[a['eye'][0][0], a['eye'][0][1]]
                    if o in a['extra']:
                        if any(temp != body_color):
                            ecount += 1

                    elif o in a['eye']:
                        if all(temp == eye_color) and any(temp != body_color):
                            gcount += 1

                    elif all(temp == body_color):
                        bcount += 1
                    else:
                        if brk == 1:
                            break
                        brk += 1
                    first = False
                    error = (len(a['body']) + len(a['eye']) + len(a['extra']) - (gcount + bcount + ecount))
                # if i == 118 and j == 25 and a['name'] == 'Short Right':
                #     print(bcount, gcount, ecount, a['name'])
                #     exit(0)
                # if bcount == len(a['main']) and gcount == len(a['glass']) and ecount == len(a['extra']) :
                if error <= 1:
                    # if a['name'] == "No_Bag Short left":
                    #     print(bcount, gcount, ecount)
                    #     exit(0)
                    # print(f"found at loc {i},{j}")
                    count += 1
                    for c in a['body'] + a['eye']:
                        im[i + c[0], j + c[1]] = img[i + c[0], j + c[1]]
                    break

    cv.imshow(IMG_NAME, im)
    print("Count =", count)
    cv.imwrite(f"{IMG_NAME}_final_{count}.png", im)
    cv.waitKey(0)

# Aswin Koroth
main()
# img = cv.imread('crop.png')
# cv.imwrite('test.png', img[118:123, 25:29])
#

