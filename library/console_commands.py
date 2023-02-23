from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Book, Author, Publisher
from datetime import date

# Connect to the activities database
engine = create_engine('sqlite:///library.sqlite', echo=False)

# Create a session and add the people to the database
sess = Session(engine)
persons = sess.query(Person).all()
books = sess.query(Book).all()
authors = sess.query(Author).all()
publishers = sess.query(Publisher).all()

author = authors[1]
print(f'{author.author_name} wrote:')
for book in author.works:
    print(book.title)

books[2].authors.append(authors[0])
print(books[2].authors)

new_book = Book(title="Lord of the Rings",
                isbn='0008471282',
                num_pages=1248,
                publication_date=date(202,10,14),
                )
new_author = Author(author_name="J R R Tolkein")
new_book.authors.append(new_author)
new_book.publisher = publishers[2]

# sess.add(new_book)
# sess.commit()
sess.close()