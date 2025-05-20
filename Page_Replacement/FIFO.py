class FIFO:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []

    def page_in(self, pages):
        x=0
        c=0
        for i in range(len(pages)):
            if pages[i] not in self.frames:
                if len(self.frames) == self.frame_count:
                    q=self.frames.pop(x)
                    self.frames.insert(x,pages[i])
                    x+=1
                    c+=1
                else:
                    self.frames.append(pages[i])
                self.display_frames()

            if x==self.frame_count:
                x=0
        return c

    def display_frames(self):
        print("FIFO frames:", self.frames)



# Driver code
pages=[1, 4, 2, 5, 3, 2, 4, 6, 5, 2, 3, 4, 3, 5, 2, 1, 6, 5, 1, 2]
frame_count = 5
print("FIFO Page Replacement Algorithm")
print("Pages:", pages)
print("Frame Count:", frame_count)
fifo = FIFO(frame_count)
fifo.page_in(pages)
