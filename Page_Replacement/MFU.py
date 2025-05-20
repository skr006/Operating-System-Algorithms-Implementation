class MFU:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []

    def page_in(self, pages):
        c=0
        for i in range(len(pages)):
            if pages[i] not in self.frames:
                if len(self.frames)<self.frame_count:
                    self.frames.append(pages[i])
                else:
                    key=self._MRF(pages,i)
                    q=self.frames.pop(key)
                    self.frames.insert(key,pages[i])
                    c+=1
                self.display_frames()
        print("Page Faults:",c)
        return c
    def _MRF(self, pages:list,i:int):
        a=pages[i+1::1]
        x=a.count(self.frames[0])
        
        f=self.frames[0]
        for j in self.frames:
            if x<a.count(j):
                x=a.count(j)
                f=j
        f=self.frames.index(f)
        return f

    def display_frames(self):
        print("MFU frames:", self.frames)



pages=[1, 4, 2, 5, 3, 2, 4, 6, 5, 2, 3, 4, 3, 5, 2, 1, 6, 5, 1, 2]
frame_count = 5
print("MFU Page Replacement Algorithm")
print("Pages:", pages)
print("Frame Count:", frame_count)
a=MFU(frame_count)
a.page_in(pages=pages)
