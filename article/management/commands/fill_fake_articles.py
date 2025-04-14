from django.core.management.base import BaseCommand
from faker import Faker
from article.models import Article


class Command(BaseCommand):
    help = 'Заполняет БД фейковыми статьями'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Количество создаваемых статей (по умолчанию 50)'
        )
        parser.add_argument(
            '--lang',
            type=str,
            default='ru_RU',
            help='Язык данных (ru_RU, en_US и др., по умолчанию ru_RU)'
        )

    def handle(self, *args, **options):
        count = options['count']
        lang = options['lang']
        tag_choices = [tag[0] for tag in Article.TAG_CHOICES]
        try:
            fake = Faker(lang)
        except AttributeError:
            self.stderr.write(self.style.ERROR(f'Неверный язык: {lang}. Использую русский (ru_RU) по умолчанию.'))
            fake = Faker('ru_RU')

        self.stdout.write(f'Создание {count} статей с языком {lang}...')

        for _ in range(count):
            Article.objects.create(
                title=fake.sentence(nb_words=6),  # Заголовок из 6 слов
                content=fake.text(max_nb_chars=1000),  # Текст до 1000 символов
                localisation=lang,
               # tag=fake.random_element(elements=tag_choices),
                published_at=fake.date_time_this_year()
            )

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {count} статей с языком {lang}')
        )
