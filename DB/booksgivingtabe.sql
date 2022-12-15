USE Lib
CREATE TABLE BookGiving (
GivingId INT PRIMARY KEY IDENTITY (1, 1) NOT NULL,
BookId INT NOT NULL,
GivingDate SmallDateTime NOT NULL,
GettingDate SmallDateTime NOT NULL,
LibraryCard INT NOT NULL,
CONSTRAINT FK_Giving_To_Books FOREIGN KEY (BookId) REFERENCES Books (BookId),
CONSTRAINT FK_Giving_To_Readers FOREIGN KEY (LibraryCard) REFERENCES Readers (LibraryCard))