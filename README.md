# Total number of states

Consider for one column, the number of ways to fill it. The column has 3+3 slots, subject to the following constraints:
- Each number can appear in the top or the bottom but not both
- The top and bottom can hold at most 3 numbers
- The order of the numbers does not matter

Let $C$ be the number of ways to fill one column.

We can use $C \leq \binom{8}{3}^2 = 56^2 = 3136$ as an upper bound for each column.

Running `state_bounder.py`, we're getting the exact number of states to be $C = 3067$.

The order among columns doesn't matter, so we can use stars-and-bars with 3 columns, each being type $t_i \in [1, C]$.

The calculation is $\binom{C-1+3}{3}=\binom{3069}{3}\approx4.8 \times 10^9$.

# Space Usage

If we can compress every game state to a single index, then we can store all $4.8$ billion states in around $625 MB$.

If we store, for each state, simply the next state it should move to, assuming we store the next index as a $32$ bit number, this would cost around $20$ GB. Fuck.

# Other ideas

Is there a way to analyze this game using Sprague-Grundy numbers?

- Probably not, since the game is not impartial
- And you can't really XOR the Nimbers of columns to determine whether the board is winning or losing