def pluck(input_string: str, characters: list[str]):
    output_string = ''
    removed_chars = set()
    for char in input_string:
        if char not in characters:
            output_string += char
            continue
        removed_chars.add(char)

    return output_string, removed_chars


def eval(operator: str, *vals):
    if len(vals) < 2:
        raise RuntimeError('not enough terms')
    output_val = vals[0]
    for _, val in enumerate(vals, start=1):
        if operator == '+':
            output_val += val
        elif operator == '-':
            output_val -= val
        elif operator == '*':
            output_val *= val
        elif operator == '/':
            output_val /= val
