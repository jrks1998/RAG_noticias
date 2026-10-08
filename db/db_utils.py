from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from models.noticia import Base, BronzeNoticia, SilverNoticia, GoldNoticia

engine = create_engine('sqlite:///db/noticias.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)

def get_session():
    return Session()

def salvar_noticia_bronze(noticia: BronzeNoticia):
    with get_session() as db_session:
        try:
            db_session.add(noticia)
            db_session.commit()
            print(f'noticia bronze {noticia.titulo} do veiculo {noticia.veiculo} foi salva')
            return noticia
        except IntegrityError:
            db_session.rollback()
            return None
        except Exception as e:
            db_session.rollback()
            print('erro ao salvar noticia:', e)
            raise
        finally:
            db_session.close()

def listar_noticias_bronze():
        db_session = get_session()
        return db_session.query(BronzeNoticia).all()

def salvar_noticia_silver(noticia: SilverNoticia):
    with get_session() as db_session:
        try:
            db_session.add(noticia)
            db_session.commit()
            print(f'noticia silver {noticia.titulo} do veiculo {noticia.veiculo} foi salva')
        except Exception as e:
            db_session.rollback()
            print('erro ao salvar noticia:', e)
        finally:
            db_session.close()

def listar_noticias_silver():
    db_session = get_session()
    return db_session.query(SilverNoticia).all()

def salvar_noticia_gold(noticia: SilverNoticia):
    with get_session() as db_session:
        try:
            db_session.add(noticia)
            db_session.commit()
            print(f'noticia gold {noticia.titulo} do veiculo {noticia.veiculo} foi salva')
        except Exception as e:
            db_session.rollback()
            print('erro ao salvar noticia:', e)
        finally:
            db_session.close()

def listar_noticias_gold():
    db_session = get_session()
    return db_session.query(GoldNoticia).all()
