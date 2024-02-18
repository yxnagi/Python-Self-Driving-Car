import numpy as np
from PIL import ImageGrab
import cv2
import time
from sklearn.cluster import KMeans


hood_y = 400
horizon_y = 250
side_y = 15

VERTICES = np.array([
    [4, horizon_y + side_y],
    [220, horizon_y], [500, horizon_y],
    [800, horizon_y + side_y],
    [800, hood_y], [4, hood_y]]

)

def slope(line):
     try:
         if len(line) == 4: 
             y = line[1] - line[3]
             x = line[0] - line[2]
             slope_value = np.divide(y, x)
         else:
             slope_value = 1000000000 
     except ZeroDivisionError:
         slope_value = 1000000000
     finally:
         return slope_value

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass

def draw_lines2(img, lines):
    try:
        m = []
        for coords in lines:
            m.append(slope(coords))
            coords = np.array(coords, dtype='uint32')
            cv2.line(img,
                     (coords[0], coords[1]),
                     (coords[2], coords[3]),
                     [255, 255, 255], 15)
    except TypeError as e:
        print(f"draw lines error: ", e)
    else:
        pass


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_img = cv2.convertScaleAbs(processed_img, alpha=2.5, beta=-255)

    processed_img = cv2.Canny(processed_img, threshold1 = 175, threshold2 = 300)
    processed_img = roi(processed_img, [VERTICES])
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0 )

    lines = cv2.HoughLinesP(processed_img, 1,
                            np.pi/180, 180, np.array([]), 120, 20)
    nlines = np.array([])

    if lines is not None and len(lines) > 0:
       nlines = np.array([l[0] for l in lines])
       #draw_lines(processed_img,lines)

    try:
        kmeans = KMeans(n_clusters=2, random_state=0, n_init='auto').fit(nlines)
        draw_lines2(processed_img, kmeans.cluster_centers_)
    except (ValueError, TypeError) as e:
        #print(f"Kmeans ERROR", e)
        pass

    return processed_img



lasttime = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(640,300,1280,780)))
    new_screen = process_img(screen)


    print(f"LOOP TOOK {time.time()-lasttime} ")
    lasttime = time.time()
    cv2.imshow('window', new_screen)
    #cv2.imshow('window', cv2.cvtColor(np.array(printscreen_PIL), cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

