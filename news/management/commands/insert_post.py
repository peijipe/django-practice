from django.core.management.base import BaseCommand
from news.models import Post


class Command(BaseCommand):
    help = 'insert posts list'

    def handle(self, *args, **options):
        count = 0
        with open('insert_list.csv', encoding="utf-8") as f:
            for row in f:
                columns = row.rstrip().split(',')
                Post.objects.create(
                    title=columns[0], pub_date=columns[1], image=columns[2], body=columns[3]
                    )
                count += 1
            print(str(count) + '件追加')
