# Event Registration System

This is a Django-based web application for managing event registrations. Users can view upcoming events, register for events, and manage their registrations.

## Features

- User authentication (login, registration)
- Event listing with search functionality
- Event registration and unregistration
- User dashboard to view registered events
- Admin interface for managing events

## Project Structure
```
/ (root)
|   .gitignore
|   db.sqlite3
|   manage.py
|   README.md
|
+---events
|   |   admin.py
|   |   apps.py
|   |   forms.py
|   |   models.py
|   |   tests.py
|   |   urls.py
|   |   views.py
|   |   __init__.py
|   |
|   +---migrations
|   |   |   0001_initial.py
|   |   |   __init__.py
|   |
|   +---templates
|   |   +---events
|   |   |       base.html
|   |   |       event_detail.html
|   |   |       event_list.html
|   |   |       user_dashboard.html
|   |   |
|   |   \---registration
|   |           login.html
|   |           register.html
|   |
|   +---templatetags
|   |   |   form_filters.py
|   |   |   __init__.py
|   |
|   \---__pycache__ (removed)
|
\---event_registration
    |   asgi.py
    |   settings.py
    |   urls.py
    |   wsgi.py
    |   __init__.py
    |
    \---__pycache__ (removed)

```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/event_registration_system.git
    cd event_registration_system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/Scripts/activate  # On Windows
    source env/bin/activate      # On macOS/Linux
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) to access the application.

## Usage

- **Event Listing**: View upcoming events and search for specific events.
- **Event Registration**: Register for events if you are logged in.
- **User Dashboard**: View and manage your registered events.
- **Admin Interface** (Django built-in): Manage events through the Django admin interface.

