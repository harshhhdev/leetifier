# First ever Python project. Turns text into numbers. for example -> "Hello There!", becomes "H3ll0 7h3r3!"

mock_text = input()

new = []


def numify(text):
    for c in text:
        if c == 'a' or c == 'A':
            c = '4'
            new.append(c)
        elif c == 'e' or c == 'E':
            c = '3'
            new.append(c)
        elif c == 't' or c == 'T':
            c = '7'
            new.append(c)
        elif c == 's' or c == 'S':
            c = '5'
            new.append(c)
        elif c == 'i' or c == 'I' or c =='l':
            c = '1'
            new.append(c)
        elif c == 'o' or c == 'O':
            c = '0'
            new.append(c)
        elif c == 'p' or c == 'P':
            c = '9'
            new.append(c)
        else:
            new.append(c)

    return ''.join(new)


print(numify(mock_text))
