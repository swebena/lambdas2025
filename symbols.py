# NOTICE:
# mind the off-by-one offsets
# between the Tiled editor GUI and the file

# spritesheet row 1
BLANK = 1
PENGUIN = 2
WALL = 3
COIN = 4
FLAG = 5
BOMB = 6
ROCK = 7
# spritesheet row 2
PENGUIN_OPERAND = 18
WALL_OPERAND    = 19
COIN_OPERAND    = 20
FLAG_OPERAND    = 21
BOMB_OPERAND    = 22
ROCK_OPERAND    = 23
# spritesheet row 3
CTRL_TRAIT  = 34
STOP_TRAIT  = 35
PUSH_TRAIT  = 36
GOAL_TRAIT  = 37
BANG_TRAIT  = 38
GHOST_TRAIT = 39
# spritesheet row 4
ASSIGNMENT_OPERATOR = 50

valid_mappings = {
        # row 1
        BLANK:   lambda t: t,
        PENGUIN: lambda t: t,
        WALL:    lambda t: t,
        COIN:    lambda t: t,
        FLAG:    lambda t: t,
        BOMB:    lambda t: t,
        ROCK:    lambda t: t,
        # row 2
        PENGUIN_OPERAND: lambda t: t,
        WALL_OPERAND:    lambda t: t,
        COIN_OPERAND:    lambda t: t,
        FLAG_OPERAND:    lambda t: t,
        BOMB_OPERAND:    lambda t: t,
        ROCK_OPERAND:    lambda t: t,
        # row 3
        CTRL_TRAIT:  lambda t: t,
        STOP_TRAIT:  lambda t: t,
        PUSH_TRAIT:  lambda t: t,
        GOAL_TRAIT:  lambda t: t,
        BANG_TRAIT:  lambda t: t,
        GHOST_TRAIT: lambda t: t,
        # row 4
        ASSIGNMENT_OPERATOR: lambda t: t,#
        # AND_OPERATOR: # Not implemented!
        }

OPERANDS = [
        PENGUIN_OPERAND,
        WALL_OPERAND,
        COIN_OPERAND,
        FLAG_OPERAND,
        BOMB_OPERAND,
        ROCK_OPERAND,
        ]

OPERATORS = [
        ASSIGNMENT_OPERATOR,
        ]

TRAITBLOCKS = [
        CTRL_TRAIT,
        STOP_TRAIT,
        PUSH_TRAIT,
        GOAL_TRAIT,
        BANG_TRAIT,
        GHOST_TRAIT,
        ]
