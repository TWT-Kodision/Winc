# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_goal = "Ruud Gullit"
second_goal = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = first_goal+f' {goal_0}'+", "+ second_goal+f' {goal_1}'
report = f'{first_goal} scored in the {goal_0}nd minute\n{second_goal} scored in the {goal_1}th minute'
print (scorers)
print(report)
player = "Hans van Breukelen"
first_name = player[0:player.find(" ")]
print(first_name)
last_name_len = len(player[player.find(" ")+1:])
print(last_name_len)
name_short = player[0] + ". " + player[player.find(" ")+1:]
print(name_short)
chant = (first_name + "! ") * (len(first_name)-1) + (first_name + "!")
print(chant)
good_chant = chant[len(chant)-1]!=" "
print(good_chant)
