# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

from LunarLander import *

env = LunarLander()
env.reset()
exit_program = False
while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         exit_program = True
    #     if event.type == pygame.KEYDOWN:
    #         if event.key in [pygame.K_ESCAPE, pygame.K_q]:
    #             exit_program = True
    #         if event.key == pygame.K_UP:
    #             boost = True
    #         if event.key == pygame.K_DOWN:
    #             boost = False
    #         if event.key == pygame.K_RIGHT:
    #             left = False if right else True
    #             right = False
    #         if event.key == pygame.K_LEFT:
    #             right = False if left else True
    #             left = False
    #         if event.key == pygame.K_r:
    #             boost = False        
    #             left = False
    #             right = False
    #             env.reset()

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster
    if x > 15:
        right = True
    if abs(xspeed)/abs(x)>0.1:
        right = False

    if x < -15:
        left = True
    if abs(xspeed)/abs(x)>0.1:
        left = False


    if y < 170:
        if yspeed>20:
            boost = True
        if yspeed<15:
            boost = False


    if y < 100:
        if x > 10 or xspeed > 10:
            right = True
        if x < -10 or xspeed < -10:
            left = True   
        if abs(x)<15 and abs(xspeed)<=1:
            left = right = False

    if left and right:
        left = right = False



    
    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE




env.close()