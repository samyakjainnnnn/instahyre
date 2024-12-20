from api.models import User, Contact
from django.contrib.auth.hashers import make_password

users = [
    {'username': 'samyak1', 'phone_number': '123450', 'email': 'samyakjain67890@gmail.com', 'password': make_password('password0')},
    {'username': 'mumma1', 'phone_number': '1234560', 'email': 'mumma@gmail.com', 'password': make_password('password10')},
    {'username': 'papa1', 'phone_number': '12345670', 'email': 'papa@gmail.com', 'password': make_password('password20')},
    {'username': 'anjana1', 'phone_number': '123451', 'email': 'z8n4okd-94vvinjru0i2xwld0gqgh0rbfzko@reply.instahyre.com', 'password': make_password('password1')},
    {'username': 'user51', 'phone_number': '1234580', 'email': 'user5@example.com', 'password': make_password('password5')},
    {'username': 'user61', 'phone_number': '1234590', 'email': 'user6@example.com', 'password': make_password('password6')}
]

for user_data in users:
    user = User.objects.create(**user_data)
    for i in range(5):
        Contact.objects.create(user=user, name=f'contact{i}', phone_number=f'{user.phone_number}{i}', is_spam=(i % 2 == 0))
