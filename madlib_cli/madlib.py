import re

intro = """
************************************************
** Welcome to the Mad Lib!                    **
** Please see directions below.               **
**                                            **
**                                            **
** Please type a lower case word or number    **
** based on what you are prompted.            **
**                                            **
************************************************
"""

def read_template(file):
    try:
        with open(file) as d:
            return d.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    pieces = tuple(re.findall(r"{([^{}]*)}", string))
    for x in pieces:
        string = string.replace(x, "")
    return string, pieces


def merge(stripped, inputs):
    return stripped.format(*inputs)


print(intro)
script = read_template("examples/video_game_ex.txt")
empty_string, parts = parse_template(script)
filled_list = []
for i in parts:
    user_input = input(f" Enter {i} > ")
    filled_list.append(user_input)
result = merge(empty_string, filled_list)
print(result)
with open('output.txt', 'w') as writer:
    writer.write(result)