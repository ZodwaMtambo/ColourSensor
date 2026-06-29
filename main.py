import numpy as np
from PIL import Image

image = Image.open ("images/20221225_174227.jpg")
image_array = np.array(image)

#phase 2 
plain_image = Image.open ("images/Image 3.jpeg")
plain_image_array = np.array(plain_image)


image2= Image.open("images/Image 2.jpeg")
image2_array = np.array (image2)


image1= Image.open("images/Image 1.jpeg")
image1_array = np.array (image1)


print("plain image size:", plain_image_array.size)
print("plain image shape:", plain_image_array.shape)
print ("image2 size:", image2_array.size)
print("image2 shape:", image2_array.shape)
print ("image1 size:", image1_array.size)
print("image1 shape:", image1_array.shape)

#reshaping. 
Ex_image = image2_array.reshape(-1,3)
print ("plain picture 2D list:", Ex_image)
print (" New shape", Ex_image.shape)

#k-means
from sklearn.cluster import KMeans

model = KMeans (n_clusters= 3, random_state= 42)
X = model.fit_predict(Ex_image)
print(X)

print (model.cluster_centers_.astype(int))