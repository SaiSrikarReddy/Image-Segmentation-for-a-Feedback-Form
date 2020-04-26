import os
from segmentation_1.first import first_main
from segmentation_1.second import second_main
from time import sleep

cur = os.getcwd()


first_main(cur)
sleep(1)
second_main(cur)
