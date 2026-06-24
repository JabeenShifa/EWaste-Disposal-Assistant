from PIL import Image


def display_image(uploaded_file):

    img = Image.open(uploaded_file)

    return img