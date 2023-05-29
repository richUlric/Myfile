<?php
// Récupérer les valeurs des champs de formulaire
$nom_utilisateur = $_POST["nom_utilisateur"];
$mot_de_passe = $_POST["mot_de_passe"];

// Établir une connexion à la base de données
$mysqli = new mysqli("localhost", "root", "", "parking");

// Vérifier la connexion
if ($mysqli->connect_error) {
    die("Erreur de connexion à la base de données : " . $mysqli->connect_error);
}

// Préparer la requête d'insertion
$stmt = $mysqli->prepare("INSERT INTO utilisateur (nom_utilisateur, mot_de_passe) VALUES (?, ?)");
$stmt->bind_param("ss", $nom_utilisateur, $mot_de_passe);

// Exécuter la requête d'insertion
if ($stmt->execute()) {
    echo "Enregistrement réussi.";
} else {
    echo "Erreur lors de l'enregistrement : " . $stmt->error;
}

// Fermer la connexion
$stmt->close();
$mysqli->close();
?>

