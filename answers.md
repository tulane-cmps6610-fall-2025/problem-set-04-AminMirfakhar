# CMPS 6610 Problem Set 04
## Answers

**Name:** Amin Mirfakhar


----


## Part 1: Fixed-Length vs. Variable-Length Codes

You saw the Huffman coding algorithm for data compresssion in our
course materials. Let's implement the algorithm and look at its
empirical performance on a dataset of 5 text files.

- **1a.** Already implemented is a means to compute character frequencies
  in a text file with the function `get_frequencies` in
  `main.py`. Compute cost for a fixed length encoding for each text
  file.


    ``` Python
    # given an alphabet and frequencies, compute the cost of a fixed length encoding
    def fixed_length_cost(f):
      n = len(f) 
      bits_per_char = math.ceil(math.log2(n)) if n > 0 else 0
      total_chars = sum(f.values())
      return bits_per_char * total_chars

  ```
  

- **1b.** Complete the implementation of Huffman coding in
  `make_huffman_tree`. Note that we manipulate binary trees in the
  priority queue using the object `TreeNode`. Moreover, once the tree
  is constructed, we must compute the actual encodings by traversing
  the Huffman tree that has been constructed. To do this, complete the
  implementation of `get_code`, which is a typical recursive binary
  tree traversal. That is, given a tree node, we recursively visit the
  left and right subtrees, appending a `0` or `1` to the encoding in
  each direction as appropriate. If we visit a leaf of the tree (which
  represents a character in the alphabet) we store the
  collected encoding for that character in `code`.

    ``` Python
  # given a dictionary f mapping characters to frequencies, 
  # create a prefix code tree using Huffman's algorithm
  def make_huffman_tree(f):
      p = queue.PriorityQueue()
      # construct heap from frequencies, the initial items should be
      # the leaves of the final tree
      for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))
  
      # greedily remove the two nodes x and y with lowest frequency,
      # create a new node z with x and y as children,
      # insert z into the priority queue (using an empty character "")
      while (p.qsize() > 1):
        left = p.get()
        right = p.get()
        freq_sum = left.data[0] + right.data[0]

        p.put(TreeNode(left, right, (freq_sum, "")))
          
      # return root of the tree
      return p.get()

  ```
  
 
- **1c.** Now implement `huffman_cost` to compute the cost of a Huffman
  encoding for a character set with given frequencies.


  ``` Python
  # given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
  def huffman_cost(C, f):
    total = 0
    for c in f.keys():
        total += f[c] * len(C[c])
    return total

  ```



- **1d.**  Test your implementation of Huffman coding on the 5 given text
files, and fill out a table of the encoding cost of each file for
fixed-length and Huffman. Fill out a final column which gives the
ratio of Huffman coding cost to fixed-length coding cost. Do you see a
consistent trend? If so, what is it?


|      File     | Fixed-Length Coding |  Huffman Coding | Huffman vs. Fixed-Length |
| :-------------: | :-------------: | :-------------: | :-------------: |
| f1.txt  | 1340  | 826  | 0.62  |
| alice29.txt  | 1039367  | 676374  | 0.65 |
| asyoulik.txt  | 876253 | 606448 | 0.69 |
| grammar.lsp  | 26047 | 17356 | 0.67  |
| fields.c  | 78050  | 56206  | 0.72 |
| **Average**  | **404211.4** | **271442.0** | **0.67** |

   - All the files got reduced about the 0.4 of their size. Maybe if we could see the context of all files together, we could minimize the files furthermore.
  
----


## Part 2: Binary Heaps

- **2a.** Give a method to construct a binary min-heap in $O(n)$
work. Hint: Given an array $A$ of elements, consider the implicit
representation as an
almost-complete binary tree and show how to achieve the heap
property for this tree with $O(n)$ work.

  - having the binary tree itself, we can start at bottom layer and look at each sub trees with a root and 2 leaves. then comparing the children to the parent tells us that we should swap them or not. in this case we should perform comparison as the number of edges, which is equal to
   $2^{\log{_2}{n}} = n$
.
   so the work would be O(n). (considering the work work for camparison and swapping in c*o(1)).


- **2b.** What is the span of your approach?
  - Since we can perform all the comparison between childrens at the same time, also all subtrees at each level could be checked together at the same time. then the span could be O($\log{n}$) equal to number of levels.


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

    - consider the case that N is equal is to 9 and the coins set is {1, 2, 4, 5, 6} then if we take the largest coin af first which is 6 then we have to take 2 and 1 in the next steps, since we don't have any other options (3 coins {6, 2, 1}). But if we take 5 at first instead of 6 then on the next step we can take 4 and end up having 2 coins instead of 3 (2 coins {5, 4}).



- **4b.** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.


  - Having the coins set fixed ($k$ denominations of values $D_0, D_2, \ldots, D_k$) the Optimal substructure stats that if the optimal solution for $Optimal(N)$ has for example $D_i$ in it then the problem of having $N - D_i$ should have an optimal solution itself meaning the minimum number of coins. Otherwise, replacing it with a better solution for that subproblem would yield fewer coins, contradicting optimality.


- **4c.** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?


    ``` Python

  def min_coins(N, D):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
      for d in D:
        if d <= i:
          dp[i] = min(dp[i], 1 + dp[i - d])
      return dp[N] if dp[N] != inf else None

    ```

  - Work: O(N × k), where k = number of denominations.
  - Span: O(N), since each state depends on previous ones sequentially.


If parallelized per d, the span can be reduced to O(log k) per iteration.


  ----

  ## Part 5: Weighted Task Selection

In class we gave a greedy algorithm for task scheduling. In that
problem, all tasks had equal value and the goal was to simply maximize
the total number of non-overlapping tasks. Suppose now that we
consider tasks $A= \{ a_0, \ldots, a_{n-1} \}$ where
each task $a_i$  has $(s_i, f_i, v_i)$, with start and finish times as
well as a value for completion. The goal now is to identify a set of
tasks with maximum value. 


- **5a.** Does the optimal substructure property hold for weighted task
selection? If so, prove it. If not, give a counterexample.



- **5b.** Does the greedy choice property hold for this problem? If so,
define a greedy criterion and prove that it satisfies the greedy
choice property. If you cannot, find at least two counterexamples of greedy
criteria that fail to achieve an optimal solution. 

  - The greedy choice property does not hold for weighted task selection. for example consider we have three task to schedule {A: (0, 3, 3), B: (3, 5, 4), C: (0, 5, 6)} then the greedy algorithm, to maximize the value, would take C having the most value. but the optimal selection is taking A and B with the total value of 7.
 
  - greedy by highest value/length ratio can also fail when a long task blocks multiple short valuable ones. 




- **5c.** Use the optimal substructure property of this problem to design a
  dynamic programming algorithm for this problem. Derive the work and span of your approach.


    ``` Python

    def weighted_task_selection(tasks):
      tasks.sort(key=lambda x: x[1])  # sort out the tasks by their ending time. W: O(n log n) S: O(log^2 n)
      n = len(tasks)
      p = compute_p(tasks) # precompute the last compatible task  W: O(n log n) S: O(log(n))
      OPT = [0]*(n+1) 
      for j in range(1, n+1): # creating substructure for DP W: O(n) S: O(n)
          OPT[j] = max(tasks[j-1][2] + OPT[p[j-1]], OPT[j-1])
      return OPT[n]

    ```

  - Work: O(n log n) for sorting + O(n log n) to find p(j) → overall O(n log n).
  - Span: O(n) if sorting and binary search are parallelized O(log n).

  
