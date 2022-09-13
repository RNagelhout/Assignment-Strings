# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
first_goal_player = "Ruud Gullit "
second_goal_player = "Marco van Basten "

goal_0 = 32
goal_1 = 54

scorers = first_goal_player + \
    str(goal_0) + ", " + second_goal_player + str(goal_1)

report = first_goal_player + "scored in the " + \
    str(goal_0) + "nd minute" + "\n" + \
    second_goal_player + "scored in the " + str(goal_1) + "th minute"

# Part 2

player = "Ronald Koeman"
first_name = (player[:6])
last_name_len = len(player[7:])
first_name_len = len(first_name)
name_short = "R. Koeman"
chant = ((first_name + "! ") * first_name_len).rstrip()

good_chant = chant[-1] != " "

print(chant)
