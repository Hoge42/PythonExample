from mypackage import mymodule
import logging.config


def main():
    mymodule.hey()
    values = list(range(100))
    print(mymodule.sum_values(*values))


if __name__ == '__main__':
    logging.config.fileConfig("development.ini")
    main()
