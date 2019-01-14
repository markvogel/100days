# https://www.practicepython.org/solution/2014/12/25/23-file-overlap-solutions.html


def read_file(file_to_read):
    with open(f'{file_to_read}.txt', 'r') as open_file:
        all_text = open_file.read()
        return all_text


def overlap(input_a: list, input_b: list):
    same = (set(input_a).intersection(input_b))
    return sorted([int(i) for i in list(same)])


if __name__ == '__main__':
    prime = read_file('primenumbers').split(sep='\n')
    happy = read_file('happynumbers').split(sep='\n')
    print((overlap(prime, happy)))
