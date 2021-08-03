class MarkDown:
    formatters = ['plain', 'bold', 'italic', 'inline-code', "new-line", "link", "header"]
    special_commands = ['!help', '!done']
    lists = ['ordered-list', 'unordered-list']
    
    def __init__(self):
        self.result_str = []
        self.status = True

    def special_command(self, command):
        if command == '!done':
            self.status = False
        else:
            print("Available formatters:", *MarkDown.formatter)
            print("Special commands:", *MarkDown.special_commands)
    
    def set_text(self, formatter):
        if formatter == 'new-line':
            self.result_str.append("\n")
        else:
            input_text = input("Text: ")
            if formatter == 'plain':
                self.result_str.append(input_text)
            elif formatter == 'bold':
                self.result_str.append(f"**{input_text}**")
            elif formatter == 'italic':
                self.result_str.append(f"*{input_text}*")
            elif formatter == 'inline-code':
                self.result_str.append(f"`{input_text}`")
            
    def set_header(self):
        while True:
            level = input("Level: ")
            try:
                level = int(level)
                if 0 < level < 7:
                    result = f"{'#' * level}"
                    break
                else:
                    raise ValueError 
            except ValueError:
                print("The level should be within the range of 1 to 6")

        input_txt = input("Text: ")
        if len(self.result_str) != 0:
            self.result_str.append('\n')
        self.result_str.append(f"{result} {input_txt}")
        self.result_str.append('\n')

    def set_list(self, formatter):
        while True:
            try:
                number = int(input("Number of rows: "))
                if number > 0:
                    for i in range(1, number + 1):
                        ele = input(f"Row #{i}: ")
                        if formatter == 'unordered-list':
                            self.result_str.append(f'* {ele}\n')
                        else:
                            self.result_str.append(f'{i}. {ele}\n')
                    break
                else:
                    raise ValueError
            except ValueError:
                print("The number of rows should be greater than zero")

    def set_link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.result_str.append(f"[{label}]({url})")

    def main_(self):
        while self.status:
            formatter = input('Choose a formatter: ')
            if formatter in MarkDown.special_commands:
                self.special_command(formatter)
            elif formatter in MarkDown.formatters:
                if formatter in MarkDown.formatters[:5]:
                    self.set_text(formatter)
                elif formatter == 'header':
                    self.set_header()
                elif formatter == 'link':
                    self.set_link()
                self.save_md_print()
            elif formatter in MarkDown.lists:
                self.set_list(formatter)
                self.save_md_print()
            else:
                print("Unknown formatting type or command")
                
    def save_md_print(self):
        for str in self.result_str:
            print(str, end="")
        print()

md = MarkDown()
md.main_()