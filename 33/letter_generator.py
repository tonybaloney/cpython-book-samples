def letters():
    i = 97  # letter 'a' in ASCII
    end = 97 + 26  # letter 'z' in ASCII
    while i < end:
        yield chr(i)
        i += 1