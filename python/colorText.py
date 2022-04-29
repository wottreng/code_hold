# background: allows background formatting. Accepts ANSI codes between 40 and 47, 100 and 107
# style_text: corresponds to formatting the style of the text. Accepts ANSI code between 0 and 8
# color_text:  Corresponds to the text of the color. Accepts ANSI code between 30 and 37, 90 and 97

class ANSI:

    def style(self, code: int):
        return f"\33[{code}m"

    def text(self):
        print("------color text----")
        x = 30
        while x < 38:
            print(f"\33[{x}m code {x}")
            x += 1
        x = 90
        while x < 98:
            print(f"\33[{x}m code {x}")
            x += 1
        print('---------------')
    def background(self):
        print("---background----")
        x = 40
        while x < 48:
            print(f"\33[{x}m style code {x}")
            x += 1
        # print("---background----")
        x = 100
        while x < 108:
            print(f"\33[{x}m style code {x}")
            x += 1
        print('---------------')
    def styleX(self):
        print("---style----")
        x = 0
        while x < 9:
            print(f"\33[{x}m style code {x}")
            x += 1
        print('---------------')



class colorText():

    def __init__(self):
        self.colors = {
            "white": "\33[97m",
            "red": "\33[91m",
            "green": "\33[92m",
            "gold": "\33[33m",
            "blue": "\33[34m",
            "yellow": "\33[93m"
        }
        self.blink = {True: "\33[5m", False: "\33[0m"}
        self.background = {
            "black": "\33[40m",
            "red": "\33[41m",
            "green": "\33[42m",
            "gold": "\33[43m",
            "blue": "\33[44m",
            "grey": "\33[100m"
        }
        self.underLine = {
            True: "\33[4m",
            False: "\33[0m"
        }
        self.bold = {
            True: "\33[1m",
            False: "\33[0m"
        }

    def printColorText(self, input: str = "", color: str = "white", blink: bool = False, underline: bool = False, bold: bool = False):
        if blink:
            input = f"{self.blink[blink]}{input}"
        if underline:
            input = f"{self.underLine[underline]}{input}"
        if bold:
            input = f"{self.bold[bold]}{input}"
        output = f"{self.colors[color]}{input}{self.colors['white']}\33[0m"
        print(output)


if __name__ == '__main__':
    colorText = colorText()
    print("==============")
    colorText.printColorText("test", color="blue", blink=False, underline=True, bold=False)
    print("==============")
    # ANSI = ANSI()

