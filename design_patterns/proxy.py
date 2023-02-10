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


# У цьому прикладі клас Image представляє реальний об'єкт, який
# виконується проксі. Клас ImageProxy діє як проксі для об’єктів Image,
# та забезпечує спрощений інтерфейс для завантаження зображень із файлів.
# Метод завантаження класу ImageProxy завантажує фактичне зображення лише тоді,
# коли це перший доступ.

# Блок if __name__ == "__main__" є точкою входу програми.

# Коли програма запускається, вона створює екземпляр ImageProxy і друкує
# повідомлення про те, що зображення ще не завантажено. При виклику метода load
# повідомлення змінюється, щоб вказати, що зображення завантажено.
