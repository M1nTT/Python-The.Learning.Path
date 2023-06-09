# ex40.2.py
# 试试看能不能给它加些新功能，不知道怎么做也没关系，只要试着去做就行，看会发生什么。
# 尽管瞎折腾，弄坏了也没关系，反正程序不会觉得疼。


class Song(object):
    times = 0

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.line = 1

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line, end=' ')
            print(f"    --> {Song.times+1} song, {self.line} line")
            self.line += 1
        Song.times += 1


happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

no_matter_what = Song(["No matter what they tell us",
                       "no matter what they do",
                       "no matter what they teach us",
                       "what we believe is true"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

no_matter_what.sing_me_a_song()






