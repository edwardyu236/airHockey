#################################################################
#                   A       IIIII    RRRRRRR                    #
#                  A A        I      R     R                    #
#                 A   A       I      RRRRRR                     #
#                AAAAAAA      I      R    R                     #
#               A       A   IIIII    R     R                    #
#                                                               #
#     H    H     OOO        CCC   K    KK   EEEEEE  YY     YY   #
#     H    H   OO   OO    CC      K KK      E         YY  YY    #
#     HHHHHH  O       O  C        K         EEEEEE      YY      #
#     H    H   OO   OO    CC      K KKK     E           YY      #
#     H    H     OOO        CCC   K    KK   EEEEEE      YY      #
#                                                               #
#                                  By: (Edward) Sum Lok Yu      #
#                                                               #
#################################################################

README
--------

What it does: A game of Air Hockey

Dependencies:
Pygame (http://www.pygame.org/download.shtml).

How it works:
Games go up to 10.
Move your mouse to control your mallet (the lower one) to play against the computer.
Hit the puck into the goal to get a point.
Click "R" to reset the game.
There contains textual output for instructions and the scores.

Notes:
I implemented AI and collisions on my own. As such it is not perfect, and has some known issues.


Known Issues:
The puck may sometimes appear to go beyond the walls.
Because of the simple AI, sometimes the puck and the AI mallet may appear to be stuck for a period of time. Most of the time this gets resolved after several moments, but there may be cases in which the puck is genuinely stuck (in this case clicking "R" to reset the game would be a good idea).
Due to the simple collision algorithm, collisions may sometimes not work completely as expected in real life.