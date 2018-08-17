Django_sample_page
===============
# Description

pythonウェブフレームワークであるDjango(ver2.X)を利用して、ウェブサーバーを構築。
ニュースサイト風を目指していた。

# how to run

## install

install python 3.5.2 or newer

```sh
$ python3 pip install django
```

install MySQL

```sh
$ sudo apt update
$ sudo apt install mysql-server mysql-client
```

install PyMySQL

```sh
$ apt-get install python3-dev libmysqlclient-dev
$ pip install PyMySQL
$ pip install mysqlclient
```

## set up

DjangoのデフォルトデータベースはSQLiteであるが、ここでは拡張性を考えMySQLを利用。

データベースとユーザーの作成

```sh
$ mysql -u root -p
mysql> CREATE DATABASE DatabaseName;
mysql> GRANT ALL ON DatabaseName.* TO UserName@localhost IDENTIFIED BY 'UserName';
mysql> show grants for UserName@localhost;

+-----------------------------------------------------------------------+
| Grants for UserName@localhost                                          |
+-----------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'UserName'@'localhost'                           |
| GRANT ALL PRIVILEGES ON `DatabaseName`.* TO 'UserName'@'localhost'     |
+-----------------------------------------------------------------------+
```


作成したユーザーでデータベースへの接続確認

```sh
$ mysql -u UserName -p
mysql> select user();

+-------------------+
| user()            |
+-------------------+
| UserName@localhost|
+-------------------+

mysql> show databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| DatabaseName       |
+--------------------+
```

マイグレート

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

テーブル生成の確認

```sh
$ mysql -u root -p DatabaseName -e "show tables"

+----------------------------+
| Tables_in_DatabaseName     |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+---------------------------
```


## usage

```sh
$ python manage.py runserver [port番号]
```

`[port番号]` オプションで指定しなかった場合は、`8000`がデフォルトで指定される。

- トップページ
<http://localhost:8000>


- ログインページ
<http://localhost:8000/accounts/login>


- Adminページ
<http://localhost:8000/admin>


- json受信用ページ
<http://localhost:8000/json_page>

