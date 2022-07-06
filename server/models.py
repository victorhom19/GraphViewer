from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Code(Base):
    __tablename__ = 'Code'
    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(50), nullable=False)
    code = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)

    def __repr__(self):
        return "<Code(%d, '%s','%s', %d)>" % (self.id, self.language, self.code, self.user_id)
