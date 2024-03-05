from PIL import Image, ImageEnhance, ImageFilter
import os

# path to directory containing photos to edit
pathIn = "./to_edit"

# path to directory containing photos that have been edited
pathOut = "/edited"

print("Welcome to ImageEditor!")
print("What would you like done today?\nEnter a number that represents your service")
while True:
    try:
        order = int(input("1.Sharpen\n2.Increase Contrast\n3.Black and White Filter\n4.Convert to Thumbnail\nOrder:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Sharpen Image
if order == 1:
    for filename in os.listdir(pathIn):
        im = Image.open(f"{pathIn}/{filename}")
        edit = im.filter(ImageFilter.SHARPEN)
        clean_name = os.path.splitext(filename)[0]
        edit.save(f".{pathOut}/{clean_name}_edited.jpg")
# Enhance Contrast
elif order == 2:
    for filename in os.listdir(pathIn):
        im = Image.open(f"{pathIn}/{filename}")
        factor = 1.5
        enhancer = ImageEnhance.Contrast(im)
        edit = enhancer.enhance(factor)
        clean_name = os.path.splitext(filename)[0]
        edit.save(f".{pathOut}/{clean_name}_edited.jpg")
# Convert to Black and White
elif order == 3:
    for filename in os.listdir(pathIn):
        im = Image.open(f"{pathIn}/{filename}")
        edit = im.convert('L')
        clean_name = os.path.splitext(filename)[0]
        edit.save(f".{pathOut}/{clean_name}_edited.jpg")
# Resize to YouTube thumbnail
elif order == 4:
    for filename in os.listdir(pathIn):
        im = Image.open(f"{pathIn}/{filename}")
        size = (1280, 720)
        edit = im.resize(size)
        clean_name = os.path.splitext(filename)[0]
        edit.save(f".{pathOut}/{clean_name}_thumbnail.jpg")

else:
    print("Incorrect input! You cant handle all this!")
