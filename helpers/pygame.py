import pygame
def get_tile_surface(tmx_map, gid):
    # The tuple contains: (image_path, rect, flags)
    tile_info = tmx_map.get_tile_image_by_gid(gid)

    # Unpack the tuple
    image_path, rect, flags = tile_info

    # Load the image
    image = pygame.image.load(image_path).convert_alpha()

    # Extract the specific tile from the spritesheet
    # rect is (x, y, width, height)
    tile_surface = image.subsurface(rect)

    # Handle potential tile flipping
    if flags.flipped_horizontally:
        tile_surface = pygame.transform.flip(tile_surface, True, False)
    if flags.flipped_vertically:
        tile_surface = pygame.transform.flip(tile_surface, False, True)

    return tile_surface
