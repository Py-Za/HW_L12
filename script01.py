from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost:3306/homework_1"
)
connection = engine.connect()

Base = declarative_base()


class Cat(Base):
    __tablename__ = "pussies"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
    colour = Column(Enum("calico", "black", "piss yellow" "other"))

    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add(Cat("Koperek", 12, "calico"))

session.commit()
session.close()
