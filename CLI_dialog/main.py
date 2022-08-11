import os

os.system('clear')

def window(title, content=""):
    terminal_width = os.get_terminal_size()[0]
    terminal_height = os.get_terminal_size()[1]
    space = terminal_width - (len("| Title: ") + len(title)) - 1

    sector_1 = top_left+hor*(terminal_width-2)+top_right
    sector_title = strip+f" Title: {title}"+" "*space+strip
    sector_3 = bottom_left+hor*(terminal_width-2)+bottom_right
    
    print(sector_1)
    print(sector_title)

    if (content == ""):
        sector_3 = bottom_left+hor*(terminal_width-2)+bottom_right
        print(sector_3)
        return 0
    else:  
        sector_3 = mid_l+hor*(terminal_width-2)+mid_r
        print(sector_3)

    space = terminal_width - len(content) - 3
    sector_4 = strip+f" {content}"+" "*space+strip
    sector_5 = bottom_left+hor*(terminal_width-2)+bottom_right

    print(sector_4)
    print(sector_5)

def version():
    window("CLI-GUI", "Version: 0.0.1")


if (__name__ == "__main__"):
    top_left = "┌"
    top_right = "┐"
    bottom_left = "└"
    bottom_right = "┘"
    strip = "│"
    hor = "—"
    mid_l = "├"
    mid_r = "┤"
