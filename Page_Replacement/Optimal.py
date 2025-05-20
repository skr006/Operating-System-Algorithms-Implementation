class Optimal:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = []

    def page_in(self, pages):
        c=0
        for i in range(len(pages)):
            if pages[i] not in self.frames:
                if len(self.frames) < self.frame_count:
                    self.frames.append(pages[i])
                    self.display_frames()
                else:
                    key=self._find_optimal_replacement(pages,i)
                    self.frames.pop(key)
                    self.frames.insert(key,pages[i])
                    self.display_frames()
                    c+=1

        print("PDF",c)
        return c

    def _find_optimal_replacement(self, pages:list,i:int):
        a=pages[i+1::1]
        if self.frames[0] in a:
            x=a.index(self.frames[0])
        else:
            return 0
        for j in self.frames:
            if j not in a:
                
                return self.frames.index(j)
            if x<a.index(j):
                x=a.index(j)
        x=a[x]
        x=self.frames.index(x)
        return x

    def display_frames(self):
        print("Optimal frames:", self.frames)



# Driver code

frame=5
optimal=Optimal(frame)
pages=[1, 4, 2, 5, 3, 2, 4, 6, 5, 2, 3, 4, 3, 5, 2, 1, 6, 5, 1, 2]
print("Optimal Page Replacement Algorithm")
print("Pages:", pages)
print("Frame Count:", frame)
optimal.page_in(pages)
