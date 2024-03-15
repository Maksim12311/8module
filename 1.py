from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create engine
engine = create_engine('sqlite:///database.db', echo=True)  # Change database URL as needed

# Create a base class for our ORM models
Base = declarative_base()

# Define User and Post classes
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='posts')

# Create tables in the database
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Define CRUD functions for User
def create_user(name):
    with Session() as session:
        user = User(name=name)
        session.add(user)
        session.commit()

def get_all_users():
    with Session() as session:
        return session.query(User).all()

def get_user_by_id(user_id):
    with Session() as session:
        return session.query(User).filter_by(id=user_id).first()

def delete_user(user_id):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()

# Define CRUD functions for Post
def create_post(title, content, user_id):
    with Session() as session:
        post = Post(title=title, content=content, user_id=user_id)
        session.add(post)
        session.commit()

def get_all_posts():
    with Session() as session:
        return session.query(Post).all()

def get_posts_by_user(user_id):
    with Session() as session:
        return session.query(Post).filter_by(user_id=user_id).all()

def get_post_by_id(post_id):
    with Session() as session:
        return session.query(Post).filter_by(id=post_id).first()

def delete_post(post_id):
    with Session() as session:
        post = session.query(Post).filter_by(id=post_id).first()
        if post:
            session.delete(post)
            session.commit()

# Example usage:
if __name__ == "__main__":
    create_user("John Doe")
    create_post("First Post", "This is my first post!", user_id=1)

    print(get_all_users())
    print(get_all_posts())
    print(get_posts_by_user(user_id=1))
    print(get_user_by_id(user_id=1))
    print(get_post_by_id(post_id=1))

    delete_post(post_id=1)
    delete_user(user_id=1)