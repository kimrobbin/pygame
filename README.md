# Pygame 

This is a game made in Python using Pygame. The game is inspired by Super Mario Bros.

## **The Game**
The objective of the game is to jump on moving mobs and gaining a high score. After a certain number of kills, the game becomes more difficult. If you touch the sides of a mob instead of jumping on its head, you will  die.

## **Controls**

### **Movement**
- **Jump:** `W`, `SPACE`, `ARROW UP`
- **Move Left:** `A`, `ARROW LEFT`
- **Move Right:** `D`, `ARROW RIGHT`

### **Game Functions**
- **Restart Game:** `R`
- **Quit Game:** `ESCAPE`

## **How to Run the Game**

1. **Install Required Software**  
   Ensure you have Python and Pygame installed. Use the following command to install Pygame:
   ```bash
    pip install pygame-ce
    ```
2. **Run the Game**
    ```bash¨
     python main.py


Leaderboard
Spillet inkluderer et leaderboard som viser de 10 beste spillerne basert på poengsum. Dette kan vises i en nettleser ved å kjøre Flask-applikasjonen.

## **Hvordan starte Flask-applikasjonen**
1. Sørg for at Flask er installert: <br>
``pip install flask``

2. Start Flask-applikasjonen: <br>
``python app.py``
3. Skriv in ip-en til pc-en i en nettleser 

### **Database**
Spillet bruker en MySQL-database for å lagre spillerdata. 

**Oppsett av database**
Databasen opprettes automatisk når spillet startes første gang. Tabellen ``USERS`` lagrer følgende informasjon:

* score: Poengsum oppnådd av spilleren.
* time_survived: Tiden spilleren overlevde.
* user: Spillernavn.

## **Feilsøking**
* Hvis spillet ikke starter, sjekk at alle libaries er installert.
* Sørg for at MySQL-serveren kjører og at påloggingsinformasjonen i db.py er korrekt.