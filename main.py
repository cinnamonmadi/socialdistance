import pygame
import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 360

TARGET_FPS = 60
SECOND = 1000
UPDATE_TIME = SECOND / 60.0
fps = 0
frames = 0
dt = 0
before_time = 0
before_sec = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.font.init()
font_small = pygame.font.SysFont("serif", 11)


def main():
    running = True

    while running:
        input_state = handle_input()

        if input_state['quit']:
            running = False

        render_clear()
        render_fps()
        render_flip()
        engine_tick()


def handle_input():
    input_state = {
        'quit': False
    }
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            input_state['quit'] = True

    return input_state


def render_clear():
    pygame.draw.rect(display, BLACK, (0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), False)


def render_flip():
    global frames

    pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    pygame.display.flip()
    frames += 1


def render_fps():
    text = font_small.render("FPS: " + str(fps), False, WHITE)
    display.blit(text, (0, 0))


def engine_tick():
    global before_time, before_sec, fps, frames, dt

    # Update delta based on the time elapsed
    after_time = pygame.time.get_ticks()
    dt = (after_time - before_time) / UPDATE_TIME

    # Update fps if a second has passed
    if after_time - before_sec >= SECOND:
        fps = frames
        frames = 0
        before_sec += SECOND
    before_time = pygame.time.get_ticks()

    # Update pygame clock
    clock.tick(TARGET_FPS)


if __name__ == "__main__":
    main()
