from django.core.management.base import BaseCommand
from faker import Faker
from company.models import Company


class Command(BaseCommand):
    help = 'Заполняет БД фейковыми статьями'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Количество создаваемых компаний (по умолчанию 10)'
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
        sector_choices = [tag[0] for tag in Company.SECTOR_CHOICES]

        try:
            fake = Faker(lang)
        except AttributeError:
            self.stderr.write(self.style.ERROR(f'Неверный язык: {lang}. Использую русский (ru_RU) по умолчанию.'))
            fake = Faker('ru_RU')

        self.stdout.write(f'Создание {count} компаний с языком {lang}...')

        for _ in range(count):
            Company.objects.create(
                name=fake.company(),
                #sector=fake.random_element(elements=sector_choices),
                inn=fake.random_number(digits=12, fix_len=True),  # 12-значный ИНН
                founded_date=fake.date_between(start_date='-30y', end_date='today'),
                localisation=lang,
                # created_at добавится автоматически (auto_now_add=True)
            )

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {count} компаний с языком {lang}')
        )
