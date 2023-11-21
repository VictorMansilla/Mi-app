import sqlalchemy as bd
import persistence.model as mod

engine = bd.create_engine('sqlite:///C:\\Users\\User\\Desktop\\tarea\\PY\\Inicio de Sesion\\db\\login.sqlite', echo=True, future=True)
mod.base.metadata.create_all(engine)