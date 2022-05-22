import time
import concurrent.futures
import cv2
import matplotlib.pyplot as plt

def channels_30(img):
    b,g,r = cv2.split(img)

    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] += 0.2

    for i in range(len(g)):
        for j in range(len(g[i])):
            g[i][j] += 0.2

    for i in range(len(r)):
        for j in range(len(r[i])):
            r[i][j] += 0.2

    return cv2.merge((r,g,b))


if __name__ == "__main__":
    image_name = "bigbang.jpg"

    img = cv2.imread(image_name)

    start = time.time() 

    img_30 = channels_30(img)
    
    end = time.time()
    
    print(f"Took: {round(end - start, 2)} second(s).")

    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    plt.figure(figsize=(12,6))
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(img_30)
    plt.show()

    