# Django Blog Application

This is a simple blog application built with Django. It allows users to register, log in, create, update, and delete blog posts. 

## Features

- User registration and authentication
- Create, read, update, and delete posts
- User profile management

## Requirements

- Python 3.11
- Django 5.0.6

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/yourrepository.git
    ```
    ```
    cd yourrepository
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    ```
    ```
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

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

6. Start the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000/` to see the blog home page.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage users and posts.

## Project Structure

- `blog/`: Contains the blog application code.
- `users/`: Contains the user management application code.
- `templates/`: Contains the HTML templates.
- `static/`: Contains the static files (CSS, JavaScript, images).
- `app/`: Main project settings and URLs.

## Deployment with Docker

1. Build the Docker image:

    ```sh
    docker build -t django-blog .
    ```

2. Run the Docker container:

    ```sh
    docker run -d -p 8000:8000 django-blog
    ```

## Troubleshooting

- **404 Errors for URLs:** Ensure your URL patterns are correct and that the names match in the templates.
- **Form Errors:** Make sure all required fields are present in your forms and models.

## Contact

For any questions or issues, please open an issue on the repository or contact the maintainer at [mail2kaifkhan@gmail.com](mailto:mail2kaifkhan@gmail.com).
