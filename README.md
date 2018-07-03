# PythonExample
ToxとかSphinxとかloggingとかUnitTestとかのサンプルプロジェクト

## インストール手順

### 1. Python仮想環境を作成

Python3.6が既にインストールされているとして、docs, mypackage, testsなどがあるディレクトリでvenvを作成する

```bash
$ python3 -m venv venv
```

### 2. Python仮想環境を有効化
#### Linux
```bash
$ source venv/bin/activate
(venv) $
```

#### Windows
```
> venv\Scripts\activate.bat
(venv) >
```

### 3. 依存パッケージをインストール
#### デプロイ時
```bash
(venv) $ pip install -r requirements.txt
```

#### 開発時
```bash
(venv) $ pip install -r requirements_develop.txt
```

### 4. 自動テスト実行
テストが全てsucceededならOK

```bash
(venv) $ tox
（中略）
___________________________________ summary ___________________________________
  flake8: commands succeeded
  docs: commands succeeded
  py36: commands succeeded
  congratulations :)
```

### 5. ドキュメントを読む
`docs/build/index.html` にドキュメントが出来上がるので読む

