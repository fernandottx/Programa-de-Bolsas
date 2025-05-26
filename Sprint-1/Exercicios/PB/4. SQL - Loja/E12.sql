WITH VendasPorVendedor AS (
    SELECT 
        cdvdd, 
        SUM(qtd * vrunt) AS valor_total_vendas
    FROM tbvendas
    WHERE status = 'Concluído'
    GROUP BY cdvdd
    HAVING SUM(qtd * vrunt) > 0
    ORDER BY valor_total_vendas
    LIMIT 1
)
SELECT 
    d.cddep, 
    d.nmdep, 
    d.dtnasc, 
    v.valor_total_vendas
FROM tbdependente d
JOIN VendasPorVendedor v ON d.cdvdd = v.cdvdd;