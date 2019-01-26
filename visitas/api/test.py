from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from lugares.models import Lugar
from usuarios.models import Usuario
from tags.models import Tag
from categorias.models import Categoria
from visitas.models import Visita


class VisitasAPITestCase(APITestCase):

    def setUp(self):
        tags = []
        tag = Tag.objects.create(nombre="Test - Tag")
        tags.append(tag)

        usuario = Usuario.objects.create(
            uid='Dq2hAFrjjwTR0SeGrTpKm8jr9Eq1',
            nombre='Usuario',
            email="test@test.com",
            foto='foto',
            fecha_nacimiento='1999-03-03',
            telefono='99999',
            genero='Masculino',
            departamento='Valle del Cauca',
            municipio='Ginebra')

        categoria = Categoria.objects.create(nombre="Nombre Categoria Test",
                                             foto="Foto Test")

        lugar = Lugar.objects.create(nombre="Lugar Test",
                                     descripcion="Descripcion Test",
                                     foto="{ }",
                                     calificacion=1,
                                     email="{ }",
                                     sitio_web="{ }",
                                     telefono="{ }",
                                     redes="{ }",
                                     direccion="Direccion Test",
                                     hora_abierto="{06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00, 06:00:00}",
                                     hora_cerrado="{22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00, 22:00:00}",
                                     dias_servicio="{Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo}",
                                     latitud=17890,
                                     longitud=54321,
                                     categoria=categoria,
                                     propietario=usuario,
                                     fecha_creacion="1996-08-15",
                                     municipio="Municipio Test",
                                     departamento="Departamento Test")

        lugar.tag.set(tags)

        visita = Visita.objects.create(usuario=usuario,
                                       lugar=lugar,
                                       fecha_visita="2015-01-12",
                                       hora_visita="11:11:00")

    #########################################################################
    def test_single_categoria(self):
        categoria_count = Categoria.objects.count()
        self.assertEqual(categoria_count, 1)

    def test_single_tags(self):
        tags_count = Tag.objects.count()
        self.assertEqual(tags_count, 1)

    def test_single_usuario(self):
        usuario_count = Usuario.objects.count()
        self.assertEqual(usuario_count, 1)

    def test_single_lugar(self):
        lugar_count = Lugar.objects.count()
        self.assertEqual(lugar_count, 1)

    def test_single_visita(self):
        visita_count = Visita.objects.count()
        self.assertEqual(visita_count, 1)

    #########################################################################
    def test_get_visitas_list_forbidden(self):
        data = {}
        url = api_reverse("api-visitas:visitas-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #########################################################################
    def test_get_visitas_list_with_user_ok(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ2MjE0NSwiZXhwIjoxNTQ4NDY1NzQ1LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.JhoPGy_2PKHp2M0C96UaInxRdTNmw8bgzd4yU-d4k7s7rtipb-QL_WSVvhgHZltzPcIGuL79htuYC5E9OYv9u9rSuNkciAnfkKhYs0UCydyebWzmBIb7fhV-7eBc55N0R42zDFvqFU57xG_tvP2ogF3EJmenzk7f0HF17_hETelERIhsBhZraQW-L240yuoZ6ODQmwDyjVNIFhfA_bs6D28BdbnLbbhTtaUvAd151SoN5uz3Y8wk1Eunqog-5k6XqZssqInmVKyun0ANwM6g8OAOXSpTjg7DP2IL-qWq1YISj7p-Up_W1GwXoCaarOsRfCDsiTLT6GiuYXn094AemA")
        data = {}
        url = api_reverse("api-visitas:visitas-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #########################################################################
    def test_post_visitas_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ2MjE0NSwiZXhwIjoxNTQ4NDY1NzQ1LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.JhoPGy_2PKHp2M0C96UaInxRdTNmw8bgzd4yU-d4k7s7rtipb-QL_WSVvhgHZltzPcIGuL79htuYC5E9OYv9u9rSuNkciAnfkKhYs0UCydyebWzmBIb7fhV-7eBc55N0R42zDFvqFU57xG_tvP2ogF3EJmenzk7f0HF17_hETelERIhsBhZraQW-L240yuoZ6ODQmwDyjVNIFhfA_bs6D28BdbnLbbhTtaUvAd151SoN5uz3Y8wk1Eunqog-5k6XqZssqInmVKyun0ANwM6g8OAOXSpTjg7DP2IL-qWq1YISj7p-Up_W1GwXoCaarOsRfCDsiTLT6GiuYXn094AemA")

        data = {"usuario":1,
                "lugar":1,
                "fecha_visita":"1996-05-05",
                "hora_visita":"11-11-11"}

        url = api_reverse("api-visitas:visitas-create")
        print(url)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #########################################################################
    def test_put_visitas_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ1Nzk2NCwiZXhwIjoxNTQ4NDYxNTY0LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.v75f3olYx5wtqCCbJjO7rrpAhyrSwxIQUQShc7YYYJjPYkxpScM8Wo9KwJRmhsjhe8I9Y5xe1fKVroJGfo-TbfW4TQ8nXWo9uWLix7D9j6oj32tkz_kwc396kJXifQphRqtK4_8mjbFMP9cNt2pBn81YORY19o8G6rKaC8pOPAwJrsVk2--OcBOCYpQu_OfuCEUippRiGh2piPIkN6kQjeB675UD8xTfjblqKGFwt4vi2MNRurKsnmRdg3hZmvMpRO7q1dk3R2y4NYUoCw37alypnIZnh_LabVjDb6-7iW3g_VqPLUayp8JDHfAzsN6Q7kxzjTLkMSfMNutP1ca07w")

        visitas = Visita.objects.first()
        url = visitas.get_api_url()

        data = {"usuario": 1,
                "lugar": 1,
                "fecha_visita": "1992-05-05",
                "hora_visita": "01-01-01"}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
