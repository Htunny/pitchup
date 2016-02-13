from server import db
from sqlalchemy.orm import validates
from server.helpers.sessions import current_user


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    capacity = db.Column(db.Integer())
    number_players = db.Column(db.Integer())
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, args):
        self.name = args['name']
        self.capacity = args['capacity']
        self.number_players = args['number_players']
        self.created_by = current_user().id

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Team name cannot be empty')
        return name

    @validates('capacity')
    def validate_capacity(self, key, capacity):
        if not capacity.isdigit():
            raise ValueError('Capacity must be a number')
        return capacity

    @validates('number_players')
    def validate_number_players(self, key, number_players):
        if not number_players.isdigit():
            raise ValueError('Number players must be a number')
        return number_players

# if number_players >= capacity:
#     raise ValueError('Number players must be less than capacity')

    #
    # @validates('username')
    # def validate_username(self, key, username):
    #     if not username:
    #         raise ValueError('Username cannot be empty.')
    #     if self.query.filter_by(username=username).first() is not None:
    #         raise ValueError('Username already exists.')
    #     return username
    #
    # @validates('password_hash')
    # def validate_password(self, key, password_hash):
    #     if not password_hash:
    #         raise ValueError('Password cannot be empty.')
    #     if len(password_hash) < 6:
    #         raise ValueError('Password must be longer than 6 characters')
    #     return generate_password_hash(password_hash)

    def __repr__(self):
        return '<Team {}>'.format(self.id)
