from app import db

class Category(db.Model):
    """
    Create an Category table
    """

    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Category: {}>'.format(self.name)


class Product(db.Model):
    """
    Create an Product table
    """

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    price = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products',
                                                         lazy='dynamic'))

    def __repr__(self):
        return '<Product: {}>'.format(self.name)
