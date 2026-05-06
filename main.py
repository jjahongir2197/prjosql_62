from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_full.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    posts = db.relationship('Post', backref='user')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

with app.app_context():
    db.create_all()

    u1 = User(username="ali")
    p1 = Post(title="Hello", content="First post", user=u1)
    c1 = Comment(text="Nice!", post=p1)
    l1 = Like(user_id=1, post_id=1)

    db.session.add_all([u1, p1, c1, l1])
    db.session.commit()
