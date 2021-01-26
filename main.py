import rotatescreen
import time
# screen = rotatescreen.get_primary_display()
# screen.rotate_to(0)
# for i in range(10000):
#     time.sleep(1)
#     screen.rotate_to(i*90 % 360)

a = rotatescreen.get_primary_display()
a.rotate_to(0)
# this loop is rotatescreen till the range
for i in range(13):
    time.sleep(1)
    a.rotate_to(i*90 % 360)
