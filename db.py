from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# implement database model classes

association_table_category = db.Table(
    "association_category",
    db.Model.metadata,
    db.Column("article_id", db.Integer, db.ForeignKey("article.id")),
    db.Column("category_id", db.Integer, db.ForeignKey("category.id"))
)

association_table_citation = db.Table(
    "association_citation",
    db.Model.metadata,
    db.Column("article_id", db.Integer, db.ForeignKey("article.id")),
    db.Column("citation_id", db.Integer, db.ForeignKey("citation.id"))
)

association_table_user = db.Table(
    "association_user",
    db.Model.metadata,
    db.Column("article_id", db.Integer, db.ForeignKey("article.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable = False)
    comments = db.relationship("Comment", cascade = "delete")
    categories = db.relationship("Category", secondary = association_table_category, back_populates = "articles")
    citations = db.relationship("Citation", secondary = association_table_citation, back_populates = "articles")
    users = db.relationship("User", secondary = association_table_user, back_populates = "articles")

    def __init__(self, **kwargs):
        self.description = kwargs.get("description")

    def serialize(self):
        return {
            "id" : self.id,
            "description" : self.description,
            "comments": [s.serialize() for s in self.comments],
            "categories": [c.sub_serialize() for c in self.categories],
            "citations": [c.sub_serialize() for c in self.citations],
            "followers" :[c.sub_serialize() for c in self.users],
        }

    def sub_serialize(self):
        return {
            "id" : self.id,
            "description" : self.description,
            "comments": [s.serialize() for s in self.comments],
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    articles = db.relationship(
        "Article", secondary = association_table_user, back_populates = "users"
    )

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")

    def serialize(self):
        return {
            "id" : self.id, 
            "username": self.username,
            "following articles": [t.serialize() for t in self.articles],
        }

    def sub_serialize(self):
        return {
            "id" : self.id,
            "username" : self.username,
        }


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable = False)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))

    def __init__(self, **kwargs):
        self.description = kwargs.get("description")
        self.article_id = kwargs.get("article_id")

    def serialize(self):
        return {
            "id" : self.id,
            "description": self.description,
            "article_id" : self.article_id,
        }

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String, nullable = False)
    articles = db.relationship(
        "Article", secondary = association_table_category, back_populates = "categories"
    )

    def __init__(self, **kwargs):
        self.description = kwargs.get("description")

    def serialize(self):
        return {
            "id": self.id,
            "description":self.description,
            "articles": [t.serialize() for t in self.articles],
        }

    def sub_serialize(self):
        return {
            "id": self.id,
            "description":self.description,
        }

class Citation(db.Model):
    __tablename__ = 'citation'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    articles = db.relationship(
        "Article", secondary = association_table_citation, back_populates = "citations"
    )

    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.author = kwargs.get("author")

    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "articles": [t.serialize() for t in self.articles],
        }

    def sub_serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "author": self.author,
        }
