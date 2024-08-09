
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('HISTOGRAM\img.jpeg')
def brighten_image(img, value=50):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    brightened_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return brightened_img


def darken_image(img, value=50):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.subtract(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    darkened_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return darkened_img


brightened_image = brighten_image(image, value=50)
darkened_image = darken_image(image, value=50)

cv2.imwrite('brightened_image.jpg', brightened_image)
cv2.imwrite('darkened_image.jpg', darkened_image)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')

axs[1].imshow(cv2.cvtColor(brightened_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Brightened Image')
axs[1].axis('off')

axs[2].imshow(cv2.cvtColor(darkened_image, cv2.COLOR_BGR2RGB))
axs[2].set_title('Darkened Image')
axs[2].axis('off')

plt.show()