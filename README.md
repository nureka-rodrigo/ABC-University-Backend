# abc-university-backend

This project is a web application built using Django.
It's a student management system that allows students to view their profile,
update their profile and password, register for courses, and provide feedback.

This project is the backend part of the ABC University Student Management System.
The frontend part of the project is
available [here](https://github.com/nureka-rodrigo/abc-university-frontend).

## Features

- View student profile
- Update student profile
- Update student password
- Register for courses
- Provide feedback

## Environment Variables

The project uses the following environment variables, which are stored in a `.env` file:

- `DJANGO_SECRET_KEY`: The secret key for the Django application
- `DJANGO_DEBUG`: The debug mode for the Django application

## Installation

This project was bootstrapped with [Django](https://www.djangoproject.com/).

To set up and run this project locally,
you'll need to have [Python](https://www.python.org/),
[pip](https://pip.pypa.io/en/stable/) and [pipenv](https://pipenv.pypa.io/en/latest/) installed.
Follow these steps:

1. Clone the repository: `git clone https://github.com/nureka-rodrigo/abc-university-backend.git`
2. Navigate into the project directory: `cd abc-university-backend`
3. Install the dependencies: `pipenv install`
4. Activate the pipenv shell: `pipenv shell`
5. Start the application: `python manage.py runserver`

The application will start running on `http://localhost:8000`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the terms of
the [MIT license](https://github.com/nureka-rodrigo/abc-university-backend/blob/main/LICENSE).