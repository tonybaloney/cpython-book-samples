def gen_letters(start, x):
    i = start
    end = start + x
    while i < end:
        yield chr(i)
        i += 1

def letters(upper):
    if upper:
        yield from gen_letters(65, 26)  # A-Z
    else:
        yield from gen_letters(97, 26)  # a-z

for letter in letters(False):
    # Lower case a-z
    print(letter)

for letter in letters(True):
    # Upper case A-Z
    print(letter)