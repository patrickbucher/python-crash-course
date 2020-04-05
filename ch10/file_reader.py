def get_pi(filename):
    pi = ''
    with open(filename) as f:
        for line in f:
            pi += line.strip()
    return pi


if __name__ == '__main__':
    pi = get_pi('pi.txt')
    print(pi)
