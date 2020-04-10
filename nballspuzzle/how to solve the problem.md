> Things get more complex with three eggs, but taking a deep breath we can apply the same principle of minimizing maximum regret. 
We need to select our first egg such that, if it breaks, or does not break, it results in a problem, which recursively is now a two egg problem, that we already know how to solve to minimize maximum
 regret!

OK hold on tight, here we go …

Let's define our building to have a maximum of k floors. 
Let's say that the number of egg we have is represented by e, and the floor we are currently attempting to drop from is represented by n. With me so far? 
OK, what we need to find our optimal solution is to calculate what would happen if we dropped an egg from every floor (1 through to k) and 
(recursively) calculate the minimum number of droppings needed in the worst case. We're looking for the floor that gives the minimum solution to the worst case.

If we drop an egg from floor n, one of two events happens:

1) The egg breaks, so now our problem is reduced to a tower of height n-1, and we now have e-1 eggs.

2) The egg doesn't break and now we need to check k-n floors and we still have e eggs.

Remember we need to mimimize the number of drops in the worst case, so we take the higher (max) of these two situations, and select the floor which yields the minimum number of drops.

The code to solve this is fairly easy to write recursively, but suffers from a common problem that occurs with recursive solutions in which the same sub-problems are evaluated again, and again,
 and again, dragging performance to a grind for anything other than trivial solutions.
 To get around this, we need to keep track of values already computed so that we don't have to repeat the calculation.

Rather than getting lost in gnarly code, let's just share some of the results, and for some buildings higher than 100 stories.
