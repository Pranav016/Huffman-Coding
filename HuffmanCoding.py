class Huffman:
    def __init__(self,path):
        self.path=path
    
    def make_freq_dict(self,text):
        freq_dict={}
        for w in text:
            freq_dict[w]=freq_dict.get(w,0)+1
        return freq_dict

    def compression(self):
        text="erewryhxcvbd"
        
        # making freq dict
        freq_dict=self.make_freq_dict(text)

