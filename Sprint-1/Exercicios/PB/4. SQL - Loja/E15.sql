SELECT 
    t.cdven
FROM 
    tbvendas t
WHERE 
    t.deletado = '1'
ORDER BY 
    t.cdven;