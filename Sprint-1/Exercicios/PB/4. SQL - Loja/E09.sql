SELECT v.cdpro, t.nmpro
FROM tbvendas t
JOIN tbestoqueproduto v ON t.cdpro = v.cdpro
WHERE t.status = 'Concluído'
  AND t.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY v.cdpro, v.qtdpro
ORDER BY SUM(v.qtdpro) DESC
LIMIT 1;