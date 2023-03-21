from PIL import Image

# mac = Image.open('wall.png')
# # mac.show()
# print(mac.size)
# # mac.crop((0,0,100,100)).show()
# var = mac.crop((0,0,100,100))
# x = mac.paste(im=var,box=(243,209))
# mac.show()
# mac.rotate(90)


image1 = Image.open('mask.png')
matrix = Image.open('word_matrix.png')
image1.putalpha(200)
print(matrix.size)
print(image1.size)

t = matrix.resize((505,251))
print(t.size)
x = t.paste(image1,(0,0),image1)
t.show()

# print(matrix.size)
# image1.show()