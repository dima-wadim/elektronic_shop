from django.core.management import BaseCommand

from users.models import Users


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = Users.objects.create(
            telegram_account='test_user',
            email='kantora_70@mail.ru',
            is_staff=False,
            is_superuser=False,
            is_active=True
        )

        user.set_password('qwe123zxc')
        user.save()
