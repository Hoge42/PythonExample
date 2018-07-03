"""サンプル用のモジュール

モジュールはPythonファイルで複数の変数、関数、クラス等を含む。
"""

import enum
from logging import getLogger


logger = getLogger(__name__)


def hey():
    """へい！"""
    logger.info('hey')


def sum_values(*values):
    """複数の数値を加算する

    >>> sum_values(1, 2, 3, 4, 5)
    15

    Args:
        *values (int): 加算する値

    Returns:
        int: 加算した値
    """
    return sum(values)


class MyEnum(enum.Enum):
    """何かの定義だ"""

    FISH = enum.auto()
    """int:さかな"""
    CAT = enum.auto()
    """int:ねこ"""
    DOG = enum.auto()
    """int:いぬ"""
