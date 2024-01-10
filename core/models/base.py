from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import MetaData


metadata = MetaData()

class Base(DeclarativeBase):
   __abstract__ = True

   @declared_attr.directive
   def __tablename__(cls) -> str:
      return cls.__name__.lower()
   
   # @declared_attr
   # def foo(cls) -> Mapped["Model"]:
   #    return rel


   id: Mapped[int] = mapped_column(primary_key=True)
   created_at: Mapped[datetime] = mapped_column(
      default=datetime.utcnow(), 
      # server_default=datetime.utcnow()
   )
