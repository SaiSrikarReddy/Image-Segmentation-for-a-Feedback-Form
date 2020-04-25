# Image-Segmentation-for-a-Feedback-Form

* Need to have basic Knowledge on:
  * Python
  * opencv
  * python - os functions

## Problem Statment
* Still most of the people are using paper based survey/review.And, these review sheets need to be manually evaluated.
* Our algorithm is used as the first stage of that review form i.e, Segmentation of question and answer.

## Solution
> Solution would be a two level segmentation
### First_level_Segmentation
* For this you need to refer first_level_segmentation.py
* In this first level it divides each block/box of text(you can see in data/Level_1)
* Each block/box have a question and answer.
### Second_level_Segmentation
* For this you need to refer second_level_segmentation.py
* In this second level it takes each block from first level and divides question and answer.
