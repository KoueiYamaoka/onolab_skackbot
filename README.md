# Onolab Slackbot
小野研の Slack で運用されている Bot です．

## 準備
使用したいサーバ上で
``` shell
$ pip install slackclient --user
```
を走らせてください．

## 機能一覧
今はまだひとつだけ...

### プログラム終了通知
* プログラムが終了次第，Slack のダイレクトメッセージに通知が飛んできます．
* 使用方法
	* 自身が走らせたコマンドの末尾にセミコロンで区切って以下のコマンドを入力する．
    * username: Slack の表示名（display name）．空白文字を含む場合はダブルクオーテーションでくくること．
    * script_name: 実行しているスクリプト名など．オプション（Default: Your script）．
        ``` shell
        $ end_report username *script_name
        ```
* 使用例＆結果
    ```shell
    $ python test_script.py; end_report yamaoka "Test script"
    ```
    * Slack 上で: `Test script is completed :tada:`
