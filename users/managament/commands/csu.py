from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            email='kantora_70@mail.ru',
            name='admin',
            phone='+79615457453',
            is_staff=True,
            is_superuser=True,
            is_active=True

        )

        user.set_password('qwe123zxc')
        user.save()
        print('superuser created')
