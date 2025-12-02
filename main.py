# Drill #13 제출 - 2022184007 김성민

from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(800, 600)
game_framework.run(start_mode)
close_canvas()

