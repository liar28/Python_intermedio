def run():
    # challenge = [1, 2, 3, 4, 5]

    # base = [i**2 for i in challenge]

    # print(base)

    challenge = [1, 2, 3, 4, 5]

    base = list(map(lambda i: i**2, challenge))

    print(base)
if __name__ == "__main__":
    run()