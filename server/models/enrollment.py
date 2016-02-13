from server import db
from sqlalchemy.orm import validates
from server.helpers.sessions import current_user


class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), primary_key=True)
    number_players = db.Column('number_players', db.Integer)
    team = db.relationship("Team")


    def __init__(self, args):
        self.team_id = args['team_id']
        self.user_id = current_user().id
        self.number_players = args['number_players']

    def __repr__(self):
        return '<Enrollment {}>'.format(self.id)
