from symbols import OPERANDS, OPERATORS, TRAITBLOCKS
from utils import iter_grid, OrderedSet

# Predicates (hardcoded IDs)
def is_operand_block(n): return n in OPERANDS
def is_operator_block(n): return n in OPERATORS
def is_trait_block(n):   return n in TRAITBLOCKS

# Grid helpers
def in_bounds(world, x, y):
    h, w = len(world), len(world[0])
    return 0 <= y < h and 0 <= x < w

def first_match(cell, predicate):
    for n in cell:
        if predicate(n):
            return n
    return None

# Operator resolution
def resolve_operations(world, operators):
    ops = []
    for x, y in operators:
        center = world[y][x]
        operator_id = next(iter(center), None)
        if operator_id is None: continue
        # vertical
        if in_bounds(world, x, y-1) and in_bounds(world, x, y+1):
            operand_id = first_match(world[y-1][x], is_operand_block)
            trait_id   = first_match(world[y+1][x], is_trait_block)
            if operand_id and trait_id:
                ops.append((operand_id, operator_id, trait_id, "vertical"))
        # horizontal
        if in_bounds(world, x-1, y) and in_bounds(world, x+1, y):
            operand_id = first_match(world[y][x-1], is_operand_block)
            trait_id   = first_match(world[y][x+1], is_trait_block)
            if operand_id and trait_id:
                ops.append((operand_id, operator_id, trait_id, "horizontal"))
    return ops

# Rule derivation
def derive_rules(world, operations):
    rules = {}
    for operand, operator, trait, axis in operations:
        if trait == PUSH_TRAIT and operator == ASSIGNMENT_OPERATOR:
            rules.setdefault(operand, set()).add(PUSH_TRAIT)
        if trait == STOP_TRAIT and operator == ASSIGNMENT_OPERATOR:
            rules.setdefault(operand, set()).add(STOP_TRAIT)
        if trait == BANG_TRAIT and operator == ASSIGNMENT_OPERATOR:
            rules.setdefault(operand, set()).add(BANG_TRAIT)
        if trait == GHOST_TRAIT and operator == ASSIGNMENT_OPERATOR:
            rules.setdefault(operand, set()).add(GHOST_TRAIT)
    return world, rules

# ----------------------------
# Indices
# ----------------------------
def build_indices(world, rules):
    trait_index = {}
    cell_index = {}
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            traits_here = set()
            for obj in cell:
                for t in rules.get(obj, set()):
                    trait_index.setdefault(t, []).append((x, y, obj))
                    traits_here.add(t)
            if traits_here:
                cell_index[(x, y)] = traits_here
    return trait_index, cell_index

# ----------------------------
# Push logic (simplified)
# ----------------------------
def get_push_chain(world, rules, x, y, dx, dy):
    chain = []
    while True:
        x, y = x+dx, y+dy
        if not in_bounds(world, x, y): return None
        cell = world[y][x]
        if any(STOP_TRAIT in rules.get(obj, set()) for obj in cell):
            return None
        pushable = next((obj for obj in cell if PUSH_TRAIT in rules.get(obj, set())), None)
        if not pushable:
            return (x, y, chain)
        chain.append((x, y, pushable))

def shift_chain(world, chain, dx, dy):
    for x, y, obj in reversed(chain):
        world[y][x].remove(obj)
        world[y+dy][x+dx].append(obj)

def trypush(world, rules, direction):
    dx, dy = direction
    new_world = [[list(cell) for cell in row] for row in world]

    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            for obj in cell:
                if CTRL_TRAIT not in rules.get(obj, set()):
                    continue
                if GHOST_TRAIT in rules.get(obj, set()):
                    # Ghosts move without collision or pushing
                    nx, ny = x + dx, y + dy
                    if in_bounds(world, nx, ny):
                        new_world[y][x].remove(obj)
                        new_world[ny][nx].append(obj)
                    continue

                # Normal avatar logic (push chain, stop, etc.)
                result = get_push_chain(world, rules, x, y, dx, dy)
                if result:
                    tx, ty, chain = result
                    shift_chain(new_world, chain, dx, dy)
                    new_world[y][x].remove(obj)
                    new_world[y+dy][x+dx].append(obj)
    return new_world

def bang(world, rules):
    """
    Destroy all contents of any cell that contains an object with the 'bang' trait,
    plus all 8 neighbors (diagonals included). Returns a new grid.
    """
    h, w = len(world), len(world[0])
    to_destroy = set()
    # Find all bang sources
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            if any(BANG_TRAIT in rules.get(obj, set()) for obj in cell):
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        nx, ny = x + dx, y + dy
                        if in_bounds(world, nx, ny):
                            to_destroy.add((nx, ny))
    # Build new grid with destroyed cells emptied
    new_world = [[list(cell) for cell in row] for row in world]
    for (x, y) in to_destroy:
        new_world[y][x] = []
    return new_world

# ----------------------------
# Step pipeline
# ----------------------------
def step(world, direction):
    # find operators
    operators = [(x,y) for y,row in enumerate(world) for x,cell in enumerate(row)
                 if any(is_operator_block(n) for n in cell)]
    operations = resolve_operations(world, operators)
    world, rules = derive_rules(world, operations)
    world = trypush(world, rules, direction)
    world = bang(world, rules)
    return world
