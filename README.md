Consulta de Filmes – API com FastAPI

  Este projeto foi desenvolvido para permitir que o usuário pesquise um filme pelo nome e receba informações básicas sobre ele:
título, ano e sinopse. A busca é feita usando a API pública OMDb, e tudo é devolvido em formato JSON de forma simples e direta.
A ideia é mostrar como criar um serviço REST pequeno, organizado e funcional, consultando uma API externa e retornando só o que realmente importa.

O que esse sistema faz

  Recebe o nome de um filme
Consulta a OMDb pra pegar os dados
Retorna apenas:
  titulo
  ano
  sinopse
Tudo isso por meio de um endpoint /filme
Simples, limpo e seguindo exatamente o que o enunciado pede.
