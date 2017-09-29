import datetime
import praw

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

def is_lineup()

		
##Create bot develop instance, and connect to the reddit API
EarlbotDevDude = []
reddit_connect = EarlbotDevDude.establish_api_connection()

##
for comment in EarlbotDevDude.subreddit('leafs').stream.comments():
	if is_lineup
		## Send array of players to google sheet
		## Retreive data from google sheeet
		## Format data from google sheet
		## Reply to comment with text