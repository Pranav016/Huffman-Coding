import heapq
import os

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


class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.heap=[]
        self.codes={}
        self.reverse_mapping = {}
    
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
            self.reverse_mapping[curr_bits] = root.char
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

    def getPaddedEncodedText(self,encoded_text):
        num_padded=8-len(encoded_text)%8 #eg. we get (len(encoded_text)%8)=5 ; then we need to append (8-5)=3 0's at the end
        for i in range(num_padded):
            encoded_text+='0'
            i+=1
        padded_info="{0:08b}".format(num_padded) # means convert encoded text to 'b'-binary format in groups of 8 bits
        padded_encoded_text=padded_info + encoded_text
        return padded_encoded_text

    def getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            array.append(int(byte,2)) # convert to int of base 2

        return array

    def compress(self):
        file_name,file_extension=os.path.splitext(self.path)
        output_path=file_name+".bin"
        
        with open(self.path,'r+') as file , open(output_path, 'wb') as output:
            text=file.read()
            text=text.rstrip()

            # making freq dict
            freq_dict=self.make_freq_dict(text)

            # construct heap from freq_dict
            self.build_heap(freq_dict)

            # construct binary tree from heap
            self.build_tree()

            # converting the whole text to codes
            encoded_text=self.get_encoded_text(text)

            # pad the encoded text
            # we pad the encoded text to multiples of 8 because if we don't, the system will by itself add 0's when storing in terms of bits
            padded_encoded_text=self.getPaddedEncodedText(encoded_text)

            # getting the byter array of the padded text
            bytesArray=self.getBytesArray(padded_encoded_text)

            # returning bytes array
            final_array=bytes(bytesArray)
            output.write(final_array)

        print("compressed")
        return output_path

    def remove_padding(self,padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1*extra_padding]
        return encoded_text

    def decode_text(self,encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string =""
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            encoded_text = self.remove_padding(bit_string)
            decompressed_text = self.decode_text(encoded_text)
            output.write(decompressed_text)
        print("Decompressed")
        return output_path