"""Google StyleのDocstringのサンプル

このモジュールはnapoleonの `Example Google Style Python Docstrings`_ の翻訳

本家からいろいろアレンジしたり省略したりしている

仕様の詳細は `Google Python Style Guide`_ を見るべし

Attributes:
    module_level_variable1 (int): モジュールレベルの変数その1
    module_level_variable2 (int): モジュールレベルの変数その2

Todo:
    * モジュールのTODOのサンプル
    *  ``sphinx.ext.todo`` のSphinx拡張をconf.pyに追加するべし

.. _Example Google Style Python Docstrings:
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

module_level_variable1 = 12345

module_level_variable2 = 98765


def function_with_types_in_docstring(param1, param2):
    """Docstringで型を指定する関数のサンプル

    Args:
        param1 (int): ほげ
        param2 (str): ぴよ

    Returns:
        bool: 成功したらTrue、それ以外はFalse

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """型ヒントを使用する関数のサンプル

    Args:
        param1: ほげ
        param2: ぴよ

    Returns:
        成功したらTrue、それ以外はFalse

    """


def module_level_function(param1, param2=None, *args, **kwargs):
    """モジュールレベル関数のサンプル

    関数のパラメータはArgsに書くべき。各パラメータ名は必須。
    型と説明は省略可能だが、自明でないなら書くべきだ

    引数のフォーマットは次のように書く::

        変数名 (型): 説明
            説明は複数行で書ける。二行目以降はインデントする

            空行を挟むと段落を分けられる

    Args:
        param1 (int): ほげ
        param2 (:obj:`str`, optional): デフォルトはNone
            2行目はインデントする必要がある
        *args: 位置引数
        **kwargs: キーワード引数

    Returns:
        bool: 成功したらTrue、それ以外はFalse

        引数の説明と同様にインデントをつけて複数行で書ける

        reStructuredTextのフォーマットも使える::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: この関数が投げる例外のリスト。これは引数に関連するエラー
        ValueError: params1とparams2が等しいとき

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """ジェネレーターのサンプル

    Returnsの代わりにYieldsを書く

    Args:
        n (int): 生成値の上限値で、0から `n` - 1の範囲

    Yields:
        int: 0 から `n` - 1の次の値

    Examples:
        ExamplesにはDoctestのフォーマットで、この関数がどのように使われるかを書こう

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


class ExampleError(Exception):
    """例外はクラスと同様にdocstringを書ける

    __init__メソッドのdocstringはクラスレベルにも書ける。
    どっちに書いても構わないが、混在してはいけない。

    Note:
        self引数はArgsに書かないこと

    Args:
        msg (str): 例外の説明文
        code (:obj:`int`, optional): エラーコード

    Attributes:
        msg (str): 例外の説明文
        code (int): エラーコード

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


class ExampleClass(object):
    """1行目にはクラスの概要を書く

    クラスがpublic属性を持つなら、Argsセクションと同じフォーマットで
    Attributesセクションに書ける。
    あるいは__init__の中での代入のところでインラインでも書ける。

    ``@property`` デコレータで作ったプロパティの説明ははプロパティのゲッターに書くべきだ。

    Attributes:
        attr1 (str): ほげ
        attr2 (:obj:`int`, optional): ぴよ

    """

    def __init__(self, param1, param2, param3):
        """__init__ メソッドのdocstringのサンプル

        __init__メソッドのdocstringはここにもクラスレベルのdocstringにも書ける。
        どっちに書いても構わないが、混在してはいけない。

        Note:
            self引数はArgsに書かないこと

        Args:
            param1 (str): ほげ
            param2 (:obj:`int`, optional): ぴよ
            param3 (list(str)): ふが

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: public属性のコメントは行末にもインラインで書ける

        #: list(str): public属性のコメントは前の行にもインラインで書ける
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: docstringは行のあとにも書けるぞ"""

    @property
    def readonly_property(self):
        """str: プロパティの説明はゲッターメソッドに書くべきだ"""
        return 'readonly_property'

    @property
    def readwrite_property(self):
        """list(str): ゲッターとセッターをもつプロパティの説明はゲッターのみに書くべきだ

        もしセッターメソッドが特殊な動作をするなら、それはここに書くべきだ
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        pass

    def example_method(self, param1, param2):
        """クラスメソッドは関数と同様に書ける

        Note:
            ただしself引数はArgsセクションには書かない

        Args:
            param1: ほげ
            param2: ぴよ

        Returns:
            成功ならTrue、それ以外はFalse

        """
        return True

    def _private(self):
        """privateな関数

        これは通常Sphinxのapidocでは出力されない

        """
        pass
