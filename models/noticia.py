from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class BronzeNoticia(Base):
    __tablename__ = 'brz_noticias'

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    veiculo: Mapped[str] = mapped_column(String)
    titulo: Mapped[str] = mapped_column(String)
    subtitulo: Mapped[str] = mapped_column(String)
    materia: Mapped[str] = mapped_column(String)
    data_publicacao: Mapped[datetime] = mapped_column(DateTime)
    link: Mapped[str] = mapped_column(String, unique = True)
    categoria: Mapped[str] = mapped_column(String)
    hash: Mapped[str] = mapped_column(String, unique = True)

    def __repr__(self):
        return f'<Noticia Bronze(titulo="{self.titulo}", veiculo="{self.veiculo}")>'

class SilverNoticia(Base):
    __tablename__ = 'slv_noticias'

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    veiculo: Mapped[str] = mapped_column(String)
    titulo: Mapped[str] = mapped_column(String)
    subtitulo: Mapped[str] = mapped_column(String)
    materia: Mapped[str] = mapped_column(String)
    data_publicacao: Mapped[datetime] = mapped_column(DateTime)
    link: Mapped[str] = mapped_column(String, unique = True)
    categoria: Mapped[str] = mapped_column(String)
    hash: Mapped[str] = mapped_column(String, unique = True)

    def __repr__(self):
        return f'<Noticia Prata(titulo="{self.titulo}", veiculo="{self.veiculo}")>'

class GoldNoticia(Base):
    __tablename__ = 'gld_noticias'

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    veiculo: Mapped[str] = mapped_column(String)
    titulo: Mapped[str] = mapped_column(String)
    materia: Mapped[str] = mapped_column(String)
    data_publicacao: Mapped[datetime] = mapped_column(DateTime)
    link: Mapped[str] = mapped_column(String, unique = True)
    categoria: Mapped[str] = mapped_column(String)
    hash: Mapped[str] = mapped_column(String, unique = True)
    embedding: Mapped[str] = mapped_column(String)
    resumo: Mapped[str] = mapped_column(String)
    tags: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f'<Noticia Gold(titulo="{self.titulo}", veiculo="{self.veiculo}">'
