import arcade
import random
import math
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BlastMaster"

SPRITE_SCALING_PLAYER = 1.0
SPRITE_SCALING_ROCK = 0.3
SPRITE_SCALING_LASER = 0.8
ROCK_COUNT = 50
BULLET_SPEED = 3.5
window = None

class MyGame(arcade.Window)

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        self.player_sprite = None
        self.score = 0
        self.score_text = None
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.score = 0
        self.player_sprite = arcade.Sprite("halo.jpeg", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 75
        self.player_sprite.center_y = 75
        self.player_list.append(self.player_sprite)
        for i in range(ROCK_COUNT):
            rock = arcade.Sprite("rock.jpeg", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(50, SCREEN_HEIGHT)
            self.rock_list.append(rock)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.rock_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        bullet = arcade.Sprite("bullet.jpeg", SPRITE_SCALING_LASER)
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        dest_x = x
        dest_y = y
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        self.bullet_list.update()
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.rock_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for rock in hit_list:
                rock.remove_from_sprite_lists()
                self.score += 1
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()



