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
            freq_sum=node1.freq+node2.freq
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=node1
            newNode.right=node2
            heapq.heappush(self.heap,newNode)
        return 

    def compression(self):
        text="erewryhxcvbd"
        
        # making freq dict
        freq_dict=self.make_freq_dict(text)

        # construct heap from freq_dict
        self.build_heap(freq_dict)

        # construct binary tree from heap
        self.build_tree()