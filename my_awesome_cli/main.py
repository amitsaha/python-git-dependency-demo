import fire


class Calculator(object):
    """A simple calculator class."""

    def double(self, number):
        return 2 * number


def main():
    fire.Fire(Calculator)


if __name__ == '__main__':
    main()
