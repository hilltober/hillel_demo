class Image:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        print("Loading image from file {}".format(self.filename))


class ImageProxy:
    def __init__(self, filename):
        self._filename = filename
        self._image = None

    def load(self):
        if not self._image:
            self._image = Image(self._filename)
        self._image.load()


if __name__ == "__main__":
    image = ImageProxy("image.png")
    print("Image not loaded yet")
    image.load()
    print("Image loaded")


# In this example, the Image class represents the real object that
# is being proxied. The ImageProxy class acts as a proxy for Image objects,
# and provides a simplified interface for loading images from files.
# The load method of the ImageProxy class only loads the actual image when
# it is first accessed.
# The if __name__ == "__main__" block is the entry point of the program.
# When the program is run, it creates an instance of ImageProxy and prints
# a message indicating that the image has not been loaded yet. When the load
# method is called, the message changes to indicate that the image
# has been loaded.
