import sys
import shutil

def combine_phrase(elems: list, width: int):
    if len(elems) == 1:
        return "You entered nothing!"
    maximum = 0
    dissed_elems = []
    for elem in elems[1:]:
        if len(elem) > width:
            diff = len(elem) // width
            for i in range(diff):
                dissed_elems.append(elem[i * width:(i + 1) * width - 1])
            dissed_elems.append(elem[(diff) * width:])
        else:
            dissed_elems.append(elem)
    for elem in dissed_elems:
        if len(elem) > maximum:
            maximum = len(elem)
    result = []
    while len(dissed_elems) > 0:
        temp = dissed_elems.pop(0)
        if len(dissed_elems) == 0:
            result.append(temp)
            break
        # point for space symbol
        while len(temp + dissed_elems[0]) + 1 <= width:
            temp += " " + dissed_elems.pop(0)
            if len(dissed_elems) == 0:
                break
        result.append(temp)
    return result, maximum

def add_cloud(text: list, length: int):
    print(" " + "_" * (length + 2))
    if len(text) > 1:
        print(f"/ {text[0]}" + " " * (length - len(text[0])) + " \\")
        for i in range(1, len(text) - 1):
            print(f"| {text[i]}" + " " * (length - len(text[i])) + " |")
        print(f"\\ {text[-1]}" + " " * (length - len(text[-1])) + " /")
    else:
        print(f"< {text[0]} >")
    print(" " + "-" * (length + 2))

def add_kitty():
    for i in range(2, 4):
        print(" " * i + "\\")
    print("     |\\__/,|   (`\\")
    print("     |_ _  |.--.) )")
    print("     ( T   )     /")
    print("    (((^_(((/(((_/")

def main():
    columns = 30
    win_size = shutil.get_terminal_size()
    if win_size.columns < 19:
        print("Not enough space for kitty :(")
        return
    if win_size.columns - 4 < columns:
        columns = win_size.columns - 4
    phrase, length = combine_phrase(sys.argv, columns)
    add_cloud(phrase, length)
    add_kitty()
    return

if __name__ == "__main__":
    main()