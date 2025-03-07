CREATE PROCEDURE prova.atualiza_modelo_prova()
BEGIN

/* CARGA DA DIM_ESCOLA*/

   INSERT INTO prova.dim_escola
   SELECT DISTINCT CO_MUNICIPIO_ESC, NO_MUNICIPIO_ESC, CO_UF_ESC, SG_UF_ESC,
                   TP_DEPENDENCIA_ADM_ESC, TP_LOCALIZACAO_ESC, TP_SIT_FUNC_ESC
   FROM prova.microdados_2020
   where CO_MUNICIPIO_ESC IS NOT NULL;

/* CARGA DA DIM_LOCAL_PROVA*/

   INSERT INTO prova.dim_local_prova
   SELECT DISTINCT CO_MUNICIPIO_PROVA, NO_MUNICIPIO_PROVA, CO_UF_PROVA, SG_UF_PROVA
   FROM prova.microdados_2020;

/* CARGA DA DIM_PARTICIPANTE*/

   INSERT INTO prova.dim_participante
   SELECT NU_INSCRICAO, NU_ANO, TP_FAIXA_ETARIA, TP_SEXO, TP_ESTADO_CIVIL, TP_COR_RACA,
          TP_NACIONALIDADE, TP_ST_CONCLUSAO, TP_ANO_CONCLUIU, TP_ESCOLA, TP_ENSINO, IN_TREINEIRO,
          TP_LINGUA, Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q008, Q009, Q010,
          Q011, Q012, Q013, Q014, Q015, Q016, Q017, Q018, Q019, Q020, Q021, Q022,
          Q023, Q024, Q025
   FROM prova.microdados_2020;

/* CARGA DA FATO_PROVA*/

   INSERT INTO prova.fato_prova
   SELECT NU_INSCRICAO, CO_MUNICIPIO_ESC,TP_DEPENDENCIA_ADM_ESC, TP_LOCALIZACAO_ESC,
          TP_SIT_FUNC_ESC, CO_MUNICIPIO_PROVA, TP_PRESENCA_CN, TP_PRESENCA_CH,
          TP_PRESENCA_LC, TP_PRESENCA_MT, CO_PROVA_CN, CO_PROVA_CH, CO_PROVA_LC, CO_PROVA_MT,
          NU_NOTA_CN, NU_NOTA_CH, NU_NOTA_LC, NU_NOTA_MT, TX_RESPOSTAS_CN, TX_RESPOSTAS_CH,
          TX_RESPOSTAS_LC, TX_RESPOSTAS_MT, TX_GABARITO_CN, TX_GABARITO_CH, TX_GABARITO_LC,
          TX_GABARITO_MT, TP_STATUS_REDACAO, NU_NOTA_COMP1, NU_NOTA_COMP2, NU_NOTA_COMP3,
          NU_NOTA_COMP4, NU_NOTA_COMP5, NU_NOTA_REDACAO
   FROM prova.microdados_2020;

   COMMIT;

END;