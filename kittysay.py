import sys
import shutil

def combine_phrase(elements: list):
    result = elements[2]
    if len(elements) == 2:
        return result
    else:
        for element in elements[2:]:
            result += " " + element
        return result


def  main():
    win_size = shutil.get_terminal_size()
    phrase = combine_phrase(sys.argv)
    print(phrase)
    return

if __name__ == "__main__":
    main()