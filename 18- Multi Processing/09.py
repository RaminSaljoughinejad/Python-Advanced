import time
import concurrent.futures
import cv2
import matplotlib.pyplot as plt


def channel_new(channel):
    for i in range(len(channel)):
        for j in range(len(channel[i])):
            channel[i][j] += 0.2
    return channel


if __name__ == "__main__":
    image_name = "bigbang.jpg"

    img = cv2.imread(image_name)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        start = time.time()
        b, g, r = cv2.split(img)
        b = executor.submit(channel_new, b)
        g = executor.submit(channel_new, g)
        r = executor.submit(channel_new, r)
        b = b.result()
        g = g.result()
        r = r.result()
        img_new = cv2.merge((r, g, b))
    
    end = time.time()

    print(f"Took: {round(end - start, 2)} second(s).")

    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(img_new)
    plt.show()