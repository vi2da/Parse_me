import path_manipule as pm
import re

PATH = r"C:/Users/David/Desktop/Projects/Java/Games/Nim/Nim/Move.java"

# need to a reggex funk for find the num in start of lines
def del_line_nums(line):
    pattern = r'\w+\s+'
    spl = re.split(pattern, line, maxsplit=1)
    print(spl)
    return spl[1] if len(spl) >= 2 else ""
    


def action_on_line(line):
    return del_line_nums(line)


def manipulat_files(txt_abs_path):
    head, name, Extension = pm.get_pure_base_name(txt_abs_path)
    from_f = open(txt_abs_path, 'r')
    try:
        new_f = open(pm.append_to_base_name(txt_abs_path, "Manipulated"), 'a+')
    except FileExistsError:
        print("The name already exist")

    for line in from_f:
        new_f.write(action_on_line(line))

    from_f.close()
    new_f.close()


def main():
    manipulat_files(PATH)


if __name__ == '__main__':
    main()