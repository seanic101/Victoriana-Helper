# Victoriana-Helper
this document will be broken down into 3 diffrent areas
	
	1-general ideas of what the structure should look like
	2-how stuff could look, psydocode
	3-questions for eli from sean (and visa vera very rarely)
	
	
1-GENERAL IDEAS
	1.Have a player class that stores all attributes, items and spells, basically a player sheet of values
	2.Have the data for players be able to be loaded into object from json file
	3.if a higher up object tries to grab a stat(basically an int) thats not part of the file, then itll return a 0 with a comment that it didnt exist. 
	
2-PSUDOCODE FROM SEAN
	class Player:
		def__init__(self):
			self.name_first="temblate";
			self.name_last="last";
			
			self.ethics="neutral good";
			self.race="human";
			self.class="upper";
			self.age=12;
			self.gender="male";
			self.hair="black";
			self.eye_color="blue";
			self.childhood_experiences="whatever";
			self.vocation="bandit";
			
			self.stre = 1;
			self.dext = 1;
			self.fort = 1;
			self.pres = 1;
			self. wits = 1;
			self.reso = 1;
			
			self.common_skills = 4;
			
			self.special.skillname = 4;
			
			
3-QUESTIONS
	1. Is this the best way to store data in valiable form? I do want to be able to access all of the variables by a getter and setter.
	2. What should I do for things like a spell list, that has more data that could be included, so maybe the player class can own spells, weapons and armor?
			
			
			
	
	
	
	