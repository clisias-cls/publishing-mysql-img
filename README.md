# Repositório "publishing-mysql-img"
Repositório para publicação do container MySQL gerada no Docker no Github e de todos os componentes e documentos do projeto.
- Nome do Docker Container: cls-mysql

Objetos gerados no container:
- Database prova
- Tabela prova.microdados_2020 - Recebe os microdados do enem-2020 com as transformações necessárias para a análise de dados.
- Tabela prova.dim_escola - Dimensão de dados das escolas de origem dos participantes da prova do enem-2020.
- Tabela prova.dim_local_prova - Dimensão de dados dos locais onde as provas do enem-2020 foram ministradas.
- Tabela prova.dim_participante - Dimensão de dados pessoais dos participantes do enem-2020.
- Tabela prova.fato_prova - Tabela Fato com os dados das provas realizadas do enem-2020 por participante.
- Procedure prova.atualiza_modelo_prova - Lê os dados transformados da tabela prova.microdados_2020 e distribui na tabela Fato e nas Dimensões.

Modelo de Dados
- MODELO_ESTRELA_MICRODADOS_ENEM_2020.pdf - Desenho da modelagem (modelo estrela) para os microdados do Enem-2020.

Carga dos dados: Efetuada por scripts python.
- CARGA_MICRODADOS_ENEM.py - Efetua a carga da tabela prova.microdados_2020 realizando as transformações necessárias para a análise dos dados.
- CARGA_ENEM.py - Executa a proc prova.atualiza_modelo_prova após a carga inicial.

Arquivos SQL:
- MICRODADOS-2020.sql - Guarda o comando de criação da tabela prova.microdados_2020.
- MOD_ESTRELA.sql - Guarda os comandos de criação das tabelas Fato e Dimensão.
- ATUALIZA_MODELO_PROVA.sql - Guarda o código da procedure prova.atualiza_modelo_prova.

Modelagem de Dados:
- MODELO_ESTRELA_MICRODADOS_ENEM_2020.pdf - Modelagem estrela para os microdados do Enem-2020.

Arquivo Word:
- QUESTIONÁRIO - MICRODADOS ENEM-2020.docx - Respostas do questionário
