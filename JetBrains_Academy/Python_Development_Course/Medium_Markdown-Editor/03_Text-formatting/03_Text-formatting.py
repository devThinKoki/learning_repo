class MarkDown:
    formatters = ['plain', 'bold', 'italic', 'inline-code', "new-line", "link", "header"]
    special_commands = ['!help', '!done']
    
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

    def set_link(self):
        label = input("Label: ")
        url = input("URL: ")
        self.result_str.append(f"[{label}]({url})")

    def main_(self):
        while self.status:
            formatter = input('Choose a formatter: ')
            if formatter in MarkDown.special_commands:
                self.special_command(formatter)
            elif formatter not in MarkDown.formatters:
                print("Unknown formatting type or command")
            else:
                if formatter in MarkDown.formatters[:5]:
                    self.set_text(formatter)
                elif formatter == 'header':
                    self.set_header()
                elif formatter == 'link':
                    self.set_link()
                self.save_md_print()
                

    def save_md_print(self):
        for str in self.result_str:
            print(str, end="")
        print()
        # if self.result_str:
            # with open('markdown.md', 'a') as f:
                # f.write(self.result_str)
            # with open('markdown.md') as f:
                # lines = f.readlines()
                # for line in lines:
                    # print(line.strip())
            # self.result_str = ''

md = MarkDown()
md.main_()


# def main_():
#     while True:
#         formatter = input('Choose a formatter: ')
#         if formatter in ['!help', '!done']:
#             special_command(formatter)
#         elif formatter in ['plain', 'bold', 'italic', 'inline-code', "header", "link", "new-line"]:
#             if formatter in ['plain', 'bold', 'italic', 'inline-code']:
#                 line = print_text(formatter)
#             elif formatter == 'header':
#                 line = print_header()
#             elif formatter == 'link':
#                 line = print_link()
#             elif formatter == 'new-line':
#                 line = '\n'
            
#             if line:
#                 with open('markdown.md', 'a') as f:
#                     f.write(line)
#                 with open('markdown.md') as f:
#                     lines = f.readlines()
#                     for line in lines:
#                         print(line, end='')

#                 if formatter == 'header' or formatter == 'new-line':
#                     print()
#         else:
#             print("Unknown formatting type or command")

# def special_command(command):
#     if command == '!done':
#         exit()
#     else:
#         print("""Available formatters: plain bold italic header link inline-code new-line
# Special commands: !help !done""")

# def print_text(format):
#     input_text = input("Text: ")
#     if format == 'plain':
#         return input_text
#     elif format == 'bold':
#         return f"**{input_text}**"
#     elif format == 'italic':
#         return f"*{input_text}*"
#     elif format == 'inline-code':
#         return f"`{input_text}`"

# def print_header():
#     try:
#         level = int(input("Level: "))
#         input_text =input('Text: ')
#         if 0 < level < 7:
#             return f"{'#' * level} {input_text}\n"
#         else:
#             raise ValueError
#     except ValueError:
#         print("The level should be within the range of 1 to 6")

# main_()