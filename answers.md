# CMPS 6610 Problem Set 04
## Answers

**Name:** Amin Mirfakhar


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |                     |                |
alice29.txt    |                     |                |
asyoulik.txt    |                     |                |
grammar.lsp    |                     |                |
fields.c    |                     |                |




- **1d.**



----

## Part 2: Binary Heaps

- **2a.** Give a method to construct a binary min-heap in $O(n)$
work. Hint: Given an array $A$ of elements, consider the implicit
representation as an
almost-complete binary tree and show how to achieve the heap
property for this tree with $O(n)$ work.




- **2b.** What is the span of your approach?


----

## Part 3: Making Change

After completing a tortuous semester of Algorithms, you decide to take a much needed vacation. You arrive in a city called Geometrica, and head to the bank to
exchange $N$ dollars for local currency. In Geometrica they have a
currency that is 1-1 with U.S. Dollars, but they only have
coins. Moreover the coins are in
denominations of powers of $2$ (e.g., $k$ denominations of values $2^0$, $2^1$, \ldots,
$2^k$). You wonder why they have
such strange denominations. You think about it a while, and because
you had such a good Algorithms instructor, you realize that there is a
very clever reason. 

- **3a.** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.

  - So, we can look for the largest number of k that $2^k$ is less than or equal to the N, in this case if we subtract the value form N $\to N' = N-2^k$ then we can repeat this process untill the N' = 0. In other words, if we look at the binary representation of N then the number of position having element 1 shows the number and values of the coins we should get. 

- **3b.** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.

    - If we don't act greedy then instead of taking the largest value k (in greedy algorithm G) then there is a m whick m is less than k and m is in the optimal set (O). In this case we devide our problem into to suboptimal case with $N - 2^m$ and then we could end up with more than one of coin m, but for each 2 coin with value m there is a coin with value m+1 if we repeat this process to reduce the number of coins then we reach m should be equal to k.




- **3c.**  What is the work and span of your algorithm?

  - the process is similar to deviding N by 2 we repeat the process for the quotient in each step and keep the number of time we did this if remainder is equal to 1. So the number of that we can perform devision by 2 is equal to the work and span (since it is a sequential process) then it will at most take $\log{_2}{N}$. The other method is taking the int value of $\log{_2}{N}$ (k) then calculate the $N - 2^k$ and repeat this process. which again would take k times at most (k  = int($\log{_2}{N}$)).


----

## Part 4: Making Change Again

You get tired of Geometrica and travel to the nearby town of
Fortuito. While Fortuito also has a 1-1 exchange rate to the US
Dollar, it has an even stranger system of currency where any given bank
has a completely arbitrary set of denominations ($k$ denominations of
values $D_0, D_2, \ldots, D_k$). There is no guarantee that you can
even make change. So you wonder, given $N$ dollars is it possible to
even make change? If so, how can it be done with as few coins as
possible?


- **4a.** You realize the greedy algorithm you devised above doesn't
  work in Fortuito. Give a simple counterexample that shows that the
  greedy algorithm does not produce the fewest number of coins.

    - consider the case that N is equal is to 9 and the coin set is {1, 2, 4, 5, 6} then if we take the largest coin af first which is 6 then we have to take 2 and 1 in the next steps since we don't have any other options (3 coins {6, 2, 1}). But if we take 5 at first instead of 6 then on the next step we can take 4 and end up having 2 coins instead of 3 (2 coins {5, 4}).



- **4b.** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.




- **4c.** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?


  ----


- **5a.**



- **5b.**




- **5c.**
