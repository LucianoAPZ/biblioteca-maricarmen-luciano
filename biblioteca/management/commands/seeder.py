import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from faker import Faker
from biblioteca.models import *

IDIOMES = ["Català", "Español", "English", "Français"]
NUM_LLIBRES_PER_IDIOMA = 10
NUM_USUARIS = 50

class Command(BaseCommand):
    help = "Seeder para poblar la base de datos con libros, ejemplares y usuarios"

    def handle(self, *args, **kwargs):
        fake_catala = Faker('ca_ES')
        fake_espanol = Faker('es_ES')
        fake_ingles = Faker('en_US')
        fake_frances = Faker('fr_FR')

        fake_dict = {
            "Català": fake_catala,
            "Español": fake_espanol,
            "English": fake_ingles,
            "Français": fake_frances
        }

        # Crear países y lenguas si no existen
        paisos = {idioma: Pais.objects.get_or_create(nom=idioma)[0] for idioma in IDIOMES}
        llengues = {idioma: Llengua.objects.get_or_create(nom=idioma)[0] for idioma in IDIOMES}

        # Crear libros y ejemplares
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
                # Crear 2 ejemplares por libro
                for _ in range(2):
                    Exemplar.objects.create(
                        cataleg=llibre,
                        registre=fake.unique.isbn13(),
                        exclos_prestec=random.choice([True, False]),
                    )

        # Crear usuarios
        for _ in range(NUM_USUARIS):
            Usuari.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )

        self.stdout.write(self.style.SUCCESS("Datos insertados correctamente."))
