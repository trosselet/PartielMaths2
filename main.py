from Transform import Transform


def main():
    t = Transform(0, 0, 0, 0, 0, 0)
    t.translate(1, 2, 3)
    t.rotate(30, 45, 0)
    print(t)


if __name__ == "__main__":
    main()