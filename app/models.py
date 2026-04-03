from typing import Optional
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, timezone
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)

    username: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index = True, unique = True)

    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    # don't understand this line btw
    def set_password(self,  password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    #complains about password_hash can accept both none and str, but functions only wants to receive string
    
    expenses: so.WriteOnlyMapped['Expense'] = so.relationship(back_populates='author')

    # Here I understand that we're creating structure for our DB, giving what values
    # each column should contain, and restricting size of values 





@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


class Expense(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key= True)

    amount: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)

    category: so.Mapped[str] = so.mapped_column(sa.String(50), nullable=False)

    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(200))

    date: so.Mapped[datetime] = so.mapped_column(sa.DateTime, default=datetime.utcnow)

    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.id'), nullable=False)

    author: so.Mapped['User'] = so.relationship(back_populates='expenses')

#loader function