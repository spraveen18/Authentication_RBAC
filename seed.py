from extensions import db
from models import User
from app import app

sample_users = []
roles = ["Admin", "Legal", "PM", "Sales"]

for i in range(1, 21):
    role = roles[i % len(roles)]
    sample_users.append({
        "name": f"{role} User {i}",
        "email": f"{role.lower()}{i}@example.com",
        "password": f"{role.lower()}{i}pass",
        "role": role
    })

with app.app_context():
    for user_data in sample_users:
        if not User.query.filter_by(email=user_data['email']).first():
            user = User(
                name=user_data['name'],
                email=user_data['email'],
                role=user_data['role']
            )
            user.set_password(user_data['password'])
            db.session.add(user)
    db.session.commit()
    print("Seeded users.")