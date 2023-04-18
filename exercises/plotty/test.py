import cv2
from matplotlib import pyplot as plt

img = cv2.imread("test.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# RGB a quel pixel
print(img[300, 200])
img[300, 200] = [0, 0, 0]
print(img[300, 200])

#accessing RED value
print(img.item(10,10,2)) # 59
#modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2)) # 100

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.imshow(img)
f.add_subplot(1, 2, 2)

plt.show()

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball