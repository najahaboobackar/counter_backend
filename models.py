from sqlalchemy import Column,ForeignKey,Integer,String
from database import Base

class Count(Base):
    __tablename__='counts'
    id=Column(Integer,primary_key=True,index=True)
    count=Column(Integer,index=True)
   