from sqlalchemy import Column, Integer, String, Date, Boolean, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

book_author = Table("book_author",
                    Base.metadata,
                    Column('book_id', ForeignKey('book.book_id')),
                    Column('author_id', ForeignKey("author.author_id")),
                    UniqueConstraint('book_id', 'author_id')
                    )

book_loan = Table("book_loan",
                  Base.metadata,
                  Column('book_id', ForeignKey('book.book_id')),
                  Column('person_id', ForeignKey("person.person_id")),
                  UniqueConstraint('book_id', 'person_id')
                  )


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    isbn = Column(String, unique=True)
    num_pages = Column(Integer)
    publication_date = Column(Date)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))

    authors = relationship("Author",
                           secondary=book_author,
                           order_by='(Author.author_name)',
                           back_populates="works")

    borrowers = relationship("Person",
                             secondary=book_loan,
                             order_by='(Person.name)',
                             back_populates='on_loan')

    publisher = relationship("Publisher", back_populates="books")

    def __repr__(self):
        return f"Book(title='{self.title}',"  \
               f"isbn={self.isbn}), " \
               f"num_pages={self.num_pages}, " \
               f"publication_date={self.publication_date})"


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String)
    books = relationship("Book", back_populates="publisher")

    def __repr__(self):
        return f"Publisher(publisher_name='{self.publisher_name}')"


class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String)

    works = relationship("Book",
                         secondary=book_author,
                         order_by='(Book.title)',
                         back_populates="authors")

    def __repr__(self):
        return f"Author(author_name='{self.author_name}'))"


class Person(Base):
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    membership_expiry = Column(Boolean)

    on_loan = relationship("Book",
                           secondary=book_loan,
                           order_by='(Book.title)',
                           back_populates="borrowers")

    def __repr__(self):
        return f"Person(name='{self.name}')"
