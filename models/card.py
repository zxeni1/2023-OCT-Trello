from init import db, ma 
from marshmallow import fields

class Card(db.model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.Date) # Date the card was created
    description = db.Column(db.Text)
    status = db.Column(db.String)
    priority = db.Column(db.String)


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates="cards")

    # {id: 1 title: Card 1, user_id: 2}

class CardSchema(ma.Schema): 

    user = fields.Nested('UserSchema', only = ['name', 'email'])

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'status', 'priority', 'user')

card_schema = CardSchema()
card_schema = CardSchema(many=True)
