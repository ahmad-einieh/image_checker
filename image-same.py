from PIL import Image
import imagehash
# x = [imagehash.average_hash(Image.open("image-same/apple1.png")),
#      imagehash.average_hash(Image.open("image-same/apples2.png")),
#      imagehash.average_hash(Image.open("image-same/orange1.jpg")),
#      imagehash.average_hash(Image.open("image-same/orange2.jpg")),
#      imagehash.average_hash(Image.open("image-same/tree1.png")),
#      imagehash.average_hash(Image.open("image-same/tree2.jpg"))]

y = [
    imagehash.average_hash(Image.open("image-same/tree2.jpg")),
    imagehash.average_hash(Image.open("image-same/apples2.png")),
    imagehash.average_hash(Image.open("image-same/orange2.jpg")),
    imagehash.average_hash(Image.open("image-same/tree1.png")),
    imagehash.average_hash(Image.open("image-same/apple1.png")),
    imagehash.average_hash(Image.open("image-same/orange1.jpg")),
]

# Image.open("image-same/orange1.jpg").show()


# image1 = imagehash.average_hash(Image.open("image-same/apple1.png"))
# image2 = imagehash.average_hash(Image.open("image-same/apples2.png"))
# image3 = imagehash.average_hash(Image.open("image-same/orange1.jpg"))
# image4 = imagehash.average_hash(Image.open("image-same/orange2.jpg"))
# image5 = imagehash.average_hash(Image.open("image-same/tree1.png"))
# image6 = imagehash.average_hash(Image.open("image-same/tree2.jpg"))

tolerance = 20

for i in range(6):
    for j in range(5, -1, -1):
        if i == j:
            continue
        if y[i] - y[j] < tolerance:
            print(f"{i} - {j} same")
