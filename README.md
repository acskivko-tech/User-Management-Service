# User-Management-Service

The User Management Service is a backend-only REST API for managing user accounts, authentication, and access control. Built with Django and Django REST Framework (DRF), it includes automatic Swagger API documentation, offering an interactive interface to test endpoints directly in the browser.

---

## Features

- User registration and authentication
- Update current user profile
- Admin can view and update any user
- Role-based access control (admin vs regular user)
- Custom Django admin interface for managing users
- Automatic API documentation with Swagger

---

## Models

### UserModel
- `username`, `email`, `first_name`, `last_name`
- `phone_number` (default: "000-000-0000")
- `city` (default: "world")
- `status` (ForeignKey to Status model)

### Status
- `status_name` — User status (e.g., active, inactive)

---

## API Endpoints

### User Endpoints

- **Register user**  
  `POST /api/user/create/`  
  Creates a new user account. Passwords are hashed automatically. Optional fields like `city` and `phone_number` can be set.

- **Update current user profile**  
  `PUT /api/user/update/current`  
  Allows the logged-in user to update their own information.

- **Get current user info**  
  `GET /api/user/current/`  
  Returns the profile of the currently authenticated user.

- **Update user by ID (admin only)**  
  `PUT /api/user/update/<id>/`  
  Admins can update any user’s profile.

- **Get user by ID (admin only)**  
  `GET /api/user/<id>/`  
  Admins can view any user's profile.

- **List all users**  
  `GET /api/users/list`  
  Returns a list of all users (admin access recommended).

---

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repo-url>
cd User-Management-Service