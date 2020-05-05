# FIFA Filter
**Data Overview**

The data files included in this assignment are “Fifa19.csv”, “Fifa18.csv”, and “Fifa17.csv”. They were provided by Kaggle users ​Soumitra Agarwal, ​Aman Shrivastava and Karan Gadiya, respectively. Each data set contains information about every single footballer in the games Fifa 19, Fifa 18, and Fifa 17. This information includes the skill ratings, player values, country of birth, club, position, and more. This data also represents the information of each player and goalie in real life with good accuracy. The fields of data that are used in this assignment are as follows from the files are: 

 Data Structure #1 (Fifa 19) - Shotpower: Power of a player’s kick - Diving: A goalie’s diving ability - Pace: Stamina and speed of player - Handling: How well a goalie can catch - Passing: Passing accuracy of player - Kicking: How strong a goalie’s kick is - Dribbling: Ball control of player - Positioning: How will a goalie covers angles - Defending: How good of a defender a player is - Reflex: How quick a goalie can react - Physical: How strong a player is - Speed: How fast a goalie can run  - Position: The footballer’s primary position - Value: Price of footballer in Euros 
 
 Data Structure #2 (Fifa19, Fifa 18, Fifa 17) - Club: The club a footballer plays for - Overall Rating: The overall skill rating of a footballer 
 
 
 
**Player Data In Dictionary (Data Structure #1) A dictionary of lists containing FIFA 19 player and goalie stats.**
 
If the footballer is a player, the values are as follows: Footballers = {Prefered Name : [Position, Pace, ShotPower, Passing, Dribbling, Defending, Physical, Value], ...} 
 
If the footballer is a goalie, the values are as follows: Footballers = {Prefered Name : [Position, Pace, ShotPower, Passing, Dribbling, Defending, Physical, Value], ...} 
 
Example of filled data structure: Footballers = {‘L. Messi’ : ['Position: RF', 'Pace: 86', 'ShotPower: 85', 'Passing: 90', 'Dribbing: 97', 'Defending: 28', 'Physical: 59', 'Price: 110.5M Euros'], ‘M. Neuer’ : ['Position: GK', 'Diving: 90', 'Handling: 86', 'Kicking: 91', 'Positioning: 87', 'Reflex: 87', 'Speed: 60', 'Price: 38M Euros'], ...} 
 


**Team Data Over Time (Data Structure #2) A dictionary of dictionaries that store the yearly rating for each club in FIFA 17 to FIFA 20.** 
 
The dictionary would contain sub-dictionaries that are structured as follows: Clubs = {Club Name : { ‘Fifa17’ : 2017 Club Rating, ‘Fifa18’ : 2018 Club Rating, ‘Fifa19’ : 2019 Club Rating, ‘Fifa20’ : Predicted 2020 Club Rating}, …} 
 
Example of filled data structure (ratings rounded to 2 decimals): Clubs = {'FC Barcelona': {'Fifa17': 82.56, 'Fifa18': 78.09, 'Fifa19': 78.03, 'Fifa20': 77.97}, 'Juventus': {'Fifa17': 81.65, 'Fifa18': 79.79, 'Fifa19': 82.28, 'Fifa20': 84.78}, 'Paris Saint-Germain': {'Fifa17': 77.96, 'Fifa19': 77.43, 'Fifa20': 77.43}, 
 
