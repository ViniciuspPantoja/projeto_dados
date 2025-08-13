CREATE TABLE organizacao_dados (
    "organizacao" TEXT,
    "nome" TEXT,
    "descricao" TEXT,
    "tags" TEXT,
    "quantidade_recursos" TEXT,
    "quantidade_reusos" TEXT,
    "quantidade_downloads" TEXT,
    "quantidade_seguidores" TEXT,
     data_criacao timestamp without time zone not null default (current_timestamp at time zone 'utc')
);