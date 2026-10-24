import sys
import shutil

def combine_phrase(elems: list, width: int):
    if len(elems) == 1:
        return "You entered nothing!"
    dissed_elems = []
    for elem in elems[1:]:
        if len(elem) > width:
            diff = len(elem) // width
            for i in range(diff):
                dissed_elems.append(elem[i * 0:(i + 1) * width - 1])
            dissed_elems.append(elem[(diff) * width:])
        else:
            dissed_elems.append(elem)
    result = []
    while len(dissed_elems) > 0:
        temp = dissed_elems.pop(0)
        if len(dissed_elems) == 0:
            break
        # point for space symbol
        while len(temp + dissed_elems[0]) + 1 <= width:
            temp += " " + dissed_elems.pop(0)
            if len(dissed_elems) == 0:
                break
        result.append(temp)
    return result


def main():
    win_size = shutil.get_terminal_size()
    phrase = combine_phrase(sys.argv, win_size.columns)
    for line in phrase:
        print(line)
    return

if __name__ == "__main__":
    main()