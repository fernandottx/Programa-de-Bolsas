SELECT 
    v.nmvdd AS vendedor,
    SUM(t.qtd * t.vrunt) AS valor_total_vendas,
    ROUND((SUM(t.qtd * t.vrunt) * v.perccomissao)/100,2) AS comissao
FROM 
    tbvendas t
JOIN 
    tbvendedor v ON t.cdvdd = v.cdvdd
WHERE 
    t.status = 'Concluído'
GROUP BY 
    v.cdvdd, v.nmvdd, v.perccomissao
ORDER BY 
    comissao DESC
