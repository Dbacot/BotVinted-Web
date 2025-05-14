
Vinted Bot
===========

Ce bot permet de recevoir les nouveaux articles de Vinted directement sur votre serveur Discord via un webhook tout en modifiant les paramètres facilement depuis une interface Web

Prérequis
----------

- Un serveur Discord avec un webhook.
- 2 tokens à récupérer manuellement sur [Vinted API](https://www.vinted.fr/api/v2/catalog/items).
- Installez les dépendances via `pip install -r requirements.txt`.

Configuration
-------------

1. Récupérez vos tokens et le webhook Discord.
2. Lancez le serveur avec la commande :
   ```
   python app.py
   ```
3. Accédez à `http://127.0.0.1:5000/` et remplissez les champs :
   - `Refresh_token_web`
   - `Access_token_web`
   - `Discord Webhook`
   - `Recherche Vinted` (ex: "Air Force 1")
4. Cliquez sur **Lancer le script** pour démarrer le bot.

Erreurs possible : 
-----------------

- **Erreur 401** : Vérifiez vos cookies et tokens. Si vous obtenez une erreur comme `{"code":100,"message":"Jeton d'authentification invalide"}`, essayez de changer de navigateur pour récupérer de nouveaux cookies.

Références
----------

- Tutoriel utilisé : [Créer un bot Vinted](https://www.elletrouvetout.com/2024/11/27/comment-creer-un-bot-vinted/)
- Documentation de `requests` : [Requests Docs](https://docs.python-requests.org/en/latest/)
