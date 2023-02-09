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
