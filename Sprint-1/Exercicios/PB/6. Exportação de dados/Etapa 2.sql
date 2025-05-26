SELECT 
    COUNT(liv.cod) AS quantidade,
    edi.nome,
    end.estado,
    end.cidade
FROM 
    livro liv
JOIN 
    editora edi ON liv.editora = edi.codeditora
JOIN 
    endereco end ON edi.endereco = end.codendereco
GROUP BY 
    edi.nome, end.estado, end.cidade
ORDER BY 
    quantidade DESC
LIMIT 5;