# StappieBird

## Inspiration
We came across an Internet article on [Play Therapy](https://www.additudemag.com/fun-games-help-adhd-children-learn-from-play/) for ADHD (Attention Deficit Hyperactivity Disorder) young children. Play Theory suggests that activities that demand ADHD kids to control their movements help them maintain focus. So, we came up with an idea to implement a small yet engaging game to serve the purpose. Because everyone loves Flappy Bird, we decided to base our game on top of it.

## What it does
Helping your young child with ADHD is hard work, and nagging him/her to “do this” or “stop that” often appears as a demanding task, especially your own children. 

Our game, **Stappie Bird** differs from the ordinary **Flappy Bird** in terms of playing mechanisms. With the help of OpenCV library, the game detects the position of the hand (or the object) using webcam. 
For a bird to flap (i.e- jump the user has to make sure his hand does not go outside the configured area. 
However, if the user were to keep moving his hand, the bird would just glide downwards.

The mechanism above has the following benefits:
-    Controls Movement
-    Engages the Childs' Brain and Body Movement
-    Maintains Focus and Attention
-    Builds Concentration
AND…..
ITS FUN and ENTERTAINING!

## How we built it
With laughter and rounds of failure :D The game is essentially built using pyGame library and the computer vision tasks are handled using OpenCV. We are also using a python library called keyboard to run the game successfully without concurrency issues.

## Challenges we ran into
Initial plan is detect motion of the user's hand and to flap the bird only when the user is stationary. However, after several trials with OpenCV we have learned the hard way that the library is so slow that it is no longer practical to use along with the game. We opted to checking the objects position against preset boundary area.

## Accomplishments that we're proud of
First time playing around with OpenCV for tasks like this but we managed to get it working in the end.  
I also scored "5" playing my own game!   
**How much can you score? :P**

## What we learned
Dont get deceived by those Sci-Fi movies, OpenCV is nowhere close to offering smooth detection using cameras.
Built-in webcams in laptops really let you down when you need them the most.
Most importantly, we had fun making it and hope you have fun playing it too.

## What's next for Stappie Bird
The actual fine-tuned motion detection to go alongside the game.

## Team
Phone Thant Ko - 0595
Divya Khemlani - 0350

## Special Thanks
[Deepgaze](https://github.com/mpatacchiola/deepgaze) library for detection tools.
