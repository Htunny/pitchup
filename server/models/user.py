from server import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates, backref


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password_hash = db.Column(db.String())
    teams_created = db.relationship("Team", cascade="all,delete", backref="users")
    teams = db.relationship("Enrollment")

    def __init__(self, args):
        self.username = args['username']
        self.email = args['email']
        self.password_hash = args['password']

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Email address must contain an @ sign.')
        if self.query.filter_by(email=email).first() is not None:
            raise ValueError('Email already exists.')
        return email

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username cannot be empty.')
        if self.query.filter_by(username=username).first() is not None:
            raise ValueError('Username already exists.')
        return username

    @validates('password_hash')
    def validate_password(self, key, password_hash):
        if not password_hash:
            raise ValueError('Password cannot be empty.')
        if len(password_hash) < 6:
            raise ValueError('Password must be longer than 6 characters')
        return generate_password_hash(password_hash)

    def __repr__(self):
        return '<User {}>'.format(self.id)
