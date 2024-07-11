Hey! :smile:

Are you bored? Do you want something to challenge you? Playing a game :video_game:? Boring! Let’s make one instead!

Ever wonder what happens in game codes, especially their AI parts? How do characters act in different situations? How does changing the difficulty level make NPCs smarter or dumber? If we want to explain what AI is in this field, or generally what AI and ML models are and how they work, we could simplify it to: "These models are giant trees of 'if' and 'else' statements leading to specific results based on situations—but in a much more complex way!" I know this isn't a scientific or entirely accurate explanation, but it can help in understanding the basic concepts.

Let’s make a simple game and see this in action! How about Tic Tac Toe? You know the rules, so no need to explain them.

Let’s keep it simple. We need a few functionalities at first: showing the board, choosing a marker, choosing a cell to place the marker, checking for a win, loss, or draw, and displaying the score. To keep everything tidy and organize my thoughts, I’ll draw a simple flowchart.

<img src="https://github.com/user-attachments/assets/7587de5c-cda8-4903-8029-4a8cc31194e1" alt="Flowchart1" width="500" />

Here is the code: [main.py](old/V1/main.py)

It works. It’s fun, but it’s random. The poor computer doesn’t have a chance to win. Let’s make it better.

This time, we want to help the computer make better choices. What can we do? Sure, there are lots of algorithms like Minimax that can help, but we want to learn and make something from scratch, and also, NOT that complex! So, let’s just assume that our computer thinks better and, instead of choosing a cell randomly, chooses a cell that helps it move towards winning the game.

For that purpose, we can consider all possible states of the game board, and then based on the player’s move, the computer will choose the best cell that leads to a win.

Again, a simple flowchart to organize thoughts :brain:.


<img src="https://github.com/user-attachments/assets/cd535c94-9029-46d8-8ac1-ebc243064051" alt="Flowchart2" width="500" />


In this way, we know which states lead to a win. We have the path (sequence of cells that lead to a win) and the number of steps (we want to win as quickly as possible). Here is the code. I wrote them in a separate file. You know, even the AI needs its own space!

[main.py](old/V2/main.py) and [smart.py](old/V2/smart.py)

Let’s play. In this version of the game, we can see that the computer is acting better, but still somewhat dumb. Why? Because it’s always going for the win, but just going for the win! That’s the problem here, sometimes it needs to block the opponent’s move to prevent them from winning.

Let’s add that to our game as well. Also, if you ran the code, you noticed that after the first move, there is a bit of loading and processing time. This is because the computer needs to generate all possible states over again and then use them to continue playing. We can solve this easily by saving our precomputed states and loading them whenever needed, eliminating the need to recompute everything repeatedly.

Final version: 


<img src="https://github.com/user-attachments/assets/344358f6-4ed8-4b1a-838f-651901ceebe9" alt="Flowchart3" width="500" />

[main.py](main.py) and [smart.py](smart.py)

Ok! It’s done. Our evil :smiling_imp: AI can now play Tic Tac Toe! Technically, it’s not real AI, but it gives us the concepts of how everything works in this field—how models are defined, how they consider all possible states and outcomes, and how the probability of each state helps models act based on their input.

I hope you liked it. Send me any errors or suggestions for improvement. Sometimes small projects are fun and can teach us a lot. With this in mind, what could I add to the game to make it better? It’s simple and easy. Let me know. Thanks! :smile:
