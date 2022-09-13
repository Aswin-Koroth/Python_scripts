import cv2
import cv2 as cv
import numpy as np

img = cv.imread('scr1.png')
template = cv.imread('aa.png', 0)
# cv.imshow('m',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

w, h = template.shape

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    # img2 = img.copy()
    img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    method = eval(meth)

    result = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    print(top_left)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    im = cv.cvtColor(img2, cv.COLOR_GRAY2BGR)
    print(list(map(lambda x:x+1,top_left)))
    cv.rectangle(im, top_left, bottom_right, (0,0,255), 1)
    # cv.imshow('m',img2)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # img2 = img2[top_left[1]-1:bottom_right[1]+2, top_left[0]-1:bottom_right[0]+2]
    ret = cv.imwrite(f'img/{meth}.png', im)
