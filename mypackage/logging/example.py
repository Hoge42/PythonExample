"""ログ出力のサンプル

ログ出力はlogging.getLoggerでロガーを取得して使う。

.. code-block:: python

    from logging import getLogger


    logger = getLogger(__name__)

``logging.info('foo')`` などとはしてはいけない。
loggingに直接ログを流すとrootロガーを使用するので、ログ出力の分離ができない。
つまり誰がログを吐いたのか特定するのを難しくするし、パッケージ・ライブラリごとの
ログ出力レベルの変更などができないのだ。

``logger = getLogger(__name__)`` とするとモジュール単位でロガーが取得できる。
この場合のロガーは `mypackage.logging.example` になる。

モジュール単位でログ出力を分離するとロガーは木構造になっている。
例えばmypackage以下はファイルに出力、mypackage.subpackage以下はエラー時にメールを送信といったように
パッケージごとに出力方法やログレベル等を設定できる。

"""
from logging import getLogger


logger = getLogger(__name__)


def run():
    logger.debug('ログ1')
    logger.info('ログ2')
    logger.warning('ログ3')
    logger.error('ログ4')
    try:
        1 / 0
    except Exception as error:
        logger.exception(error)
