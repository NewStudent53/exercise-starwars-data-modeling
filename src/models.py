import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(DateTime, nullable=False)
    favoritos = relationship('Favorito', back_populates='usuario')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(500))
    favoritos = relationship('Favorito', back_populates='personaje')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250))
    terreno = Column(String(250))
    favoritos = relationship('Favorito', back_populates='planeta')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
