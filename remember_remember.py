from PIL import Image


def remember_remember(image):
    """
    The function receives an image and return the message encrypted in it.
    The function passes each pixel in the image and checks if its color is black (to be exact (1, 1, 1)) if so the
    function inserts the letter representing the line number. And so the encrypted message is created.
    :param image: The image that is decoded.
    :return: The message encrypted.
    """
    encrypted_message = ""
    rgb_image = image.convert('RGB')

    for col in range(image.width):
        for row in range(image.height):
            if rgb_image.getpixel((col, row)) == (1, 1, 1):
                encrypted_message += chr(row)

    return encrypted_message


if __name__ == "__main__":
    with Image.open("code.png", 'r') as image:
        print(remember_remember(image))
