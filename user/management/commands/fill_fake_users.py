from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User


class Command(BaseCommand):
    help = 'Заполняет БД фейковыми пользователями'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Количество создаваемых пользователей (по умолчанию 100)'
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

        try:
            fake = Faker(lang)
        except AttributeError:
            self.stderr.write(self.style.ERROR(f'Неверный язык: {lang}. Использую русский (ru_RU) по умолчанию.'))
            fake = Faker('ru_RU')

        self.stdout.write(f'Создание {count} пользователей с языком {lang}...')

        for _ in range(count):
            User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=70),
                localisation=lang,
            )

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {count} пользователей с языком {lang}')
        )