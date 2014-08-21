Data Modeling: The Dark Crystal
======

Introduction
------
In the Movie, ["The Dark Crystal"](http://en.wikipedia.org/wiki/The_Dark_Crystal), the evil Skeksis are able to restore their youth by draining and consuming the essense from other beings.  They've driven the Gelfling race to the brink of extinction (only two remain), however there are still plenty of Podlings that can be rounded up.

The Skeksis consume the essense of a lot of Podlings.  They're also a greedy race, so there are constant fights over who has consumed the most essense.  The chief prison warden of the Skeksis has requested you build him a database to help him keep track of everything.


Requirements
------
Here's what you know:

* The prison current has 20 cages to hold their captives, though they may want to add more if they get a large haul.
* Each cage can hold up to 5 Podlings or Gelflings.
* Each Podling has a certain amount of essense stored within them.  When processed and entered into the system, the Skeksis will measure the essence and record it as an integer between 0-500.
* Gelflings hold a large amount of essense (between 0-10000 units).
* For each prisoner, we need to keep track of:
 * Race
 * Arrival Date
 * Amount of Essense Remaining
 * Location (which cage are they in)

* Skeksis regularly visit the processing facility to consume essense.  Need to keep track of:
 * Which Skeksis consumed essense
 * When the essense was consumed
 * From which prisoner the essense was consumed
 * How much essense was consumed

Data Model
------
Design a database system to store data meeting the above requirements.  

* Plan out what tables you need and what data needs to be stored in each table.  
* Note what data types each column should be.  
* Define any relationships you would build in between the tables.

