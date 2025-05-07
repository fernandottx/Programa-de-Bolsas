SELECT 
    t.estado, 
    t.nmpro AS nmpro, 
    ROUND(AVG(t.qtd), 4) AS quantidade_media
FROM 
    tbvendas t
JOIN 
    tbestoqueproduto p ON t.cdpro = p.cdpro
WHERE 
    t.status = 'Concluído'
GROUP BY 
    t.estado, t.nmpro
ORDER BY 
    t.estado, t.nmpro