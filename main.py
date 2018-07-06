import argparse


from mypackage import mymodule
import logging.config


def main():
    mymodule.hey()
    values = list(range(100))
    print(mymodule.sum_values(*values))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='サンプルプロジェクト')
    parser.add_argument('config', type=str, help='コンフィグファイルパス')
    args = parser.parse_args()
    logging.config.fileConfig(args.config)
    main()
