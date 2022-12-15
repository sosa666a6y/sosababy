USE Lib
SELECT BookGiving.GivingDate, BookGiving.BookId, Books.BookName, Readers.LibraryCard, Readers.ReaderName
FROM BookGiving 
JOIN Books ON Books.BookId = BookGiving.BookId
JOIN Readers ON Readers.LibraryCard = BookGiving.LibraryCard