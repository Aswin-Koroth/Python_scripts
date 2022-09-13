import cv2 as cv
import os

IMG_PATH = "place2022.png"
IMG_NAME = os.path.basename(IMG_PATH).split('.')[0]
shape = (7, 5)
AMG = [
        {
            "name": "Long Right",
            "body": [[1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[2, 3], [2, 2]],
            "extra": [[0, 1], [0, 2], [0, 3], [1, 0], [1, 4], [3, 4], [4, 4], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "Long left",
            "body": [[1, 1], [1, 2], [1, 3], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[2, 1], [2, 2]],
            "extra": [[0, 1], [0, 2], [0, 3], [1, 0], [1, 4], [3, 0], [4, 0], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "Normal Right",
            "body": [[2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [4, 0], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[3, 3], [3, 2]],
            "extra": [[1, 1], [1, 2], [1, 3], [2, 0], [2, 4], [4, 4], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "Normal Left",
            "body": [[2, 1], [2, 2], [2, 3], [3, 3], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[3, 1], [3, 2]],
            "extra": [[1, 1], [1, 2], [1, 3], [2, 0], [2, 4], [4, 0], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "No_Bag Normal Right",
            "body": [[2, 1], [2, 2], [2, 3], [3, 1], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[3, 3], [3, 2]],
            "extra": [[1, 1], [1, 2], [1, 3], [2, 0], [2, 4], [3, 0], [4, 0], [4, 4], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "No_Bag Normal Left",
            "body": [[2, 1], [2, 2], [2, 3], [3, 3], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[3, 1], [3, 2]],
            "extra": [[1, 1], [1, 2], [1, 3], [2, 0], [2, 4], [3, 4], [4, 0], [4, 4], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "Short Right",
            "body": [[3, 1], [3, 2], [3, 3], [4, 0], [4, 1], [5, 0], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[4, 3], [4, 2]],
            "extra": [[2, 1], [2, 2], [2, 3], [3, 0], [3, 4], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "Short left",
            "body": [[3, 1], [3, 2], [3, 3], [4, 3], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4], [6, 1], [6, 3]],
            "eye": [[4, 1], [4, 2]],
            "extra": [[2, 1], [2, 2], [2, 3], [3, 0], [3, 4], [5, 0], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "No_Bag Short Right",
            "body": [[3, 1], [3, 2], [3, 3], [4, 1], [5, 0], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[4, 3], [4, 2]],
            "extra": [[2, 1], [2, 2], [2, 3], [3, 0], [3, 4], [4, 0], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
        },
        {
            "name": "No_Bag Short left",
            "body": [[3, 1], [3, 2], [3, 3], [4, 3], [5, 1], [5, 2], [5, 3], [6, 1], [6, 3]],
            "eye": [[4, 1], [4, 2]],
            "extra": [[2, 1], [2, 2], [2, 3], [3, 0], [3, 4], [4, 4], [5, 0], [5, 4], [6, 0], [6, 2], [6, 4]]
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
    for i in range((img.shape[0]-shape[0])+1):
        print(i)
        for j in range((img.shape[1]-shape[1])+1):

            for a in AMG:
                # if a['name'] != "No_Bag Normal Right":
                #     continue
                bcount = 0
                gcount = 0
                ecount = 0

                first = True
                brk = 0
                acc = 1
                error = 0
                reg = img[i:i + shape[0], j:j + shape[1]]
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

                    elif all(temp == eye_color):
                            bcount -= 1
                    else:
                        if brk == 1:
                            break
                        brk += 1
                    first = False
                    error = (len(a['body']) + len(a['eye']) + len(a['extra']) - (gcount + bcount + ecount))
                # if i == 7 and j == 90 :
                #     print(bcount, gcount, ecount, a['name'], error)
                #     exit(0)
                if len(a['body']) < 10:
                    acc = 0
                if bcount >= len(a['body']) - acc and gcount >= len(a['eye']) - acc and ecount >= len(a['extra']) - 2 and error < 3 :
                    # print(f"found at loc {i},{j}")
                    count += 1
                    for c in a['body'] + a['eye']:
                        im[i + c[0], j + c[1]] = img[i + c[0], j + c[1]]
                    break

    cv.imshow(IMG_NAME, im)
    print("Count =", count)
    cv.imwrite(f"{IMG_NAME}_final1_{count}.png", im)
    cv.waitKey(0)

# 6/4/2022
# Ok-Patience-9530
main()

