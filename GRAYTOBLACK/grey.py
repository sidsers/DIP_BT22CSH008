import cv2


# Load the color image
color_image = cv2.imread('GREY_IMAGE\gray_image.jpg')

# Convert the color image to grayscale
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Thresholding to convert grayscale image to black and white
_, bw_from_color = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Load the grayscale image directly (if you have one)
gray_image_direct = cv2.imread('GREY_IMAGE\gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Thresholding to convert directly loaded grayscale image to black and white
_, bw_from_gray = cv2.threshold(gray_image_direct, 128, 255, cv2.THRESH_BINARY)

# Display the images
cv2.imshow("",bw_from_color)
cv2.imshow("",bw_from_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
