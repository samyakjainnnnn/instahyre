
### What This Covers:

- **Setup and Installation**:
  - Cloning the repository.
  - Creating a virtual environment.
  python -m venv venv
  source venv/bin/activate  
  - Installing dependencies.
  pip install -r requirements.txt
  - Running migrations.
  python manage.py makemigrations api python manage.py migrate
  - Creating a superuser.
  python manage.py createsuperuser
  - Populating the database.
  python manage.py shell < populate_data.py
  - Starting the development server.
  python manage.py runserver


- **Accessing the API**:
 http://127.0.0.1:8000/api/

- **API Endpoints**:
/api/token/: Obtain JWT token.
/api/token/refresh/: Refresh JWT token.
/api/users/: User registration and list.
/api/contacts/: Contact list and create.
/api/contacts/{id}/mark_as_spam/: Mark contact as spam.
/api/search/users/: Search users by name or phone number.
/api/search/contacts/: Search contacts by name or phone number.

- **Testing**:
  python manage.py test api

