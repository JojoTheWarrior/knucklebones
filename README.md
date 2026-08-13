# Total number of states

Consider for one column, the number of ways to fill it. The column has 3/3 slots, subject to the following constraints:
- Each number can appear in the top or the bottom but not both
- The top and bottom can hold at most 3 numbers
- The order of the numbers does not matter

# Other ideas

Is there a way to analyze this game using Sprague-Grundy numbers?

- Probably not, since the game is not impartial
- And you can't really XOR the Nimbers of columns to determine whether the board is winning or losing