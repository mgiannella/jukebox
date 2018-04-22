# Jukebox
HackRU 2018 Project - A collaborative music queue

## Description
This web-application serves to function as a collaborative music queue. Users are able to add songs, up-vote, and down-vote based on their personal music preferences. The song with the highest priority (number of up-votes) gets played. Once a song finishes, the song with the next highest priority automatically starts. Each user is given a unique ID upon connecting to the server, and that ID is used to make sure that no user can have a more than 1 point total impact on the score of the song.  

## API Reference

This project was developed to incorporate the BOSE SoundTouch API 

## Modules 

* requests            
* datetime 
* flask                 
* random
* json                  
* string
* spotify               
* threading
* Queue                 
* bosesoundhooks
* webbrowser            
* time 

## Contributors

Mike Giannella @mgiannella
Caleb Frey @calefrey
Adam Romano @aromano31

## License

This project is distributed under the MIT license. See https://opensource.org/licenses/MIT for details. 
