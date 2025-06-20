### README.md

```markdown
# 🔐 Authentication System with Role-Based Access Control (RBAC)

## 📌 Objective
Build a secure backend API for user authentication and role-based access control using JWT.

## 🧰 Tech Stack
- Python + Flask
- SQLite (can switch to PostgreSQL easily)
- JWT (via flask-jwt-extended)
- Password hashing with Bcrypt

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/spraveen18/Authentication_RBAC.git
cd Authentication_RBAC
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file:
```env
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey123

cp .env.example .env
# Then edit the .env file with your own keys
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey123
```

### 4. Seed database with sample users
```bash
python seed.py
```

### 5. Run the application
```bash
python app.py
```

Flask server will start on: `http://127.0.0.1:5000` or Codespace URL.

## 🔍 API Endpoints

| Method | Endpoint             | Description                       | Auth         |
|--------|----------------------|-----------------------------------|--------------|
| GET    | `/health`            | Health check                      | ❌ No         |
| POST   | `/api/register`      | Register new user                 | ❌ No         |
| POST   | `/api/login`         | Login and get JWT token           | ❌ No         |
| GET    | `/api/profile`       | Get logged-in user's profile      | ✅ JWT token  |
| GET    | `/api/admin/users`   | List all users (Admin only)       | ✅ Admin only |

## 📬 Postman Docs (API Testing)

### 1. Health Check
**GET** `http://localhost:5000/health`
- ✅ No authentication required

### 2. Register a User
**POST** `/api/register`
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "role": "Admin"
}
```

### 3. Login
**POST** `/api/login`
```json
{
  "email": "john@example.com",
  "password": "password123"
}
```
✅ Response includes `access_token`

### 4. Get Profile (Protected)
**GET** `/api/profile`
- Header:
```
Authorization: Bearer <access_token>
```

### 5. Admin – Get All Users
**GET** `/api/admin/users`
- Header:
```
Authorization: Bearer <admin_access_token>
```

## 👥 Sample Seeded Users
Run `python seed.py` to create them.

| Email               | Password      | Role  |
|---------------------|---------------|-------|
| admin1@example.com  | admin1pass    | Admin |
| legal2@example.com  | legal2pass    | Legal |
| pm3@example.com     | pm3pass       | PM    |
| sales4@example.com  | sales4pass    | Sales |
| admin5@example.com  | admin5pass    | Admin |
| ...                 | ...           | ...   |

## 🧪 Testing Tools
- ✅ Use **Postman** or **curl**
- 🔄 Optional: Swagger UI integration (`/apidocs`) [can be added]

---
```