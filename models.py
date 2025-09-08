from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    addresses: Mapped[list["Address"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_accounts.id"))  # 🔑 FIXED

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id}, email='{self.email}', user_id={self.user_id})"


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"
    
class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fee: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f"Courses(id={self.id}, name='{self.name}', fee={self.fee})"
    
class Enrollment(Base):
    __tablename__ = "enrollment"

    id: Mapped[int] = mapped_column(primary_key=True)
    c_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    s_id: Mapped[int] = mapped_column(ForeignKey("student.id"))
    date: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"Enrollment(s_id={self.s_id}, c_id={self.c_id}, date='{self.date}')"