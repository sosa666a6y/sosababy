USE Lib
GO
CREATE TRIGGER Debtors_DELETE
ON Debtors
AFTER DELETE
AS
INSERT INTO History (DebtorId, OperationName)
SELECT DebtorId, DebtorName + '  ��������� ������ �� �������� '
FROM DELETED