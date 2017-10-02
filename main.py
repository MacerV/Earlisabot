import datetime
import praw
import pickle

class User:
	def __init__(self,username,platform)
		self.username = username
		self.platform = platform
		
class Developer:
	def __init__(self,username,platform,**kwargs)
		User.__init__(username,platform)
		for keys,vall in kwargs.items()
			exec(key + '=val')

class RedditDev
	def__init__(self,username,platform,**kwargs)
		Developer.__init__(self,username,platform,**kwargs)
	def establish_api_connection(self)
		reddit_api = praw.Reddit(client_id=self.client_id,client_secret=self.client_secret,user_agent=self.user_agent,username=self.username,password=self.password)
		return reddit_api
	def create_post(self,api,post_type,Text_or_URL,title,subreddit,stickey=False,sort='new')
		if post == "text"
			thread = reddit_connect.subreddit(subreddit).submit(title,selftext=selftext)
		elif post == "link"
			thread = reddit_connect.subreddit(subreddit).submit(title,url=text_or_URL)
		if stickey
			thread.mod.sticky()
		if sort != "new"
			thread.mod.suggested_sort(sort=sort)		
		return thread
	def comment_reply(self,comment,reply_text)
		comment.reply(reply_text)

def is_lineup(comment,Players)
	#gets unique words/names in comment
	WordsInComment = comment.split()

	##HardCode for Goalienames
	if ('Andersen' or 'Anderson') not in WordsInComment
		WordsInComment.append('Andersen')
	if ('McElhinney' or 'MacElhinney' or 'McBackup') not in WordsInComment
		WordsInComment.append('McElhinney')
		
	#makes sure that there are no name typos in the comments
	for word in WordsInComment
		if word in Players
			word = Players.get(player)
		##May consider removing
		elif
			for knownPlayer in Players
				if Levenshtein_Distance(player, knownPlayer) < 2
					#Could be typo, maybe not
					print(player + " may not be knownPlayer: " + knownPlayer + '. Check roster.")
					player = Players.get(knownPlayer)
					break
		else
			WordsInComment.remove(word)

	#finds the number of players actually mentioned in the comment
	PlayerList = WordsInComment
	if len(list(PlayerList & setPlayers)) == 20
		return PlayerList
	else
		return False
	

	
		
##Create bot develop instance, and connect to the reddit API
EarlbotDevDude = []
reddit_connect = EarlbotDevDude.establish_api_connection()

#loads known players into Player list.
pkl_file = open('Players.pkl', 'rb')
Players = pickle.load(pkl_file)
pkl_file.close()

##
for comment in EarlbotDevDude.subreddit('leafs').stream.comments():
	Lineup(comment,Players) = isLineup
	if Lineup is not False
		## Send list of players to google sheet
		## Retreive data from google sheeet
		## Format data from google sheet
		## Reply to comment with text