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
        '''
        Intializes the parent class
        '''
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        '''
        Exemplifies where the files are expected to come from.
        '''
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        '''
        Sprite list variables
        '''
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None
        
        '''
        Player information for the game
        '''
        self.player_sprite = None
        
        '''
        Background of the game
        '''
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setup(self):
        '''
        Initializes variables and sets up game
        '''
        
        '''
        Sprite Lists
        '''
        self.player_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        
        '''
        Image and set up of sprite
        '''
        self.player_sprite = arcade.Sprite("halo.jpeg", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 75
        self.player_sprite.center_y = 75
        self.player_list.append(self.player_sprite)
        
        '''
        Image and creation of rocks
        '''
        for i in range(ROCK_COUNT):
            rock = arcade.Sprite("rock.jpeg", SPRITE_SCALING_ROCK)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(50, SCREEN_HEIGHT)
            self.rock_list.append(rock)
        
        '''
        Background color
        '''
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        '''
        Has to be done in order to provide a screen or starting point
        '''
        arcade.start_render()
        
        '''
        Draws all of the sprites
        '''
        self.rock_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        '''
        Whenever the mouse is moved, the following code will be executed
        '''
        
        '''
        Creates the bullet
        '''
        bullet = arcade.Sprite("bullet.jpeg", SPRITE_SCALING_LASER)
        
        '''
        This constantly moves the bullet to the player's location
        '''
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y
        
        '''
        Position of the bullet based on the mouse
        '''
        dest_x = x
        dest_y = y
        
        '''
        Destination of the bullet and the angle at which it travels
        '''
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        
        '''
        Angles the sprite in way that it doensn't look awkward or out of place
        '''
        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")
        
        '''
        The angle is included in the calculation, all determining the velocity of the bullet
        '''
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED
        
        '''
        Adds bullet to the correct sprite list
        '''
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        '''
        Updates and movement of game
        '''
        
        '''
        Updates all existing sprites
        '''
        self.bullet_list.update()
        
        '''
        This is a for loop, going through all the bullets throughout the game
        '''
        for bullet in self.bullet_list:
            '''
            Checks to see if a rock was hit
            '''
            collision_list = arcade.check_for_collision_with_list(bullet, self.rock_list)
            
            '''
            If contact was made, remove that rock
            '''
            if len(collision_list) > 0:
                bullet.remove_from_sprite_lists()
                
            '''
            If a bullet is off screen, take it out of the game
            '''
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()



