class LRU:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []
        self.freq=[]

    def page_in(self, pages):
        c = 0
        k=0
        for i in range(len(pages)):
            if pages[i] not in self.frames:
                if len(self.frames) < self.frame_count:
                    self.frames.append(pages[i])
                    self.updateFrequency()
                    self.freq.append(0)
                else:
                    m=self.freq.index(max(self.freq))
                    self.frames.pop(m)
                    self.frames.insert(m,pages[i])
                    self.updateFrequency()
                    self.freq[m]=0
                    c += 1
                self.display_frames()    
            else:
                self.updateFrequency()
                self.addfrequency(self.frames.index(pages[i]))
                # self.display_frames()
            
        return c

    def display_frames(self):
        print("LRU frames:", self.frames)
    
    def addfrequency(self,x):
        self.freq[x]=0
    def updateFrequency(self):
        for i in range(len(self.freq)):
            self.freq[i]+=1


# Driver code
frame_count = 5
pages = [1, 4, 2, 5, 3, 2, 4, 6, 5, 2, 3, 4, 3, 5, 2, 1, 6, 5, 1, 2]
print("LRU Page Replacement Algorithm")
print("Pages:", pages)
print("Frame Count:", frame_count)
a = LRU(frame_count)
a.page_in(pages)
