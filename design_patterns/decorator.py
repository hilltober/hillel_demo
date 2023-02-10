class TextTag:
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


if __name__ == "__main__":
    simple_hello = TextTag("Hello, world!")
    special_hello = ItalicWrapper(BoldWrapper(simple_hello))
    print(simple_hello.render())
    print(special_hello.render())


# У цьому прикладі клас TextTag є простою реалізацією текстового тегу,
# що містить рядок тексту. Класи BoldWrapper та ItalicWrapper
# це класи декораторів, які обгортають екземпляри TextTag і додають HTML
# теги 'напівжирний' та 'курсив' до відтвореного тексту відповідно.

# Блок if __name__ == "__main__" є точкою входу програми.

# Коли програма запускається, вона створює екземпляр TextTag з
# текстом "Hello, world!", а потім обгортає його в BoldWrapper
# та екземпляр ItalicWrapper.

# Потім викликається екземпляр для створення остаточного виводу HTML.
