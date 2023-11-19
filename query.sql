-- 1. Вивести назви категорій, власники яких живуть в United States
SELECT DISTINCT o.category_org
FROM Billionaire b
JOIN organization o ON b.name_org = o.name_org
JOIN country c ON b.name_country = c.name_country
WHERE c.name_country = 'United States';


-- 2. Вивести кількість мільярдерів за кожною країною
SELECT c.name_country, COUNT(*) AS billionaire_count
FROM Billionaire b
JOIN Country c ON b.name_country = c.name_country
GROUP BY c.name_country;

-- 3. Вивести координати країни мільярдера та його ім'я
SELECT b.firstname, b.lastname, c.latitude_country, c.longtitude_country
FROM Billionaire b
JOIN Country c ON b.name_country = c.name_country;
