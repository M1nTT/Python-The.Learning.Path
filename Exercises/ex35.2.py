# ex35.2.py
# 画出路线图


# & Start
# 
# 1.left // 2.right // 3.neither
#
# 1.1 & bear_room
#   1.1.1 take honey -> ***dead***
#   1.1.2 taunt bear
#       1.1.2.1 taunt bear -> ***dead***
#       1.1.2.2 open door -> & gold_room
#           1.1.2.2.1 Pure numbers, including 1 or 0
#               1.1.2.2.1.1 Less than 50 -> ***WWWWWWWWWWWWWWin***
#               1.1.2.2.1.2 Greater than or equal to 50 -> ***dead***
#           1.1.2.2.2 Purely numeric, does not contain 0 or 1 -> ***dead***
#           1.1.2.2.3 neither -> ***Bug***
#   1.1.3 neither -> & bear_room
#
#
# 2.1 & Cthulhu_room
#   2.1.1 head -> ***dead***
#   2.1.2 flee -> & Start
#   2.1.3 neirther -> & Cthulhu_room
#
#
# 3.1 neither -> ***dead***