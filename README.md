# Thirty Shots Battlehips

## How to play

## Features

## Data Model

## Testing

## Testing
### Solved bugs
Security issue with Heroku app.
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
- Code Institue Battleships tutorial
- [Code credit on Ship class goes to Cloud2236863496](https://discuss.codecademy.com/u/cloud2236863496/summary)
- [Background clipart image of cliffs](https://www.clipsafari.com/clips/o313445-sea-cliffs)
- [Favicon image of ship](https://upload.wikimedia.org/wikipedia/commons/9/95/P_ship_grey.svg)

## Tools used
- [Heroku app](https://www.heroku.com/)
- [PEP8 online validator](http://pep8online.com/)