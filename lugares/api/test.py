from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from lugares.models import Lugar
from usuarios.models import Usuario
from tags.models import Tag
from categorias.models import Categoria
from comentarios.models import Comentario


class LugaresAPITestCase(APITestCase):

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

        categoria = Categoria.objects.create(
            nombre="Test Categoria",
            descripcion="Test Categoria Descripcion",
            foto="Test Foto Categoria")

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

    #########################################################################
    def test_get_lugares_list_forbidden(self):
        data = {}
        url = api_reverse("api-lugar:lugar-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #########################################################################
    def test_get_lugares_list_with_user_ok(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ2MjE0NSwiZXhwIjoxNTQ4NDY1NzQ1LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.JhoPGy_2PKHp2M0C96UaInxRdTNmw8bgzd4yU-d4k7s7rtipb-QL_WSVvhgHZltzPcIGuL79htuYC5E9OYv9u9rSuNkciAnfkKhYs0UCydyebWzmBIb7fhV-7eBc55N0R42zDFvqFU57xG_tvP2ogF3EJmenzk7f0HF17_hETelERIhsBhZraQW-L240yuoZ6ODQmwDyjVNIFhfA_bs6D28BdbnLbbhTtaUvAd151SoN5uz3Y8wk1Eunqog-5k6XqZssqInmVKyun0ANwM6g8OAOXSpTjg7DP2IL-qWq1YISj7p-Up_W1GwXoCaarOsRfCDsiTLT6GiuYXn094AemA")
        data = {}
        url = api_reverse("api-lugar:lugar-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #########################################################################
    def test_post_lugares_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ2MjE0NSwiZXhwIjoxNTQ4NDY1NzQ1LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.JhoPGy_2PKHp2M0C96UaInxRdTNmw8bgzd4yU-d4k7s7rtipb-QL_WSVvhgHZltzPcIGuL79htuYC5E9OYv9u9rSuNkciAnfkKhYs0UCydyebWzmBIb7fhV-7eBc55N0R42zDFvqFU57xG_tvP2ogF3EJmenzk7f0HF17_hETelERIhsBhZraQW-L240yuoZ6ODQmwDyjVNIFhfA_bs6D28BdbnLbbhTtaUvAd151SoN5uz3Y8wk1Eunqog-5k6XqZssqInmVKyun0ANwM6g8OAOXSpTjg7DP2IL-qWq1YISj7p-Up_W1GwXoCaarOsRfCDsiTLT6GiuYXn094AemA")

        data = {"direccion": "Km 1 Vía El Cerrito - Ginebra",
                "fecha_creacion": "2019-01-10",
                "tag": [{"nombre": "Test - Tag", "id": 1}],
                "telefono": ["2561150", "3113595768", "3162830130"],
                "descripcion": "Somos un restaurante campestre, prestamos servicios de alimentos y bebidas de comida típica vallecaucana e internacional, atendemos reuniones sociales.",
                "comentario": [],
                "nombre": "Restaurante el Naranjal",
                "categoria": 1,
                "dias_servicio": ["LUN", "MAR", "MIE", "N", "VIE", "SAB", "N"],
                "municipio": "Ginebra",
                "email": ["restauranteelnaranjal@hotmail.com"],
                "calificacion": 1.5,
                "departamento": "Valle del Cauca",
                "hora_abierto": ["06:00 a.m.", "06:00 a.m.", "06:00 a.m.", "N", "06:00 a.m.", "08:00 a.m.", "N"],
                "sitio_web": ["https:\/\/www.livevalledelcauca.com\/"],
                "latitud": 3.7036843,
                "propietario": 1,
                "longitud": -76.2940772,
                "hora_cerrado": ["22:00 p.m.", "22:00 p.m.", "22:00 p.m.", "N", "22:00 p.m.", "22:00 p.m.", "N"],
                "foto": ["gs:\/\/trabajo-de-grado-f9cb8.appspot.com\/lugares\/1\/slider-logo.png"],
                "redes": ["www.facebook.com", "www.twitter.com"]}

        url = api_reverse("api-lugar:lugar-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #########################################################################
    def test_put_lugares_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ1Nzk2NCwiZXhwIjoxNTQ4NDYxNTY0LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.v75f3olYx5wtqCCbJjO7rrpAhyrSwxIQUQShc7YYYJjPYkxpScM8Wo9KwJRmhsjhe8I9Y5xe1fKVroJGfo-TbfW4TQ8nXWo9uWLix7D9j6oj32tkz_kwc396kJXifQphRqtK4_8mjbFMP9cNt2pBn81YORY19o8G6rKaC8pOPAwJrsVk2--OcBOCYpQu_OfuCEUippRiGh2piPIkN6kQjeB675UD8xTfjblqKGFwt4vi2MNRurKsnmRdg3hZmvMpRO7q1dk3R2y4NYUoCw37alypnIZnh_LabVjDb6-7iW3g_VqPLUayp8JDHfAzsN6Q7kxzjTLkMSfMNutP1ca07w")

        lugar = Lugar.objects.first()
        url = lugar.get_api_url()

        data = {"direccion": "Calle 29 # 11 - 123",
                "fecha_creacion": "2019-07-07",
                "tag": [{"nombre": "Test - Tag", "id": 1}],
                "telefono": ["3162830130"],
                "descripcion": "Tienda Palacios",
                "comentario": [],
                "nombre": "Tienda Palacios",
                "categoria": 1,
                "dias_servicio": ["LUN", "MAR", "MIE", "N", "VIE", "SAB", "N"],
                "municipio": "Buga",
                "email": ["oarp1996@hotmail.com"],
                "calificacion": 5,
                "departamento": "Valle del Cauca",
                "hora_abierto": ["06:00 a.m.", "06:00 a.m.", "06:00 a.m.", "N", "06:00 a.m.", "08:00 a.m.", "N"],
                "sitio_web": ["www.facebook.com/OscarRuiz15"],
                "latitud": 3.7036843,
                "propietario": 1,
                "longitud": -76.2940772,
                "hora_cerrado": ["22:00 p.m.", "22:00 p.m.", "22:00 p.m.", "N", "22:00 p.m.", "22:00 p.m.", "N"],
                "foto": ["gs:\/\/trabajo-de-grado-f9cb8.appspot.com\/lugares\/1\/slider-logo.png"],
                "redes": ["www.facebook.com", "www.twitter.com"]}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
