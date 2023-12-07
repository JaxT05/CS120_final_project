# CS120_final_project
Instructions: Win this turn-based combat battle by clicking fight, heal, or cast. 
Goal Summary: My main goal was to create a turn-based combat system with visual elements and an easy user interface. A smaller (unaccomplished) goal was to create a tiny overworld to go along with it. 
Technologies: SimpleGE, Pygame, Random + “characterdata”, which I created to store a basic build for a combat character 
Citations – 
Graphics: 
Dragon - https://opengameart.org/content/dragons
Background – Me (Jax)
Sounds: 
Background Music - https://opengameart.org/content/tiny-swords-duel
Player Strike – https://opengameart.org/content/metal-impact-sounds
Player Miss – https://opengameart.org/content/3-melee-sounds
Player Cast – https://opengameart.org/content/magic-words-healing-sound-effect
Player Casting Miss - https://opengameart.org/content/were-doomed
Player Heal - https://opengameart.org/content/magic-words-healing-sound-effect
Player Healing Miss – https://opengameart.org/content/short-wind-sound
Enemy Strike - https://opengameart.org/content/hit-sound-bitcrush
Font: https://fonts.google.com/specimen/VT323
To start off, I set up the shell of the game and created a textbox, fight button, and heal button before playing around with the placement until I came up with something I liked. After this I created a base combat system by attaching combat functions to the buttons – I used what I wrote for the Turn-Based Combat project for necessary character data and hitting functions. To track the combat, I made the textbox update and added labels to show player hp and enemy hp, then added a “continue” function to fix the problem with the textbox updating too fast. After this, I created a “cast” function, which randomizes stat changes for both the player and the enemy, and then added updating labels for the main stats. After tweaking the code to my liking, I finally added the graphics and sounds I wanted and began to polish the UI, and then created a game over screen with reset and quit buttons to tie everything off. 
I learned a lot while working on this project. I believe that this is the one that finally had me look back at all my progress and notice how far I had come in such a short time. When I got discouraged, I managed to pick myself back up and keep pushing until I got the necessary results. 
I managed to get stuck quite a bit, but I had two major roadblocks that took a while to find a workaround for. The first was getting the combat system working. I wasn’t sure how to approach it until I broke it up into smaller pieces that were activated by buttons on the UI. The second was getting the textbox to update in a readable manner, for which I tried to think of multiple solutions. The one that worked the best was using a “continue” button that prevented the textbox from changing until the user clicked to proceed. 
In terms of improving, I think more can always be done. As my first change, I would add to the casting option so that the user could have a selection of spells instead of working with a completely randomized spell (although I also think there’s some fun in that). If I had to do things differently, I think I would set up everything so that I could plug in more monsters to have a selection from, and most likely a small overworld to explore. 
The initial idea that I presented on my design document is a far stretch from what I created, but I wouldn’t have it any other way, and I’m glad that I lessened the workload. I still kept my initial goal- which was to create a visual turn-based combat system. 
Staying on task is not my forte but creating milestones and daily goals helped me push through a lot. Checking in with my peers also encouraged me to stay caught up and constantly work towards my goals. 
 
