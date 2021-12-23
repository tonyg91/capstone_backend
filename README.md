## Capstone Project

### Title: Bullet Journal App

## User Story 
A user can use this page to view different types of bullet journals, supplies, and page themes to get them started. The user can add in their own bullet journal themes, bullet journals, and supplies that they use and want to share with others. There will aslo be links for beginners to find out where they should start and what they should start with. When the user is adding their own personal page themes the user has a section to put there name as the creator.

## Models
# Journal
  -brand: String,
  -paperweight: String,
  -sizes: String,
  -image: String,
# Supply
 -brandName: String,
 -type: String,
 -ink: String,
 -image: String,
# Theme
 -image: String,
 -page: String,
 -creator: String

 ## Tech
 -Django
 -React 
 -CSS
 -Django Rest Framwork
 

### Route Table
## Journal
| URL | Method | Action |
|-----|--------|--------|
| / | GET | Masonite Welcome Page|
| /journal | GET, POST | Index page of all journals as well as the page to add journals|
| /journal/:id | PUT, DELETE | Show page of a single journal|

## Supply
| URL | Method | Action |
|-----|--------|--------|
| / | GET | Masonite Welcome Page|
| /supply | GET, POST | Index page of all supplies as well as the page to add supplies|
| /supply/:id | PUT, DELETE | Show page of a single supply|

## Theme
| URL | Method | Action |
|-----|--------|--------|
| / | GET | Masonite Welcome Page|
| /theme | GET, POST | Index page of all theme as well as the page to add theme|
| /theme/:id | PUT, DELETE | Show page of a single theme|

### Challenges 
The main challenge I had with getting my django backend up and running was that at first I could only get one model to work. I built the backend in every which way I could find online it only the first model was working. So I spent four days trying to figure out what was wrong with the backend. Because I could not find anything wrong with what I have followed from the documentation. And Here comes day five and it turns out that I was declaring the models wrong the entire time. So the four days of suffering was just because I used a : instead of = which drove me up a wall.