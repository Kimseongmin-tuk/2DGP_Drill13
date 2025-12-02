from pico2d import load_image
import game_world
import common
import random


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(50, common.court.w - 50)
        self.y = random.randint(50, common.court.h - 50)

    def update(self):
        pass

    def draw(self):
        # 화면상의 위치 계산
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            # 소년과 충돌하면 공 제거
            game_world.remove_object(self)