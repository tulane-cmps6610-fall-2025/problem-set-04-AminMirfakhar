# CMPS 6610 Problem Set 04
## Answers

**Name:**_________________________


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





- **2a.**




- **2b.**


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

    - 




- **3c.**  What is the work and span of your algorithm?

  - the process is similar to deviding N by 2 we repeat the process for the quotient in each step and keep the number of time we did this if remainder is equal to 1. So the number of that we can perform devision by 2 is equal to the work and span (since it is a sequential process) then it will at most take $\log{_2}{N}$. The other method is taking the int value of $\log{_2}{N}$ (k) then calculate the $N - 2^k$ and repeat this process. which again would take k times at most (k  = int($\log{_2}{N}$)).


----

- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
