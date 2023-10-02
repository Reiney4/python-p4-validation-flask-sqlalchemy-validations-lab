from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    @validates("name") 
    def validate_name(self,key,address):
        if not address:
            raise ValueError("Author must have a name")
        return address
    @validates("phone_number")
    def validate_phone_number(self,key,address):
        if len(address)!=10:
            raise ValueError("phone number must be 10 digits")
        return address
class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    @validates("title")
    def validate_title(self, key, title):
       if not title:
          raise ValueError("Post must have a title")
       return title
    @validates("content")
    def validate_content(self, key, content):
       if content and len(content) < 250:
          raise ValueError("Post content must be at least 250 characters long")
       return content
    @validates("summary")
    def validate_summary(self, key, summary):
        if summary and len(summary) > 250:
          raise ValueError("Post summary cannot exceed 250 characters")
        return summary
    @validates("category")
    def validate_category(self, key, category):
        if category not in ["Fiction", "Non-Fiction"]:
          raise ValueError("Post category must be either 'Fiction' or 'Non-Fiction'")
        return category
    @validates("title")
    def validate_title(self, key, title):
        if "clickbait" in title.lower():
          raise ValueError("Title is considered clickbait")
        return title


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'