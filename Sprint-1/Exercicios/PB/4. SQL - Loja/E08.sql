SELECT v.cdvdd, v.nmvdd
FROM tbvendedor v
JOIN tbvendas t ON v.cdvdd = t.cdvdd
WHERE t.status = 'Concluído'
GROUP BY v.cdvdd, v.nmvdd
ORDER BY COUNT(t.cdvdd) DESC
LIMIT 1;