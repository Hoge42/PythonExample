インストール手順
================

1. Python仮想環境を作成
--------------------------------

Python3系が既にインストールされているとして、docs, mypackage, testsなどがあるディレクトリでvenvを作成する

.. code-block:: bash

    $ python3 -m venv venv

2. Python仮想環境を有効化
--------------------------------

.. code-block:: bash
    :caption: Linux

    $ source venv/bin/activate
    (venv) $

.. code-block:: none
    :caption: Windows

    > venv\Scripts\activate.bat
    (venv) >


3. 依存パッケージをインストール
--------------------------------

.. code-block:: bash
    :caption: デプロイ時

    (venv) $ pip install -r requirements.txt

.. code-block:: bash
    :caption: 開発時

    (venv) $ pip install -r requirements_develop.txt

4. 自動テスト実行
--------------------------------

テストが全てsucceededならOK

.. code-block:: bash

    (venv) $ tox
    （中略）
    .___________________________________ summary ___________________________________
      flake8: commands succeeded
      docs: commands succeeded
      py36: commands succeeded
      congratulations :)
