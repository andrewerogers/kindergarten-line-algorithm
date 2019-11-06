# Kindergarten-Line-Algorithm
The Kindergarten Line problem is as follows; a bunch of elementary age kids are standing in a line. The teacher tells the kids to turn to their left. As the kids are young they do not know their left from their right; thus, the kids start turned in random directions. If two kids are facing each other, they turn around. Does the line ever reach a stable state?

This python script creates an array of random boolean values (0's and 1's) and applies the Kindergarten Line Algorithm to the array to evaluate the stability of the line structure. This program was also used to evaluate the time complexity of the Kindergarten Line Algorithm.

Using the Principle of Mathematical Induction, we proved that the line does stabilize to a predictable structure. We find that our worst case time complexity is O(n^2). Although the probability of observing such a structure is low, our average case complexity remains O(n^2).


