# Huffman Coding
Huffman algorithm is a string compression algorithm. It helps us to reduce the size of string data.</br>

## Data Structures used-
*Tree
*HashMap
*Min Heap

## Theory
### Step-1:
* Make a frequency table for all the characters in the string.
### Step-2:
* Pick the two smallest frequencies and make their nodes in the tree.
* Make another nodes with their combined frequencies and add it to the tree as well as to the frequency table.
* Connect the two nodes to this node with combined frequencies.
### Step-3:
* Again pick two smallest frequencies and continue the process till all the frequencies in the table are used.
### Step-4:
* Add weights to the branches of the Tree. Add weight 0 to all the left branches and 1 to all the right branches.
### Step-5:
* We can then get a code for each character just by following the path on the resultant tree.
* Make a map using this.

## Decompression of codes:
* Use the map of codes for decompression of characters because these are prefix free codes hence decompression is easy.

