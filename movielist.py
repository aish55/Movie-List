action = ["Avengers: Endgame","Black Panther", "Captain Marvel","Spiderman: Homecoming","Thor Ragnorok","Gardians of the Galaxy","Wonder Woman","Avatar"]
mystery = ["Us","Zodiac","Sherlock Holmes","10 Cloverflied Lane","Murder on the Orient Express Wind River, Arrival","Aurora Teagarden Mystery: A Bone to Pick"]
horror = ["Annbell comes Home", "A Quiet Place","Child's Play","It","Halloween","The Witch","The Nun","The conjuring"]
comedy = ["Game Night","Blockers","Step Brothers","Wedding Crashers","Super Bad","Tropic Thunder","ZombieLand","The Hangover"]
romcom = ["To All the Boys I've Loved Before","The Holiday","The Proposal","Valentine's Day","The Ugly Truth","The Break-Up","My Best Friend's Wedding","Clueless"]
animation = ["Toy Story 4","How to Train your Dragon","The Hidden World","Incredibles 2","Moana,Coco", "Zootopia","Lego Movie 2","Up"]
sciencefiction = ["Children of Men","The Martian","The Inception","Edge of Tomorrow","Interstellar"," Ex Machina","Gravity"]
musical = ["13th","Apollo 11","Free Solo","Leaving Neverland","They Shall not Grow Old,Frye","Icarus","Blackfish"]

documentary = ["THe Greatest Showman,Aladdian","La La Land", "A Star is Born, Mama Mia","Into the Woods","The Sound of Music","High School Musical"]

drama = ["The Aftermath","Spotlight","Boyhood","The Help","Gifted","Room","Call me by Your Name","Moonlight"]
historyicalfiction = ["Selma","Lincoln","12 Years as a slave","The Kings Speech", "Kingdom of Heaven,Gladiator","Bridge of Spy's","Troy"]
fantasy = ["Harry Potter","Doctor Strange","The Hobbit","Miss Peregrine's Home for Peculiar Children","Maleficent","Fantastic Beast", "Alice in Wonderland","Clash of The Titans"]


while True:
	print("Welcome to MovieLister. We have 12 genres: action, mystery, horror, comedy, romcom, animation, sciencefiction, musical, documentary, drama, historical fiction, and fantasy.n")
	genre = input("what type of genre of movies would you like to see? Press 'q' to quit\n")
	if genre == "action":
		for x in action:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "horror":
		for x in horror:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "comedy":
		for x in comedy:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "romcom":
		for x in romcom:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "animation":
		for x in animation:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "sciencefiction":
		for x in sciencefiction:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "musical":
		for x in musical:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "documentary":
		for x in documentary:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "drama":
		for x in drama:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "historyicalfiction":
		for x in historyicalfiction:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
	elif genre == "fantasy":
		for x in fantasy:
			print(x)
			ask = input("Would you like to see this movie? y/n\n")
			if ask =='y':
				break
					
					
	elif genre == 'q':
		break
	else: 
		print(" Not a genre option")
