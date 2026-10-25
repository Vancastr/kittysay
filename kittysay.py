import sys
import shutil

def combine_phrase(elems: list, width: int):
    if len(elems) == 1:
        return "You entered nothing!"
    maximum = 0
    dissed_elems = []
    for elem in elems[1:]:
        if len(elem) > maximum:
            maximum = len(elem)
        if len(elem) > width:
            diff = len(elem) // width
            for i in range(diff):
                dissed_elems.append(elem[i * 0:(i + 1) * width - 1])
            dissed_elems.append(elem[(diff) * width:])
        else:
            dissed_elems.append(elem)
    print(dissed_elems)
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
    print("-" * (length + 2))
    print("-" * (length + 2))

def main():
    win_size = shutil.get_terminal_size()
    phrase, length = combine_phrase(sys.argv, win_size.columns - 4)
    add_cloud(phrase, length)
    for line in phrase:
        print(line)
    return

if __name__ == "__main__":
    main()