-- list_databases.sql

-- Displays all databases ordered by name
SELECT schema_name AS Database
FROM information_schema.schemata
ORDER BY schema_name;
