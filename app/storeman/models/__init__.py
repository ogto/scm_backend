from app import db

def get_class_by_tablename(tablename):
    for c in db.Model._decl_class_registry.values():
        if hasattr(c, '__tablename__'):
            if c.__tablename__ == tablename:
                return c
