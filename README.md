# Thirty Shots Battlehips

This game constitues my third Project Portfolio with [Code Institute](https://github.com/Code-Institute-Org). 
The project runs in a CLI, is deployed via [Heroku](https://www.heroku.com/), and uses Python.

Thirty Shots Battleships is a single player version of the popular game Battleships where the user is recruited to sink the foreign fleet of "Chatarra" preventing them for making it ashore to the fictional town of "Oros".

During the making of the game, I have particularly enjoyed using the Heroku platform as a service (PaaS). Heroku has enabled me to build, run, and operate this application entirely in the cloud.

[The live project can be found here](https://thirty-shots-battleships.herokuapp.com/)

![Screenshot of Heroku app on PC and laptop screens](docs/Capture-pc-laptop.PNG)

## Features

### The title

- I developped a simple ASCII drawing for the title which basically consists of the "Thirty Shots" title itself in big letters.
- I added the word "battleships" to the right of the ASCII art in normal console letters. 
- I added a touch of blue colour by using ANSI codes.

![Screenshot of ASCII drawing title](docs/Capture-title.PNG)

### The Background

- As seen in the screenshot above I added a background around the actual app by modifying the layout.hml page provided by Code Institute for the project.
- This feature adds a touch of color and front-end development to the Heroku app.
- I chose a blue background svg image with a spiral pattern suitable for the maritime theme of the game.

### Site favicon

- I have added a Ship image favicon to the site in line with the naval theme of the game.

![Screenshot of browswer tab showing favicon](docs/Capture-favicon.PNG)

![Screenshot of enlarged favicon](docs/Capture_favicon-xl.PNG)

### The plot / instructions

As explained in the game's instructions, Oros is much coveted for the precious golden mineral covering its cliffs. 
Oro's watchmen have spotted Chatarra's fleet fast approaching.
The user will have to destroy the ennemy's 4 ships before they land.
If the user does not succeed, the ennemy will steal Oro's gold.
Users only have 30 cannonballs to complete their mission, hence the title of the game "Thirty Shots Battleships".
If users runs out of ammunition then Chatarra's troops will make it ashore.

The instructions go on to explain the rules:
- If a ship is hit, it will be marked as 'X'
- If it's a miss, it will be marked as '-'.

![Screenshot of plot and instructions](docs/Capture-instructions.PNG)

### Accept / Decline the mission

- The user will be given the choice to accept or decline the mission. 
- The program will print one of the following to the console depending on the user's answer:

User enters an invalid answer:

![Screenshot of printout when user inputs a wrong choice](docs/Capture-accept-mission-invalid.PNG)

User declines the mission:

![Screenshot of printout when user declines the mission](docs/Capture-mission-no.PNG)

User accepts the mission:

![Screenshot of printout when user accepts the mission](docs/Capture-accept-mission-yes.PNG)

### Game Board

- As seen above, once the user accepts the mission, the program will print a message asking the user to take a guess and will print the game board.
- The game board consists of a 7x7 grid as, after testing, this seems like a reasonable grid size to have a fair shot at sinking all the ships in thirty shots.
- As also seen in the screenshot above, under the board will be printed the number of turns left and the number of ships left as well as the instruction "Get ready to fire" to prompt the user to keep guessing.

### Enter a guess

- Users are prompted to first enter a row guess and then a column guess.
- If the row / column number are out of range, the program will print a message prompting users to enter a valid choice.

![Screenshot of guess out of range](docs/Capture-wild-guess.PNG)

### Miss... / Hit! / You sunk a ship!

- If a ship is hit it will be marked as 'X' on the grid and the console will print "Hit!&#128165;" in red font.
- If a ship is sunk the console will also print "You sunk a ship!&#128165;&#128165;&#128165;" in red font.
- If the user misses il will be marked as '-' on the grid and the console will print "You missed... 💦 in blue"

![Capture showing a hit](docs/Capture-hit.PNG)
![Capture showing a sunk ship](docs/Capture-sunk3.PNG)
![Cpature showing a missed shot](docs/Capture-you-missed.PNG)

### Lose / Win printout

- If the user manages to sink the 4 ships in thirty shots, the console will print the following:

![Capture showing a winner printout](docs/Capture-mission-accomplished2.PNG)

- If the user does not manage to sink the 4 ships in thirty shots, the console will print the  following:

![Capture showing a loser printout](docs/Capture-you-lose.PNG)

### Features left to implement
- Leave a space between ships so that no ships are immediately juxtaposed on the grid.

## Python Logic

## Data model

The functionality of the game relies mainly on the class 'Ship'. This class will create the board, randomize the ship coordinates, place the ships and display the board to the user.

## Testing

- [PEP8 online check](http://pep8online.com/) was used to validate the Python code. No errors remain at the time of this submission.
![Screenshot of the PEP8 validation results](docs/Capture-PEP8.PNG)

- [W3 validator](https://validator.w3.org/) was used to validate the layout.html page. No errors remain at the time of this submission.

### Solved bugs

- A security issue with the Heroku app prevented any automatic deployments. The deployment had to be made from gitpod signing first into heroku and then pushing to heroku with the following commands:
    - heroku login -i (to login)
    - heroku git:remote -a thirty-shots-battleships (to select the correct app on heroku)
    - git push herouk main (to push to heroku from gitpod)

- Code indentation issues and long lines of code were flagged on the PEP8 online validator and corrected accordingly.

- 'Get ready to fire' appearing even after user sinks all ships. This issue was solved by replacing the location of the print line "Get ready to fire!" from directly under the definition of the function to later in the code (line 299) as part of the section appearing under the board which also displays number of turns and ships left. Following this logic once there are no more ships to sink the game will end and the "Get ready to fire!" phrase will not be printed anymore.

Before the change:

![Screenshot showing the 'Get ready to fire!' print location before fixing the bug ](docs/fire_before.PNG)

After the change:

![Screenshot showing the 'Get ready to fire!' print location after fixing the bug](docs/fire_after.PNG)

- Issue with placement of input question prompting user to answer if mission is accepted

- Background issue





### Remaining bugs
### Validator testing

## Deployment
This project was developed by forking a specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.
The project has been optimized for a final [Heroku deployment](https://thirty-shots-battleships.herokuapp.com/).

The project was deployed to Heroku using the below procedure:

1. Log in to Heroku or sign up for free account
2. Select create new app from the drop-down list
3. Enter a unique app name
4. Select appropriate region to your location
5. Click create app button to proceed
6. 'Deploy' tab will be shown. scroll down to the config vars section in the settings tab
7. Click reveal config vars button
8. Enter PORT in the 'KEY' field
9. Enter 8000 in the 'VALUE' filed
10. Click the add button
11. In the buildpacks section click add buildpack button
12. Type and select 'Python' and click 'save changes' button
13. Repeat same to add 'node.js' pack
 
IMPORTANT The buildpacks must be in this particular order. If they are not, then click and drag to change it
 
Select Github as the deployment method from the deploy tab
Connect to Github to confirm
Type repository name and click search button
Click connect button that appeared next to your repository name
Select your preferred deployment type:
'Enable Automatic Deploys' for automatic deployments when you push updates to Github - NOT RECOMMENDED if you have a free account
'Deploy Branch' for manual deployments - RECOMMENDED for free account users



## Credits
- Code Institute's Battleships LMS tutorial
- [Code credit on Ship class goes to Cloud2236863496](https://discuss.codecademy.com/u/cloud2236863496/summary)
- Peer Code Review: I have looked at other CI students code for inspiration like [David Bowers](https://github.com/dnlbowers/battleships/blob/main/views/layout.html) layout.html code for inserting a background image, and [Lukaszkukla](https://github.com/lukaszkukla/hangman-x/blob/main/src/colors.py) code for including a range of colors in the text displayed in the console.
- [Background svg image](https://www.svgbackgrounds.com/)
- [Favicon image of ship](https://upload.wikimedia.org/wikipedia/commons/9/95/P_ship_grey.svg)
- [Clear console function from delftstack.com](https://www.delftstack.com/howto/python/python-clear-console/)
- [Code Institute for providing the template with a mock terminal to display my game via a webpage](https://github.com/Code-Institute-Org/python-essentials-template)


## Tools used
- [Heroku app](https://www.heroku.com/)
- [PEP8 online validator](http://pep8online.com/)

