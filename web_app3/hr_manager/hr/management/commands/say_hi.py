from django.core.management.base import BaseCommand, CommandError


# folosim commands sa schimbam automat mai multe chestii, in admin ar dura mult,
# de exemplu sa schimbi tote legaturile intre ceva tabele

class Command(BaseCommand):
    help = "print something in console"

    def add_arguments(self, parser):
        parser.add_argument("--message", "-m", type=str, default=None)

    def handle(self, *args, message, **options):
        if message:
            print(message)
        else:
            raise CommandError("no message argument provided")
