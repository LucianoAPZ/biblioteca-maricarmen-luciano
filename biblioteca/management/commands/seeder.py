import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from faker import Faker
from biblioteca.models import *

IDIOMES = ["Français", "English", "Deutsch", "Italiano"]
NUM_LLIBRES_PER_IDIOMA = 10
NUM_USUARIS = 50

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake_frances = Faker('fr_FR')
        fake_ingles = Faker('en_US')
        fake_aleman = Faker('de_DE')
        fake_italiano = Faker('it_IT')

        fake_dict = {
            "Français": fake_frances,
            "English": fake_ingles,
            "Deutsch": fake_aleman,
            "Italiano": fake_italiano
        }

        paisos = {idioma: Pais.objects.get_or_create(nom=idioma)[0] for idioma in IDIOMES}
        llengues = {idioma: Llengua.objects.get_or_create(nom=idioma)[0] for idioma in IDIOMES}

        for idioma in IDIOMES:
            fake = fake_dict[idioma]
            for _ in range(NUM_LLIBRES_PER_IDIOMA):
                llibre = Llibre.objects.create(
                    titol=fake.sentence(nb_words=4),
                    autor=fake.name(),
                    CDU=fake.isbn10(),
                    data_edicio=fake.date_between(start_date="-10y", end_date="today"),
                    resum=fake.text(),
                    pais=paisos[idioma],
                    llengua=llengues[idioma],
                )
                for _ in range(2):
                    Exemplar.objects.create(
                        cataleg=llibre,
                        registre=fake.unique.isbn13(),
                        exclos_prestec=random.choice([True, False]),
                    )

        for _ in range(NUM_USUARIS):
            Usuari.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )

        self.stdout.write(self.style.SUCCESS("Datos insertados correctamente."))
