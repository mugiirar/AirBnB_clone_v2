#!/usr/bin/python3
"""DBStorage engine"""
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place

class DBStorage:
    """database storage engine."""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                              format(getenv("HBNB_MYSQL_USER"),
                                     getenv("HBNB_MYSQL_PWD"),
                                     getenv("HBNB_MYSQL_HOST"),
                                     getenv("HBNB_MYSQL_DB")),
                              pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session for objects of the given class.

        If cls is None, query all types of objects.

        Returns:
        Dictionary of queried classes in the format <class name>.<obj id> = obj.
        """
        query_classes = [State, City, User, Place, Review, Amenity]

        if cls is None:
            objs = []
            for query_class in query_classes:
                objs.extend(self.__session.query(query_class).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj current database session."""
            self.__session.add(obj)

    def save(self):
        """changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

