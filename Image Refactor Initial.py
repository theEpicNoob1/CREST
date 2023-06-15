from PIL import Image

def resize_image(image, new_width, new_height): # image width height
    image = Image.open(image)
    resizedImage = image.resize((new_width, new_height))
    resizedImage.save('resized_image.jpg')  

resize_image("Train Track.jpg", 30, 30) # width height



