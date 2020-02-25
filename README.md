# Kindergarten-Line-Algorithm
The Kindergarten Line problem is as follows; a bunch of elementary age kids are standing in a line. The teacher tells the kids to turn to their left. As the kids are young they do not know their left from their right; thus, the kids start turned in random directions. If two kids are facing each other, they turn around. Does the line ever reach a stable state?

The included python script implements an algorithm designed to model the behavior in the problem statement above. The python script was used to evaluate the stability of the line structure and provide intuition for proof.

We proved that the line does reach a predictable stable state that contains exactly one bifurcation point. Additionally, we investigated number of steps to reach a stable state (one to one map to runtime) and found that n^2 steps are required to guarantee a stable state.


