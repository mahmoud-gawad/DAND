SELECT
  *
FROM
  city_data
WHERE
  country LIKE 'Eg%';

SELECT
  c.year,
  c.city,
  c.country,
  c.avg_temp AS local_avg_temp,
  g.avg_temp AS global_avg_temp
FROM
  city_data c
  JOIN global_data g ON g.year = c.year
WHERE
  c.city = 'Cairo'
  AND c.country = 'Egypt';
