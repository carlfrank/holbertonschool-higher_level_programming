-- Script to list the number of records with the same value in a column in a table in a MySQL database
-- and to sort the results.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;