-- A scripts that will list only rows with name value:
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
