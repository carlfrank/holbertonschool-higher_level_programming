-- Script to list records from a specific table in a MySQL database
-- with specific conditions and sorting.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;