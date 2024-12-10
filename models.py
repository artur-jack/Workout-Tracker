from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Workout(Base):
    __tablename__ = 'workouts'
    
    id = Column(Integer, primary_key=True)
    day_of_week = Column(String, nullable=False)
    name = Column(String, nullable=False)
    exercises = relationship("Exercise", back_populates="workout", cascade="all, delete-orphan")

class Exercise(Base):
    __tablename__ = 'exercises'
    
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=False)
    reps = Column(Integer, nullable=False)
    current_weight = Column(Float)
    pr_weight = Column(Float)
    workout = relationship("Workout", back_populates="exercises")

# Criar banco de dados
engine = create_engine('sqlite:///workouts.db')
Base.metadata.create_all(engine)

# Criar sessão
Session = sessionmaker(bind=engine)
session = Session()
