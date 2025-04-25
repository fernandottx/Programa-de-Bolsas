SELECT DISTINCT 
    aut.nome
FROM autor aut
JOIN livro liv ON aut.codautor = liv.autor
JOIN editora edi ON liv.editora = edi.codeditora
JOIN endereco ende ON edi.endereco = ende.codendereco
WHERE ende.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY aut.nome
