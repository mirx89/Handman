import glob


class Model:
    def __init__(self):
        self.database_name = "databases/hangman_words_ee.db"
        self.images_files = glob.glob("images/*.png") # All hangman images
        # New game
        self.new_word = None # Random word from databsase
        self.user_word = [] # user find letter (empty list)
        self.all_user_chars = [] # Any letters entered incorrectly
        self.counter = 0 # Error counter (wreong letters)
        # leaderboard
        self.player_name = "UNKNOWN"
        self.leaderboard_file = "leaderboard.txt"
        self.score_data = [] #leaderboard file contents
