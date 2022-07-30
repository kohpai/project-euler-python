

def read_names(filename: str):
    with open(filename) as f:
        return f.read().replace('"', "").split(",")


def alphabetical_value(name: str):
    return sum(list(map(lambda x: ord(x) - 64, name)))


if __name__ == '__main__':
    names = sorted(read_names("p022_names.txt"))
    values = list(map(alphabetical_value, names))
    scores = [(i+1) * value for i, value in enumerate(values)]
    # print(names)
    # print(values)
    # print(scores)
    print(sum(scores))
