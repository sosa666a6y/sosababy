USE Lib 
CREATE TABLE History (
Id INT IDENTITY (1, 1) PRIMARY KEY,
BookId INT NOT NULL,
OperationName NVARCHAR (150) NOT NULL,
CreateAt DATETIME NOT NULL DEFAULT GETDATE()
)