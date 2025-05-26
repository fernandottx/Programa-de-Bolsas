SELECT 
    aut.nome
FROM autor aut
LEFT JOIN livro liv ON aut.codautor = liv.autor
WHERE liv.cod IS NULL
ORDER BY aut.nome