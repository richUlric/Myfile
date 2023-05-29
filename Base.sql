-- Création de la base de données
CREATE DATABASE ma_base_de_donnees;

-- Utilisation de la base de données
USE ma_base_de_donnees;

-- Création de la table d'utilisateurs
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

