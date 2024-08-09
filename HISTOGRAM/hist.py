
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('HISTOGRAM\img.jpeg', cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)
cv2.imwrite('equalized_image.jpg', equalized_image)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[1, 0].hist(image.ravel(), bins=256, range=[0, 256])
axs[1, 0].set_title('Histogram of Original Image')
axs[0, 1].imshow(equalized_image, cmap='gray')
axs[0, 1].set_title('Equalized Image')
axs[0, 1].axis('off')
axs[1, 1].hist(equalized_image.ravel(), bins=256, range=[0, 256])
axs[1, 1].set_title('Histogram of Equalized Image')

plt.show()
