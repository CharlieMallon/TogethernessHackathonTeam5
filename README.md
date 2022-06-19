![Out of Time](https://github.com/CharlieMallon/TogethernessHackathonTeam5/blob/Koshirikdo-patch-1/static/img/lit.JPG "Out of Time")

<span id="project"></span>
## [Code Institute](https://codeinstitute.net)
### June 2022 Hackathon
#### Pride Togetherness

#### [live website here](https://togetherness-team5.herokuapp.com/)
--------------------------------------

<span id="index"></span>
## Index
 <a href="#project">Project Idea 💁</a>
1. <a href="#ux">UX 👌</a>
1. <a href="#features">Features 🎮</a>
1. <a href="#technologies">Technologies Used 👉</a>
1. <a href="#testing">Testing 🔧</a>
1. <a href="#deployment">Deployment 💥</a>
1. <a href="#credits">Credits 👋</a>

# Out of time
    
Our Pink Girrafe team joined Pride Hackathon to create a project to celebrate Pride Month, revolving around the theme of "Togetherness".
We have decided to create an adventure game which can help to bring people together.

<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy

## User Experience (UX)

<strong>Out of Time</strong> is a point and click adventure game where two characters living in the same house but in two different time periods must work together to achieve a common goal. Every action taken in the past will affect the future, in order to solve puzzles and advance in the game.
Users can choose between a single-player and a two-player campaign, the latter of which can be accessed through a mutual words-based ID.

### User stories
### Users


| User story | As a/an | I want to be able to | So that I can |
| -----------: | :--------| :--------------------| :------------|
| 1 | Player | Play an engaging story | enjoy a good game |
| 2 | Player | To play a LGTBQIA-related game | feel represented |
| 3 | Player | To join a LGTBQIA-related game | find some friends |
| 4 | Player | To play a private game | play the game with a friend |
| 5 | Player | See how to play | play the game easily |


| 5 | Team | To create a LGBTQIA-relevant story | support community |
| 6 | Team | Create a project | connect people |
| 6 | Team | Promote our project | raise awareness of the community |



| 4 | Shopper | Responsive design | Order on a mobile device |
| 5 | Shopper | Attractive app |  |


     
   ## 1.2 Scope 

Based on the User Stories following features and components will be required in order to implement Minimum Viable Product so our app can be deployed.

- Welcoming home page with nice hero image
- Play a private game with ID
- Responsive design
- Real and appealing images
- Page to join created game
- Share the Game ID created by user
- Get another ID if user does not like it

## 1.3 Structure

Project will contain both the Front-End and Back-End code.

Front-End code will be written in HTML5 and styled with CSS3.
JavaScript will enable some Front-End dynamic features and also its randomWord function will be used to generate game IDs. 
Python and Flask framework will be used for easier development. Flask support MongoDB connections which will speed up development process.
Github repository will be used for version control and project will be deployed to Heroku.

## 1.4 Skeleton

Our game will be divided into two main campaigns. The first one is where the player creates a game. A game ID is generated which can be private and shared to the other player in order to join the game. The second one is to join existing open game. Game IDs and game data will be stored in MongoDB. Game will be played in multiple rooms whith clickable areas and objects. 

### DB structure
![DB Schema](https://github.com/CharlieMallon/TogethernessHackathonTeam5/blob/Koshirikdo-patch-1/static/img/database_schema "DB Schema")

## 1.5 Surface

The inspiration for this project was sourced from our team mate Manuel who lives in a tower. Manuel took pictures of his tower which were cartonized and will be used as a background and game images. Navigation in game will be carried through clicking on different parts of picture, e.g. clicking on main door will bring the player to loby.

#### Wireframes
Balsamiq wireframes

![Tower Wireframe](https://github.com/CharlieMallon/TogethernessHackathonTeam5/blob/Koshirikdo-patch-1/static/img/database_schema "Tower Wireframe")
![Wireframes](https://github.com/CharlieMallon/TogethernessHackathonTeam5/blob/Koshirikdo-patch-1/static/img/database_schema "Wireframes")


<a href="#index">Back to top ☝️ </a>
<span id="features"></span>

# 2. Features 🎮
## 2.1 Implemented features

### Intro page
 Welcomes user to the game. Large background image with a call to action button and an introduction for the game.
 
### Game start page
 Lets the player choose wheter create a new game or join a co-op one.

### Create game id page
Here the user can create an id that can be sent to other players, in addition to choosing whether this session is public or private and what character they'll be playing as.

### Join game page
Here the player can submit an id to to join the game with another player.

### Game page
Consists of different rooms. This is where the player interact with the story.

## 2.2 To be implemented

Few more features could have been implemented but were not initially required. A nice feature would be to have a dialog box for easier communication throughout the game. 
Another one could be a dating page with ads for lonely people.

<a href="#index">Back to top ☝️ </a>
<span id="technologies"></span>

# 3. Technologies Used 🎡

## 3.1 Languages

- HTML/HTML5
Each web page was built using HTML elements.

- CSS
Some HTML elements were styled using CSS

- JavaScript
Interactive web behaviour and random word ID generator.

- Python
This app was build using python based framework Flask and its packages.

## 3.2 IDE, Version control and hosting

- GitPod
Collaborative development environments in browser

- Git and GitHub
Version control and repository

- Heroku
GitHub repository was linked with Heroku and is hosted here


## 3.4 Other tools

- Balsamiq was used to create wireframes

- Am I Responsive was used to create title image for readme.md

- DrawSQL was used to create DB schema

- Chrome Devtools were used to see the behaviour of the elements and their style

- Cartoonified backgrounds
    https://play.google.com/store/apps/details?id=com.gamebrain.cartoon&hl=it&gl=US

<a href="#index">Back to top ☝️ </a>
<span id="testing"></span>

# 4. Testing 💉

## 4.1 Validation

<a href="#index">Back to top ☝️ </a>
<span id="deployment"></span>

# 5. Deployment 🔧

Code and other files as images, and other documents are stored in Github repository. Instructions how tu deploy project with Github pages can be found [here](https://github.com/Martin-ITT/memoryTesting). At the time of working on this project Github pages does not support generating dynamic content (running a python code). A cloud application platform Heroku is used to run and operate this project. Heroku is linked with Github repository and automaticaly deployes the most recent version of the code. MongoDB service is used to store all data. 

Heroku deployment guideline
1. Create Heroku account
1. Select Create New app
1. Provide name and your region and create the app
1. Select Deploy tab and under deployment method select Connect to GitHub
1. Find corresponding repository and select Connect
1. You can enable Automatic Deploys from corresponding branch
1. Secret variables from local env<span>.</span>py had to be added to Heroku config variables. This can be found under Settings tab - Reveal Config Vars
1. Select Open app buton to run the app

MongoDB guideline
1. Create MongoDB account
1. Create New Project
1. Build a cluster - free cluster was selected for this project
1. AWS cloud based in Ireland was chosen
1. When cluster is created click collections
1. Add your own data
1. Choose appropriate name for database and also for collection
1. You can add data / insert documents into DB
1. Create user / admin account to maintain DB
1. Configure IP address which can access this DB
1. Click connect in clusters tab and select connect your application
1. Select driver and version for your project and copy connection string


<a href="#index">Back to top ☝️ </a>
<span id="credits"></span>

# 6. Credits 💳

A big thank belongs to:

- Our families and friend for patience
- Code Institute team

## 6.1 References

    
    
    
    
    
    
    
