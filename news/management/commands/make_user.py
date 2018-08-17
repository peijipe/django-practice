from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'make new users'

    def handle(self, *args, **options):
        count = 0
        with open('user_list.csv', encoding="utf-8") as f:
            for row in f:
                columns = row.rstrip().split(',')
                User.objects.create_user(
                    username=columns[0], email=columns[1], password=columns[2]
                    )
                count += 1
            print(str(count) + 'ユーザー追加')
