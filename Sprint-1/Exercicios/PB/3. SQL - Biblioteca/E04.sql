SELECT 
    aut.codautor,
    aut.nome,
    aut.nascimento,
    COUNT(liv.cod) AS quantidade
FROM autor aut
LEFT JOIN livro liv ON aut.codautor = liv.autor
GROUP BY aut.codautor, aut.nome, aut.nascimento
ORDER BY aut.nome ASC;