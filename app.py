import os
import json
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def load_config():
    config_path = "params.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    else:
        #valeurs par défaut si le fichier n'existe pas
        return {
            "refresh_token": "votre_refresh_token",
            "access_token": "votre_access_token",
            "webhook": "votre_webhook_discord",
            "search": "exemple_de_recherche"
        }

@app.route('/')
def index():
    config = load_config()
    return render_template("index.html", config=config)

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    if not data.get("refresh_token") or not data.get("access_token"):
        return "Erreur : refresh_token ou access_token manquant", 400


    with open("params.json", "w") as f:
        json.dump(data, f)
    try:
        subprocess.Popen(["python", "vintedbot.py"])
        return "Le script a été lancé avec succès !"
    except Exception as e:
        return f"Erreur lors du lancement du script : {str(e)}", 500

# Démarrage de l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
