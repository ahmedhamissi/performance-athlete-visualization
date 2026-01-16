import turtle
import csv

def validation_csv_file(fichier):
    
    with open('D:/devoir/performance_athlete.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        
        for line_num, ligne in enumerate(reader, start=2):  
            
            if len(ligne) != 2:
                raise ValueError(f"Ligne {line_num}: Chaque ligne doit contenir exactement deux valeurs séparées par une virgule.")
            
            try:
                temps, distance = map(float, ligne)
            except ValueError:
                raise ValueError(f"Ligne {line_num}: Les valeurs doivent être des nombres valides.")
            
            if temps < 0 or distance < 0:
                raise ValueError(f"Ligne {line_num}: Les valeurs doivent être positives (temps={temps}, distance={distance}).")



# 1️ Charger les données depuis un fichier CSV
def lire_donnees_csv(fichier):
    """Lit un fichier CSV contenant temps et distance"""
    donnees = []
    validation_csv_file(fichier)
    with open('D:/devoir/performance_athlete.csv', 'r') as f:
        lecteur = csv.reader(f)
        next(lecteur)  # Ignorer l'en-tête
        for ligne in lecteur: 
            temps, distance = map(float, ligne)  # Convertir en nombres
            donnees.append((temps, distance))
    return donnees

# 2️ Calculer vitesse et accélération
def calculer_performance(donnees):
    """Calcule la vitesse et l’accélération à chaque instant"""
    performances = []
    
    for i in range(1, len(donnees)):
        t1, d1 = donnees[i - 1]
        t2, d2 = donnees[i]

        vitesse = (d2 - d1) / (t2 - t1)  # Δd / Δt
        acceleration = 0

        if i > 1:  # Pour calculer l’accélération à partir de la 2e itération
            v1 = performances[-1][1]  # Vitesse précédente
            acceleration = (vitesse - v1) / (t2 - t1) 
        
        performances.append((t2, vitesse, acceleration))

    return performances

# 3️ Tracer le graphe avec Turtle
def tracer_graphe(performances):
    """Affiche la vitesse et l’accélération en fonction du temps avec Turtle"""
    turtle.speed(0)
    turtle.setup(800, 600)  # Taille de la fenêtre

    #  Axe X (Temps)
    turtle.penup()
    turtle.goto(-350, -200)
    turtle.pendown()
    turtle.forward(700)
    turtle.penup()
    turtle.goto(360, -210)
    turtle.write("Temps (s)", font=("Arial", 12, "bold"))

    #  Axe Y (Vitesse et Accélération)
    turtle.penup()
    turtle.goto(-350, -200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(400)
    turtle.penup()
    turtle.goto(-360, 190)
    turtle.write("Vitesse / Accélération", font=("Arial", 12, "bold"))

    #  Tracer la courbe de vitesse
    turtle.penup()
    turtle.color("blue")
    turtle.goto(-350, performances[0][1] * 10 - 200)  # Ajustement de l’échelle
    turtle.pendown()

    for t, v, _ in performances:
        x = t * 40 - 350  # Échelle ajustée
        y = v * 10 - 200
        turtle.goto(x, y)

    turtle.penup()
    turtle.goto(250, 180)
    turtle.color("blue")
    turtle.write("Vitesse (m/s)", font=("Arial", 10, "bold"))

    #  Tracer la courbe d’accélération
    turtle.penup()
    turtle.color("red")
    turtle.goto(-350, performances[0][2] * 50 - 200)  # Ajustement de l’échelle
    turtle.pendown()

    for t, _, a in performances:
        x = t * 40 - 350  # Échelle ajustée
        y = a * 50 - 200
        turtle.goto(x, y)

    turtle.penup()
    turtle.goto(250, 150)
    turtle.color("red")
    turtle.write("Accélération (m/s²)", font=("Arial", 10, "bold"))

    turtle.done()

# 4️ Exécution du programme
fichier_csv = "performance_athlete.csv"
donnees = lire_donnees_csv(fichier_csv)
performances = calculer_performance(donnees)
tracer_graphe(performances)

