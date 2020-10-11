import heapq

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.freq < other.freq

    def __eq__(self,other):
        return self.freq == other.freq


class Huffman:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
    
    def make_freq_dict(self,text):
        freq_dict={}
        for w in text:
            freq_dict[w]=freq_dict.get(w,0)+1
        return freq_dict

    def build_heap(self,freq_dict):
        for key,value in freq_dict:
            treeNode=BinaryTreeNode(key,value)
            heapq.heappush(self.heap,treeNode) # by default heapq makes a Min Heap
            # now we need to tell the computer that it needs to compare freq in the min heap, for that we overload a func __lt__ (less than)

    def build_tree(self):
        while len(self.heap)>1:
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)
            freq_sum=node1.freq+node2.freq # storing sum of freq of two leaf nodes
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=node1
            newNode.right=node2
            heapq.heappush(self.heap,newNode) # push the new node to the heap
        return 

    def build_codes_helper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None: # when i reach the leaf node, i store the codes.
            self.codes[root.value]=curr_bits # all the character and their freq are present at leaf nodes
            return
            
        self.build_codes_helper(root.left,curr_bits+"0")
        self.build_codes_helper(root.right,curr_bits+"1")

    def build_codes(self):
        root=heapq.heappop(self.heap)
        self.build_codes_helper(root,"")

    def get_encoded_text(self,text):
        encoded_text=""
        for char in text:
            encoded_text+=self.codes[char]
        return encoded_text


    def compression(self):
        text="erewryhxcvbd"
        
        # making freq dict
        freq_dict=self.make_freq_dict(text)

        # construct heap from freq_dict
        self.build_heap(freq_dict)

        # construct binary tree from heap
        self.build_tree()

        # converting the whole text to codes
        encoded_text=self.get_encoded_text(text)