# Spefications a M-Chessboard game

In this project has the following characterisitcs

## Initialization screen
-In principle, there is a screen where the player could choose between create a new perfil or login its perfil
  + If is new player, The game will show a screen where the player can write its nickname and can choose an image (pre-load images) for its perfil. 
    * This information will be corroborate if there is on the date base and will return the Initialization screen.
    * If a new player its information will be chraged in the database, and the game will show the template of perfil screen with its infoamtion.
  + If is login option, the game will show the templete of perfil screen with its information pre-charged (nickname, images)
- The screeen will change to the wait room screen.


## Wait Room screen
- In the wait room connect two differents players.
- The colors  will be asigned to the players in a random way or who was the first connect (maybe).


## Principal screen
- For each player screen, its pieces will be in the bottom. In top will be its timer and information of players. In lefts side, there will be show the capture pieces.
- The timer will run when the player moves its first piece.
- In its turn, the player can choose any piece and see its possibles moves (this process is not a moves). 
- For do a move need choose first the piece and choose a vacant allowed square. These moves follow the Chessboard rules.
- When the player do its move, its turn is end and its timer is in pause.
- If a local match the screen will be update change between the information of second player (Pieces on chessboard and captured)
- If is a remote match, the information of the player is send to the server. The server verify and send this information to the second player. The screen of second player is update.
- When a player is in check, screen show the word in red  words.
- In Checkmate case, the words winner is show in the screen on the winner player.
- The information of the winner player will be saved in the data base and its win matchs will be incrised by one.


