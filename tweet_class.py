class Tweet :
    reply_count = 0
    def __init__(self,tweet_data):
        self.tweet_data = tweet_data
        self.child_obj = None
        self.visited = False

    def add_child(self,childs):
        self.child_obj = childs
        self.visited = True

    def get_child(self):
        return self.child_obj

    def get_id(self):
        return self.tweet_data['tweet_id']

    def get_username(self):
        return self.tweet_data['author_id']
