from django_unicorn.components import UnicornView
from users.models import Section

class SectionsView(UnicornView):
    section:Section
    def mount(self):
        self.section = self.request.user.user_section
        print(self.section.skill)

    def change(self):
        self.section.save()


