# Battleships game
This game is a single player game designed for users to compete against the computer in a game of logic and chance. The player must sink all the computers battleships by making estimations on where the computer's battleships are located on a 5 x 5, 8 x 8 or 10 x 10 battle grid. The game provides value to users who are interested in playing online games that provide them with the opportunity of playing against the computer.

## User Experience
### User Stories
- First time visitor goals
1. I want to play a simple game of battleships with clear instructions
2. I want to see my score displayed as I play through the game
3. I want the ability to chose the size of the grid and how many battleships

- Returning visitor goals
1. I want to play against the computer using a different sized grid or different number of battlehsips
2. I want to beat the computer in fewer turns
3. I want to play the game without any errors occuring and to ensure the developer of the game is a trusted source.

- Frequent visitor goals
1. I want to see has the developer included additional features to allow the player a certain number of turns or missiles to sink all the computers ships.
2. I want to see has the developer updated the design of the site to include battleships image designs to improve the aesthetics of the game.
3. I want to see has the user included the option for players to save or share their highest scores or a leaderboard.

- Owner goals
1. I want to provide an interactive game that encourages users to play and gain encouragement and excitement from.
2. I want to provide a game that encourages healthy competition amongst users.
3. I want to gain recognition and develop an online presence in the area of online game development.

## Design
The grids are designed to display in the center of screens with the positions allocated by a number and letter system. The grid size displayed depends on the users game choice.

The functions and validation checks were planned and designed with lucidchart.

![Battelships lucid chart](assets/images/battleships-lucid-chart.PNG)

## Existing Features
The user is welcomed to the game where a short explanation is provided on how to play the game

The user is requested that they input their username and choose the grid size they wish to play.

The user grid is displayed showing the location of the user's battleships and the computers board is displayed. A prompt is issued to the user to choose a position. Validation is in place here so only numbers and letters can be used.

The user's score is displayed and incremented when a user sinks one of the computers battleships and vice versa. 

A game over screen appears whenever a player sinks the required number of battleships or the computer does.

## Accessibility

## Languages
[Python]()

## Frameworks, Libraries and Programs

[LucidChart](https://www.lucidchart.com/pages/)
- LucidChart was used to design the layout of the game and which functions would be required to run the game including areas where validation was in place.

[Git](https://www.gitpod.io/)
- Gitpod was used for adding commits each time a new feature was added to the game and for pushing the commits to Github.

[Github](https://github.com/)
- Github was used for storing the site after being pushed from gitpod.

[Heroku]()
- Heroku was used for deploying the website.

## Future Features
- I would like to provide users with the opportunity for choosing the number of missiles/turns and the number of ships.
- I would like to have make the game a two player game where the first player to sink the generated ships would win.
- I would like to provide a random variable to change the size of the hidden ships on the board and include the ships' orientation.

## Validation & Testing
[PEP8 Python Validator](https://pep8ci.herokuapp.com/)
When the code was first tested in the validator errors appeared due to the length of lines.
![]()

## Testing User Stories
- First Time Visitors
- The print messages provided clear instruction however I feel a displayed legend would have been useful and the number of ships should have been made clear to the player before the player guessed positions.
- There was a turn counter incorporated into the game, I would have preferred if a score counter was displayed and incremented each time I hit a battleship.
- I was able to choose the grid size at the beginning of the game however I would have enjoyed choosing the number of battleships.

## Testing on Browsers and Devices

### Browser Testing
The deployed game was tested on Google Chrome and Internet Explorer.
- The layout and positioning are consistent.
- The validation for a user choosing an invalid grid size operates
- The validation for the user entering valid row and column guesses is working effectively.

### Device Testing
The deployed game was tested on a variety of devices including desktop, HP laptop, Samsung Galaxy A12, A13, A22, S8, iPhone13, iPhone SE2 and Redmi 2201117TY. Family members were asked to access the deployed site, play the game and highlight any issues with the print statements, displaying the board and guesses.

### Lighthouse Testing
I carried out a Lighthouse test using the Google Chrome Lighthouse function for desktop and mobile.

## Bugs

### Solved Bugs

### Unsolved Bugs
iPhone device users had trouble accessing and playing the deployed Battleships game. The game was tested on the iPhone SE2 and iPhone 13.
On iPhone when the input requests the user to enter their name and iPhone users click return the f string does not print to the user.
![iPhone13]()

## Deployment
Heroku was used to deploy the battleships game.

### Instructions
1. Login to [Heroku](heroku.com).
2. Click "Create a New App" on the Heroku dashboard.
3. Enter a unique app name and select a region.
4. Click the ![settings tab](assets/images/heroku-settings.png).
5. Click "Reveal Config Vars" and add the key PORT and the value 8000 to the 
![key and port fields](assets/images/heroku-config-var.PNG)
6. Click "Add buildpack" and select "Python" and select "Save Changes".
![Buildpack](assets/images/add-buildpack.PNG)
![Buildpack-Python](assets/images/add-buildpack-python.PNG)
7. Click "Add buildpack" again and select "Nodejs" and select "Save changes".
![Buildpack-Nodejs](assets/images/add-buildpack-nodejs.PNG)
Note the order here is important.
8. Click the Deploy tab and select GitHub as the deployment method and click "Connect to Github"
![Deployment Method](assets/images/heroku-deployment-method.PNG)
9. Enter the Github repository by name and click "search".
10. Once the repository is shown click "connect".
11. Click "deploy branch" and wait for the message to appear stating 
![Deploy branch](assets/images/heroku-app-deployed.PNG)
12. Click the "view" button to navigate to the deployed link.


## Credits

### Code

[How to code battleship gameboard in python](https://www.youtube.com/watch?v=cwpS_ac8uk0&t=45s)
The code used in this (Youtube)[https://www.youtube.com/] tutorial was adapted to write the display board function based on the user's choice of grid size.

[Battleship - ASCII Art](https://ascii.co.uk/art/battleship)
This website was used to add a design feature of a battleship image to the welcome message at the beginning of the game. The image is displayed using several print statements.

[Portfolio Project 3 Scope](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
This video tutorial from the [Code Institute website](https://codeinstitute.net/ie/) was used and adapted to incorporate the Board class into the Battleships code to set the number of ships, the board type and provide a method to add ships to the hidden board.

[How to Code Battleship in Python](https://www.youtube.com/watch?v=tF1WRCrd_HQ)
The get ships location function in this [Youtube](youtube.com) tutorial was adapted to code the make guess function and incorporate validation checks for the user input.

[Python Intermediate Project Assignement](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=534s)
This [Youtube](https://www.youtube.com/) tutorial was watched for inspiration on the different designs a Battleships game can incorporate and methods that could be introduced to increase the complexity of a battleships game.

### Content
- All content was written by the developer.
- The design of a multi grid size battleship game was inspired by the Code Institute Scope video tutorial, the Knowledge Mavens Youtube tutorial and Python Ninja's battleship game.
- The battleship art displayed in the welcome message was adapted from asciiart.co.uk.

### Acknowledgements
- Thank you to my partner, friends and family for their support and encouragement throughout the project and for testing the deployed game on their mobile devices and providing feedback.