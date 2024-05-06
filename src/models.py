import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship('Post', backref='category', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __init__(self, title, content, category_id, author_id):
        self.title = title
        self.content = content
        self.category_id = category_id
        self.author_id = author_id
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'category_id': self.category_id,
            'author_id': self.author_id
        }

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, content, post_id, author_id):
        self.content = content
        self.post_id = post_id
        self.author_id = author_id

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'post_id': self.post_id,
            'author_id': self.author_id
        }