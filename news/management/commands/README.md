ユーザー登録、記事登録
===============
# Description

テスト用にユーザー登録、記事登録を一括で行うスクリプト

# how to run

## set up

csvファイルを読込み、一括登録を行う。適宜以下ファイルを編集。

### ユーザー登録用ファイル
レコード username,e-mail address,password

```sh
django_sample_page/user_list.csv
```


### 記事登録用ファイル
レコード title,date,image,article

```sh
django_sample_page/insert_list.csv
```


## usage

```sh
$ python manage.py make_user
$ python manage.py insert_post
```


