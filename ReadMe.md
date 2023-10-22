### Project structure
```markdown

party_master_task
├── part_master
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_partymaster_gst_number_and_more.py
│   │   └── __init__.py
│   ├── templates
│   │   └── part_master
│   │       ├── party_form.html
│   │       └── party_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── party_master_task
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv
├── data.py
├── manage.py
├── ReadMe.md
├── requirements.txt
```

# Party Master API with Django and Mysql

This is a simple RESTful API for managing a Party Master API using Django and Mysql. 
It provides basic endpoints for adding, retrieving and storing in Database tasks.

## Getting Started

These instructions will help you set up and run the API on local machine.

### Prerequisites

- Python 3.x
- Django
- Mysql

### Installation

1. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have mysql running on your machine. 

3. Configure Mysql:
   -  Modify DATABASES directory it as needed to match your Mysql setup.

### Running the Application

1. Start the Django application:

   ```bash
   python manage.py runserver
   ```

2. The API should be accessible at `http://localhost:8000`.

## API Endpoints

- `party_list`: Retrieve a list of datas.
- `add_party`: Add a new data.
- `admin`: Shows Datasets on admin page data.

## Testing the API

You can test the API using tools like Postman. 

## Also check datasets by running following command

   ```bash
   python data.py 
   ```
