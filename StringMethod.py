def length_string(s):
    return len(s)


def count_letter(tab, character):
    counter = 0
    for x in tab:
        print(x)
        if x == character:
            print(counter)
            counter += 1

    return counter
