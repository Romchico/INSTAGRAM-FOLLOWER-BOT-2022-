from follower_module import follower_start
from time import sleep

for i in range(0, 5):
    follower_start(link, post_place=i)
    sleep(5)

# I don't reccomend you to follow more than this, you can be restricted. Run this every hour at most.
