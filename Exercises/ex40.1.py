# ex40.1.py
# 使用这种方法写更多的歌进去，确保自己弄懂了传入的歌词是一个字符串列表。

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["Happy birthaday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

no_matter_what = Song(['-' * 30,
                       "No matter what they tell us",
                       "no matter what they do",
                       "no matter what they teach us",
                       "what we believe is true"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

no_matter_what.sing_me_a_song()