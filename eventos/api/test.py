from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from eventos.models import Evento
from usuarios.models import Usuario
from categorias.models import Categoria
from lugares.models import Lugar
from tags.models import Tag
from comentarios.models import Comentario


class EventosAPITestCase(APITestCase):

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

        evento = Evento.objects.create(nombre="Test Evento",
                                       descripcion="Descripcion Evento",
                                       lugar=lugar,
                                       direccion="Direccion Test",
                                       foto="{ }",
                                       calificacion="1",
                                       tipo="Tipo Test",
                                       fecha_inicio="1996-08-14",
                                       fecha_fin="1996-08-15",
                                       hora_inicio="13:00:00",
                                       hora_fin="14:00:00",
                                       finalizado="f")

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

    def test_single_evento(self):
        eventos_count = Evento.objects.count()
        self.assertEqual(eventos_count, 1)

    #########################################################################
    def test_get_eventos_list_forbidden(self):
        data = {}
        url = api_reverse("api-eventos:evento-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #########################################################################
    def test_get_eventos_list_with_user_ok(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ1Nzk2NCwiZXhwIjoxNTQ4NDYxNTY0LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.v75f3olYx5wtqCCbJjO7rrpAhyrSwxIQUQShc7YYYJjPYkxpScM8Wo9KwJRmhsjhe8I9Y5xe1fKVroJGfo-TbfW4TQ8nXWo9uWLix7D9j6oj32tkz_kwc396kJXifQphRqtK4_8mjbFMP9cNt2pBn81YORY19o8G6rKaC8pOPAwJrsVk2--OcBOCYpQu_OfuCEUippRiGh2piPIkN6kQjeB675UD8xTfjblqKGFwt4vi2MNRurKsnmRdg3hZmvMpRO7q1dk3R2y4NYUoCw37alypnIZnh_LabVjDb6-7iW3g_VqPLUayp8JDHfAzsN6Q7kxzjTLkMSfMNutP1ca07w")
        data = {}
        url = api_reverse("api-eventos:evento-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #########################################################################
    def test_post_eventos_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ1Nzk2NCwiZXhwIjoxNTQ4NDYxNTY0LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.v75f3olYx5wtqCCbJjO7rrpAhyrSwxIQUQShc7YYYJjPYkxpScM8Wo9KwJRmhsjhe8I9Y5xe1fKVroJGfo-TbfW4TQ8nXWo9uWLix7D9j6oj32tkz_kwc396kJXifQphRqtK4_8mjbFMP9cNt2pBn81YORY19o8G6rKaC8pOPAwJrsVk2--OcBOCYpQu_OfuCEUippRiGh2piPIkN6kQjeB675UD8xTfjblqKGFwt4vi2MNRurKsnmRdg3hZmvMpRO7q1dk3R2y4NYUoCw37alypnIZnh_LabVjDb6-7iW3g_VqPLUayp8JDHfAzsN6Q7kxzjTLkMSfMNutP1ca07w")

        data = {"nombre": "Nombre Test",
                "descripcion": "Descripcion Test",
                "lugar": 1,
                "comentario": [],
                "direccion": "Direccion Test",
                "foto": ["gs:\/\/trabajo-de-grado-f9cb8.appspot.com\/lugares\/1\/slider-logo.png"],
                "calificacion": 2,
                "tipo": "Tipo Test",
                "fecha_inicio": "1996-08-10",
                "fecha_fin": "1996-08-20",
                "hora_inicio": "11:00:00",
                "hora_fin": "23:00:00",
                "finalizado": "t"}

        url = api_reverse("api-eventos:evento-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #########################################################################
    def test_put_eventos_with_user_admin(self):
        self.client.credentials(
            HTTP_AUTHORIZATION="eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1OWE2NDFhMWI4MmNjM2I1MGE4MDFiZjUwNjQwZjM4MjU3ZDEyOTkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdHJhYmFqby1kZS1ncmFkby1mOWNiOCIsImF1ZCI6InRyYWJham8tZGUtZ3JhZG8tZjljYjgiLCJhdXRoX3RpbWUiOjE1NDczOTgzMTMsInVzZXJfaWQiOiJEcTJoQUZyamp3VFIwU2VHclRwS204anI5RXExIiwic3ViIjoiRHEyaEFGcmpqd1RSMFNlR3JUcEttOGpyOUVxMSIsImlhdCI6MTU0ODQ1Nzk2NCwiZXhwIjoxNTQ4NDYxNTY0LCJlbWFpbCI6ImFuZHJlc2NoZXNzMjAwOUBob3RtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhbmRyZXNjaGVzczIwMDlAaG90bWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.v75f3olYx5wtqCCbJjO7rrpAhyrSwxIQUQShc7YYYJjPYkxpScM8Wo9KwJRmhsjhe8I9Y5xe1fKVroJGfo-TbfW4TQ8nXWo9uWLix7D9j6oj32tkz_kwc396kJXifQphRqtK4_8mjbFMP9cNt2pBn81YORY19o8G6rKaC8pOPAwJrsVk2--OcBOCYpQu_OfuCEUippRiGh2piPIkN6kQjeB675UD8xTfjblqKGFwt4vi2MNRurKsnmRdg3hZmvMpRO7q1dk3R2y4NYUoCw37alypnIZnh_LabVjDb6-7iW3g_VqPLUayp8JDHfAzsN6Q7kxzjTLkMSfMNutP1ca07w")

        eventos = Evento.objects.first()
        url = eventos.get_api_url()

        data = {"nombre": "Nombre Test x2",
                "descripcion": "Descripcion Test x2",
                "lugar": 1,
                "comentario": [],
                "direccion": "Direccion Test x2",
                "foto": ["sinfoto"],
                "calificacion": 5,
                "tipo": "Tipo Test x2",
                "fecha_inicio": "2006-08-10",
                "fecha_fin": "2006-08-20",
                "hora_inicio": "11:01:00",
                "hora_fin": "23:00:20",
                "finalizado": "f"}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
