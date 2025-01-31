# Authentication System Using Django & Angular

## Project Overview

This is a simple yet effective authentication system built using **Django** for the backend and **Angular** for the frontend. It allows user registration, login, and identity verification using **JWT tokens** stored in cookies. Additionally, users can be deleted by clearing the authentication cookies.

---

## Features

- **User Registration:** New users can register with their information.
- **User Login:** Secure login system with JWT-based authentication.
- **Identity Verification:** JWT tokens are sent in cookies to verify user identity.
- **User Deletion:** Authentication cookies can be deleted to log out users.

---

## Tech Stack

- **Frontend:** Angular
- **Backend:** Django (Django REST Framework)
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** MySQL

---

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Node.js** & **npm**
- **Angular CLI**

### Backend Setup

1. Clone the project repository:

   ```bash
   git clone <repo-url>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the project dependencies:

   ```bash
   cd auth\
   pip install -r .requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python makemigrations.py migrate
   python manage.py migrate
   ```

5. Start the Django server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd angular-auth
   ```

2. Install Angular project dependencies:

   ```bash
   npm install
   ```

3. Start the Angular development server:

   ```bash
   ng serve
   ```

4. Open the app at [http://localhost:4200](http://localhost:4200).

---

## Usage

- **Register a User:** Navigate to the registration page and submit user details.
- **Login:** Enter credentials to log in and receive a JWT token.
- **Verify Identity:** The system uses the JWT token stored in cookies for secure verification.
- **Delete User:** Clear cookies to effectively log out and remove the user session.

---

## Project Structure

```
.
├── auth(backend)
│   ├── manage.py
│   ├── requirements.txt
│   ├── users/ # Django app with models, views, and serializers
│   └── auth/
└── angular-auth(frontend)
    ├── src/
    ├── angular.json
    └── package.json
```

## License

This project has no License.

---

## Acknowledgments

- Built with Django REST Framework & Angular.
- JWT implementation for secure authentication.
