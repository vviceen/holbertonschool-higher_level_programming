-- scrpt that list the number of records with same score in the table
SELECT score, COUNT(*) 'number' FROM second_table GROUP BY score ORDER BY score DESC;