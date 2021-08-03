from abc import ABC, abstractmethod


class Editor:
    formatted_text = []

    def __str__(self) -> str:
        return f"""{''.join(self.formatted_text)}"""


class TextFormatter(ABC):
    @abstractmethod
    def text_format(self):
        pass


class PlainTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.text = input('Text: ')
        self.text_format()

    def text_format(self):
        editor_class.formatted_text.append(self.text)
        print(editor_class.__str__())


class BoldTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.text = input('Text: ')
        self.text_format()

    def text_format(self):
        editor_class.formatted_text.append("**" + self.text + "**")
        print(editor_class.__str__())


class ItalicTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.text = input('Text: ')
        self.text_format()

    def text_format(self):
        editor_class.formatted_text.append("*" + self.text + "*")
        print(editor_class.__str__())


class InlineCodeTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.text = input('Text: ')
        self.text_format()

    def text_format(self):
        editor_class.formatted_text.append("`" + self.text + "`")
        print(editor_class.__str__())


class NewLineTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.text_format()

    def text_format(self):
        editor_class.formatted_text.append('\n')
        print(editor_class.__str__())


class LinkTextFormatter(TextFormatter):

    def __init__(self) -> None:
        self.label = input('Label: ')
        self.url = input('URL: ')
        self.text_format()

    def text_format(self):
        text = f"[{self.label}]({self.url})"
        editor_class.formatted_text.append(text)
        print(editor_class.__str__())


class HeaderTextFormatter(TextFormatter):

    def __init__(self) -> None:
        while True:
            try:
                self.level = int(input('Level: '))
                if self.level not in range(1, 7):
                    raise ValueError('')
                else:
                    break
            except ValueError:
                print("The level should be within the range of 1 to 6")
                continue
        self.header = input('Text: ')
        self.text_format()

    def text_format(self):
        text = f"{'#' * self.level} {self.header}\n"
        editor_class.formatted_text.append(text)
        print(editor_class.__str__())


class TextFormatterFactory(ABC):
    """
    Factory that represents a text formatter type.
    The factory doesn't maintain any of the instances it creates.
    """

    def get_text_formatter(self) -> TextFormatter:
        """ Returns a new text formatter instance. """


class PlainTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return PlainTextFormatter()


class BoldTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return BoldTextFormatter()


class ItalicTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return ItalicTextFormatter()


class InlineCodeTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return InlineCodeTextFormatter()


class NewLineTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return NewLineTextFormatter()


class LinkTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return LinkTextFormatter()


class HeaderTextFormatterFactory(TextFormatterFactory):

    def get_text_formatter(self) -> TextFormatter:
        return HeaderTextFormatter()


def read_text_formatter() -> TextFormatterFactory:
    commands = ['!help', '!done']
    formatters = {
        "plain": PlainTextFormatterFactory(),
        "bold": BoldTextFormatterFactory(),
        "italic": ItalicTextFormatterFactory(),
        "inline-code": InlineCodeTextFormatterFactory(),
        "new-line": NewLineTextFormatterFactory(),
        "link": LinkTextFormatterFactory(),
        "header": HeaderTextFormatterFactory()
    }

    while True:
        text_format = input('Choose a formatter: ')
        if text_format == '!done':
            exit()
        elif text_format == '!help':
            print("Available formatters:", *formatters.keys())
            print("Special commands:", *commands)
        elif text_format not in formatters:
            print('Unknown formatting type or command')
        else:
            return formatters[text_format]


def main(factory_: TextFormatterFactory) -> None:
    factory_.get_text_formatter()


if __name__ == '__main__':
    editor_class = Editor()
    while True:
        factory = read_text_formatter()
        main(factory)