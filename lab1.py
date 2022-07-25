'''
Sara Paguaga - 20634
'''

from gl import Renderer, color, V2
import random

width = 1024
height = 500

rend = Renderer(width, height)

        
fig1 = [V2(165, 380), V2(185, 360), V2(180, 330),
        V2(207, 345), V2(233, 330), V2(230, 360),
        V2(250, 380), V2(220, 385), V2(205, 410),
        V2(193, 383)]

fig2 = [V2(321, 335), V2(288, 286), V2(339, 251),
        V2(374, 302)]

fig3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

fig4 = [V2(413, 177), V2(448, 159), V2(502, 88),
        V2(553, 53),  V2(535, 36),  V2(676, 37),
        V2(660, 52),  V2(750, 145), V2(761, 179),
        V2(672, 192), V2(659, 214), V2(615, 214),
        V2(632, 230), V2(580, 230), V2(597, 215),
        V2(552, 214), V2(517, 144), V2(466, 180)]

fig5 = [V2(682, 175), V2(708, 120), V2(735, 148),
        V2(739, 170)]


rend.makeBorder(fig1, color(0.4, 0, 0.7))
rend.glFill(fig1, color(0, 0, 0), color(0.4, 0, 0.7))

rend.makeBorder(fig2, color(0.4, 0, 0.7))
rend.glFill(fig2, color(0, 0, 0), color(0.4, 0, 0.7))

rend.makeBorder(fig3, color(0.4, 0, 0.7))
rend.glFill(fig3, color(0, 0, 0), color(0.4, 0, 0.7))

rend.makeBorder(fig5, color(0, 0.01, 0))
rend.glFill(fig5, color(0, 0, 0), color(0, 0.01, 0))

rend.makeBorder(fig4, color(0.4, 0, 0.7))
rend.glFill(fig4, color(0, 0, 0), color(0.4, 0, 0.7))




rend.glFinish("image-5.bmp")