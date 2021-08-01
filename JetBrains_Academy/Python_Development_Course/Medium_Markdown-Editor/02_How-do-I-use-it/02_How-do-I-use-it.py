def exit_():
    exit()


def help_():
    print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done""")


def main_():
    while True:
        formatter = input('Choose a formatter: ')
        if formatter in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line", "!help", "!done"]:
            if formatter == '!help':
                help_()
            elif formatter == '!done':
                exit_()   
        else:
            print("Unknown formatting type or command")


main_()