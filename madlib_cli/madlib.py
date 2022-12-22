def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


# def parse_template(string):


def merge(stripped, inputs):
    return stripped.format(*inputs)


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