-- Displays all databases
SELECT schema_name AS `Database`
FROM information_schema.schemata
ORDER BY schema_name;
