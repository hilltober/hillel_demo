class TextTag:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())


class ItalicWrapper(TextTag):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())


if __name__ == "__main__":
    simple_hello = TextTag("Hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print(simple_hello.render())
    print(special_hello.render())


# In this example, the TextTag class is a simple implementation of a text tag
# that holds a string of text. The BoldWrapper and ItalicWrapper classes
# are decorator classes that wrap instances of TextTag and add HTML
# bold and italic tags to the rendered text, respectively.
# The if __name__ == "__main__" block is the entry point of the program.
# When the program is run, it creates a TextTag instance with
# the text "Hello, world!", and then wraps it in BoldWrapper
# and ItalicWrapper instances. The render method of the resulting special_hello
# instance is then called to produce the final HTML output.


# У цьому прикладі клас TextTag є простою реалізацією текстового тегу,
# що містить рядок тексту. Класи BoldWrapper та ItalicWrapper
# це класи декораторів, які обгортають екземпляри TextTag і додають HTML
# теги 'напівжирний' та 'курсив' до відтвореного тексту відповідно.

# Блок if __name__ == "__main__" є точкою входу програми.

# Коли програма запускається, вона створює екземпляр TextTag з
# текстом "Hello, world!", а потім обгортає його в BoldWrapper
# та екземпляр ItalicWrapper.

# Потім викликається екземпляр для створення остаточного виводу HTML.
