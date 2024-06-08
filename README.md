# Viticoles Espagnoles

Cette application est une carte interactive qui affiche les emplacements des différentes régions viticoles espagnoles. La carte utilise `TkinterMapView` pour le rendu et `CustomTkinter` pour les éléments de l'interface graphique. Les utilisateurs peuvent cliquer sur les boutons dans la barre latérale pour zoomer sur des régions spécifiques et voir les marqueurs indiquant leurs emplacements. Chaque marqueur est personnalisé avec une icône représentant le type de vin produit dans cette région (rouge ou blanc).


## Fonctionnalités

- Carte interactive de l'Espagne.
- Marqueurs indiquant les emplacements des différentes régions viticoles.
- Barre latérale avec des boutons pour zoomer sur des régions spécifiques.
- Icônes personnalisées pour les régions viticoles rouges et blanches.


## Demo

[![VinEspana Demo](./assets/demo/demo.gif)](./assets/demo/demo.gif)


## Pré-requis

Avant de pouvoir exécuter l'application, vous devez avoir les éléments suivants installés sur votre système :

- Python 3.11+
- [PDM](https://pdm-project.org/)


## Installation

Suivez ces étapes pour installer les packages requis et configurer l'application :

1. Clonez le dépôt ou téléchargez le code source.
   
   ```bash
   git clone https://github.com/Macktireh/VinEspana
   cd VinEspana
   ```

2. Installez les packages Python requis.

   ```bash
   pdm install
   ```

3. Lancez l'application.

   ```bash
   pdm start
   ```
