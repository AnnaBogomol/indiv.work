import arcade
class MyGame(arcade.Window):
    arcade.open_window(800, 600, 'Learning to create games')
    arcade.set_background_color(arcade.color.BISQUE)
    arcade.start_render()
    arcade.draw_circle_filled(400, 300, 20, arcade.color.MIKADO_YELLOW)
    arcade.draw_circle_filled(390, 310, 3, arcade.color.BLACK)
    arcade.draw_circle_filled(410, 310, 3, arcade.color.BLACK)
    arcade.draw_triangle_filled(395, 300,
                               405, 300,
                               400, 295,
                               arcade.color.BLACK)
    arcade.finish_render()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5


    def on_key_release(self, key, mo):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame(800, 600, 'Learning to create games')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
