from django.db.utils import ProgrammingError
from django.core.management.base import BaseCommand

from . import TECHNOLOGIES
from . import _MSGs as msg
from . import Technology

 
class Command(BaseCommand):
    help = "Popular tecnologias"

    def handle(self, *args, **options):
        techs = []
        for tech_name in TECHNOLOGIES:
            try:
                tech = Technology.objects.get(name=tech_name)
                self.stdout.write(msg.TECH_EXISTS.format(tech,))

            except Technology.DoesNotExist:
                tech = Technology(name=tech_name)
                techs.append(tech)
                self.stdout.write(msg.TECH_CREATION.format(tech,))

            except ProgrammingError:
                self.stdout.write(msg.PROGRAMMING_ERROR)
                exit()
        
        Technology.objects.bulk_create(techs)
