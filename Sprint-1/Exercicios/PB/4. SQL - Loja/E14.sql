SELECT 
    t.estado, 
    ROUND(AVG(t.qtd * t.vrunt), 2) AS gastomedio
FROM 
    tbvendas t
WHERE 
    t.status = 'Concluído'
GROUP BY 
    t.estado
ORDER BY 
    gastomedio DESC;