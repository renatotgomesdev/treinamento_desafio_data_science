--create database desafio_data_science;
--use desafio_data_science;

CREATE TABLE produtos (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    quantidade INT NOT NULL,
    preco INT NOT NULL,
    PRIMARY KEY (id)
);
