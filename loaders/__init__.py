import os
import re
import pytmx
#
from utils import find_first, OrderedSet
from settings import MAPS_DIR
from symbols import valid_mappings

def levels_all():
    """
    outputs level references
    """
    filenames = os.listdir(MAPS_DIR)
    levels = []
    for filename in filenames:
        d = {}
        d['filename'] = filename
        d['abspath'] = os.path.join(MAPS_DIR, filename)
        # dirty workaround for naming
        d['name'] = str(int(''.join(re.findall(r'\d', filename))))
        # dirty workaround for indexing
        d['number'] = int(''.join(re.findall(r'\d', filename)))
        levels.append(d)
    return levels

def get_level_by_number(num):
    """
    A dummy picker
    """
    levels = levels_all()
    level = find_first(levels, lambda i: i['number'] == num)
    return level

def parse_level(level):
    """
    Parse a TMX map into a 2D matrix (list of lists).
    Returns: (grid, metadata)
      - grid[y][x] = gid
      - metadata = dict with map info
    """
    tmx_data = pytmx.TiledMap(level['abspath'])
    # find the first tile layer
    layer = next(l for l in tmx_data.layers if hasattr(l, 'tiles'))
    # initialize empty matrix with zeros
    grid = [[0 for _ in range(tmx_data.width)] for _ in range(tmx_data.height)]
    # fill matrix only with valid gids
    for x, y, extra in layer.tiles():
        gid = tmx_data.get_tile_gid(x, y, 0)
        result = [gid] if (gid in valid_mappings) else []
        grid[y][x] = OrderedSet(result)
    metadata = {
        'width': tmx_data.width,
        'height': tmx_data.height,
        'tilewidth': tmx_data.tilewidth,
        'tileheight': tmx_data.tileheight,
        'orientation': tmx_data.orientation,
        'layer_name': layer.name,
        # duplication for convenience
        'filename': level['filename'],
        'abspath': level['abspath'],
        'name': level['name'],
        'number': level['number'],
        # and again
        'tmx_data': tmx_data,
    }
    return grid, metadata
