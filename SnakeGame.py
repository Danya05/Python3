import arcade
import sys
import curses
from collections import deque, namedtuple

Point = namedtuple("Point", ["x", "y"])

ScreenWidth = 800
ScreenHeight = 800

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)
        self.snake = deque([Point(x=3, y=2), Point(x=2, y=2)])

    def setup(self):
        # Настроить игру здесь
        pass

    def draw_snake(self):
        """Draw snake onto board."""

        for pt in self.snake:
            self.addch(pt.y, pt.x, self.SNAKE_CHAR)

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()

        arcade.draw_rectangle_filled(ScreenWidth//2, ScreenHeight//2, 1.5 * ScreenWidth//2, 1.5 * ScreenHeight//2, arcade.color.GUPPIE_GREEN)
        arcade.draw_rectangle_outline(ScreenWidth//2, ScreenHeight//2, 1.5 * ScreenWidth//2, 1.5 * ScreenHeight//2, arcade.color.BROWN, border_width=5)
        self.draw_snake()

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        pass


def main():
    game = MyGame(ScreenWidth, ScreenHeight)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()


arcade.finish_render()


arcade.run()
