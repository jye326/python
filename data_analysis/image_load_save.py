#이미지 생성 및 화면 출력

from scipy import datasets as ds

img_gray = ds.face(gray = True)
print(img_gray.shape)

import matplotlib.pyplot as plt


plt.imshow(img_gray)
plt.show()


