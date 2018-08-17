Django_sample_page
===============
# Description

python�E�F�u�t���[�����[�N�ł���Django(ver2.X)�𗘗p���āA�E�F�u�T�[�o�[���\�z�B
�j���[�X�T�C�g����ڎw���Ă����B

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

Django�̃f�t�H���g�f�[�^�x�[�X��SQLite�ł��邪�A�����ł͊g�������l��MySQL�𗘗p�B

�f�[�^�x�[�X�ƃ��[�U�[�̍쐬

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


�쐬�������[�U�[�Ńf�[�^�x�[�X�ւ̐ڑ��m�F

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

�}�C�O���[�g

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

�e�[�u�������̊m�F

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
$ python manage.py runserver [port�ԍ�]
```

`[port�ԍ�]` �I�v�V�����Ŏw�肵�Ȃ������ꍇ�́A`8000`���f�t�H���g�Ŏw�肳���B

- �g�b�v�y�[�W
<http://localhost:8000>


- ���O�C���y�[�W
<http://localhost:8000/accounts/login>


- Admin�y�[�W
<http://localhost:8000/admin>


- json��M�p�y�[�W
<http://localhost:8000/json_page>

