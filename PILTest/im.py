from PIL import Image

im = Image.open('image.jpeg')
print(im.size)

im2 = im.resize((600,600)
print(im2.size)

im.thumbnail((500,500))
im.save('image2.jpeg')
im3 = Image.open('image2.jpeg')
print(im3.size)
