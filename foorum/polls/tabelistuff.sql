CREATE TABLE kusimused (
    id bit
    Pealkiri varvhar(70),
    Tekst varvhar(10)
    Postitatud datetime,
    Muudetud datetime
    Autor_id bit
);

BULK INSERT db.sqlite3.tbl_polls_questions
FROM '"C:\Users\raspe\Downloads\kusimused5.csv"
WITH
    (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
    FIRSTROW = 1
    )
GO