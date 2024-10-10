# Trigonometry-Demo
Demonstrates essential video game trigonometry using pygame

Use the arrow keys to move the pirate head around. This demonstrates:
- How to make one point follow another and calculate the distance 2 points.
- How to make one point aim and lunge/shoot at another point.
- How to contain a point within a rectangle.
- How to create a ring of points. 

<h2>How to Run</h2>
1. If you don't have python installed run follow this tutorial: https://www.youtube.com/watch?v=YKSpANU8jPE
2. If you don't have pygame installed enter this into your command prompt 
<i>pip install pygame</i>
3. Open command prompt, navigate to the root folder and enter:
<i>python Presentation.py</i>

Alternatively, you can put "python Presentation.py" into a text document and change that document's extension to "cmd" and double click that.

<h2>Explanation of Python Files</h2>

<u>TrigJacknife.py</u>: Contains a custom Point and Rectangle class along with a number of essential trigonometric functions. Used by CoreGame.py.

<u>CoreGame.py</u>: The “business layer” responsible for the core logic of the game such as moving the player and NPCs. This operates independently of pygame. Used by Presentation.py

<u>Presentation.py</u>: The “presentation layer” that makes use of pygame responsible for visually interpreting what CoreGame.py is doing to the user and relaying user input to CoreGame.py.

As a best practice: I have separate core game and presentation layers. The core game is the logical game that uses the game engine as little as possible. Think of it like an old-timey game console. The console itself runs the game but doesn't have any way in and of itself to show you what's going on. That's where the presentation layer comes it. This uses the game engine to add visuals to what the core game is doing and relay user input to the core game. Think of this like the TV you connect the game console to. 

In this way, it's easier to switch game engines or translate the game to another language should the game engine become impermissible to use – like if the company that owns the game engine drops support or gets scummy. Think of it like being able to switch your game console to another TV when the company demands regular payments to continue using the TV. 
