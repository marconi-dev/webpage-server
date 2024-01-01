from django.db.utils import ProgrammingError
from django.core.management.base import BaseCommand

from . import _MSGs as msg
from . import PROFILE, LINKS
from . import Profile, ProfileLink

 
class Command(BaseCommand):
    help = "Popular perfil e links de perfil"

    def create_profile(self):
        try:
            profile = Profile.objects.first()

        except ProgrammingError:
            self.stdout.write(msg.PROGRAMMING_ERROR)
            return exit()

        if profile:
            self.stdout.write(msg.PROFILE_EXITS)
            self.profile = profile
            return
        
        self.profile = Profile.objects.create(**PROFILE)
        self.stdout.write(msg.PROFILE_CREATION)

    def create_profile_links(self):
        links = []
        for link_item in LINKS:
            try:
                link = ProfileLink.objects.get(name=link_item.get('name'))
                self.stdout.write(
                    msg.LINK_EXISTS.format(link_item.get('name'),)
                )

            except ProfileLink.DoesNotExist:
                link = ProfileLink(profile=self.profile, **link_item)
                links.append(link)
                self.stdout.write(
                    msg.LINK_CREATION.format(link_item.get('name'),)
                )

            except ProgrammingError:
                self.stdout.write(msg.PROGRAMMING_ERROR)
                exit()
        
        ProfileLink.objects.bulk_create(links)

    def handle(self, *args, **options):
        self.create_profile()
        self.create_profile_links()
