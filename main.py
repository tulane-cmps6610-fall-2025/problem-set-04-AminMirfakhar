import math, queue
from collections import Counter
import numpy as np

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data[0] < other.data[0])
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

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


# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    if code is None:
        code = {}

    if node is None:
        return code

    if node.left is None and node.right is None:
        code[node.data[1]] = prefix
        return code

    get_code(node.left, prefix + "0", code)
    get_code(node.right, prefix + "1", code)
    return code


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    n = len(f) 
    bits_per_char = math.ceil(math.log2(n)) if n > 0 else 0
    total_chars = sum(f.values())
    return bits_per_char * total_chars


# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    total = 0
    for c in f.keys():
        total += f[c] * len(C[c])
    return total

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


if __name__ == "__main__":
    files = ['f1.txt', 'alice29.txt', 'asyoulik.txt', 'grammar.lsp', 'fields.c']
    
    FC = []
    HC = []
    
    for file in files:
        try:
            print(file)
            f = get_frequencies(file)
            print("Character frequencies:", f)
            print("Fixed-length cost:", fixed_length_cost(f))

            T = make_huffman_tree(f)
            C = get_code(T)
            print("Huffman codes:", C)
            print("Huffman cost:", huffman_cost(C, f))

            FC.append(fixed_length_cost(f))
            HC.append(huffman_cost(C, f))
            
            ratio = huffman_cost(C, f) / fixed_length_cost(f)
            print("Compression ratio (Huffman / Fixed): {:.2f}".format(ratio))
            
        except FileNotFoundError:
            print("Please make sure 'f1.txt' exists in the same directory.")
        
    print(np.mean(FC), np.mean(HC), np.mean(HC)/ np.mean(FC))
