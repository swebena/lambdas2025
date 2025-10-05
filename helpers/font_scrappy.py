# text.py
import pygame

pygame.font.init()

# Default font (you can swap this out or expose a setter)
_default_font = pygame.font.SysFont(None, 28)
_default_color = (255, 255, 255)

def set_font(font):
    """Set a global font to use for draw()."""
    global _default_font
    _default_font = font

def set_color(color):
    """Set a global default color."""
    global _default_color
    _default_color = color

def draw_text(surface, text, x, y, font=None, color=None):
    """Mimic love.graphics.print: draw text at (x,y)."""
    f = font or _default_font
    c = color or _default_color
    surf = f.render(text, True, c)
    surface.blit(surf, (x, y))
