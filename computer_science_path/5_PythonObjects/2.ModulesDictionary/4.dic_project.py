# dictionary project -- 这个project总结了 dictionary 这一部分的知识

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key,value in zip(letters,points)} #创建一个字典

letter_to_points.update({"":0})#这样blank就对应0了
print(letter_to_points)

def score_word(word):
    point_total = 0
    for i in word:
        fenshu = letter_to_points.get(i , 0)
        point_total += fenshu
    return point_total

brownie_points = score_word("BROWNIE")

print(brownie_points)



player_to_words = { "player1":["Blue","TENNIS","EXIT"], "worldNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER","BELLy","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for i in words:
        input = score_word(i)
        player_points += input
    player_to_points.update({player:player_points})

print(player_to_points)

# play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# make your letter_to_points dictionary able to handle lowercase inputs as well