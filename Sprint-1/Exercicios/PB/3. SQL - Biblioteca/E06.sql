SELECT 
    aut.codautor,
    aut.nome,
    COUNT(liv.cod) AS quantidade_publicacoes
FROM autor aut
JOIN livro liv ON aut.codautor = liv.autor
GROUP BY aut.codautor, aut.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1
