# Labo 05 (ue19-lab-05)

Le projet va chercher une blague aléatoire sur Internet et l'affiche dans le terminal.

Il utilise l'API [Official Joke API](https://official-joke-api.appspot.com/random_joke).


# Comment le lancer ?

Il y a deux façons de le faire : la simple (avec Python) ou la "pro" (avec Docker).

# Option 1 : Directement sur votre PC

1.  **Clonez le projet :**
    ```bash
    git clone https://github.com/MathysCyber/ue19-lab-05.git
    cd ue19-lab-05
    ```

2.  **Installez la dépendance :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Lancez-le !**
    ```bash
    python app.py
    ```

# Option 2 : Avec Docker

1.  **Clonez le projet** (si ce n'est pas déjà fait).

2.  **Construisez l'image :**
    ```bash
    docker build -t blague-app .
    ```

3.  **Lancez le conteneur :**
    ```bash
    docker run --rm blague-app
    ```

Et voilà ! Vous devriez voir une blague apparaître.