#! /usr/bin/env python3

###Dicerolling bot by /u/Fredo699###

#A bot which rolls dice of varying sizes.


import praw, time, random, pickle
# Imports praw for the Reddit API, time for the sleep function, pickle to dump objects, and random to generate random numbers.

password = open("./pass.txt","r")
# Links to a text file, so the password won't be hardcoded in the source code.


already_done_read = open("./data/comment_log","rb")
# Links to a binary file where the old comments are stored.

r = praw.Reddit("Dicerollingbot by /u/Fredo699, message me with any issues.")
# Establishes connection to Reddit

r.login('dicerollingbot',password.read())
# logs into the account for /u/dicerollingbot with the password file

submissions = r.get_subreddit('redditroleplay').get_new(limit=100)
# Returns the 100 latest posts from /r/RedditRolePlay

already_done = pickle.load(already_done_read)
already_done_cntr = 0
# Array that keeps track of comments that are already responded to.

while True:
	for submission in submissions:
		
		flat_comments = praw.helpers.flatten_tree(submission.comments)
		# flat_comments is a variable that reorganizes the comments tree into one chronological, unidirectional list of comments
		
		for comment in flat_comments:
			if "d20" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,20))
			elif "d4" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,4))
			elif "d6" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,6))
			elif "d8" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,8))
			elif "d10" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,10))
			elif "d12" in str.lower(comment.body) and comment.id not in already_done:
				comment.reply(random.randint(1,12))
				
			
			# Replies to comments with different random number intervals
			
			already_done[already_done_cntr] = comment.id
			if already_done_cntr == 19999:
				print("Starting new iteration of already_done[]")
				already_done_cntr = 0
			already_done_cntr += 1
			# sets previous comment in already_done array
	
	
	already_done_write = open("./data/comment_log","wb")
	pickle.dump(already_done, already_done_write)
	# dumps the already_done array into the binary file.
	
	submissions = r.get_subreddit('redditroleplay').get_new(limit=100)
	# Refreshes list of submissions.
	
	time.sleep(30)
	#Makes program pause, so as not to spam Reddit and get /u/dicerollingbot banned
	
	
	
	
