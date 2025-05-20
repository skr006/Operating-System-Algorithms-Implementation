class Page:
    def __init__(self, page_number, size):
        self.page_number = page_number
        self.size = size
        self.is_allocated = False
        self.process_id = None
        self.frame_number=None

class Frame:
    def __init__(self, frame_number, size):
        self.frame_number = frame_number
        self.size = size
        self.is_allocated = False
        self.page_number = None

class process:
    def __init__(self,pid,size) -> None:
        self.size=size
        self.pid=pid

class MemoryManager:
    def __init__(self, total_frames, total_pages):
        print("Page and Frame size is 10 MB.\n")
        self.total_frames = total_frames
        self.total_pages = total_pages
        self.frames = [Frame(frame_number, size=10) for frame_number in range(total_frames)]
        self.pages = [Page(page_number, size=10) for page_number in range(total_pages)]

    def allocate_memory(self, process:process):
        allocated_pages = []
        num_pages = (process.size + 9) // 10  
        available_pages = [page for page in self.pages if not page.is_allocated]
        if len(available_pages) < num_pages:
            print("Error: Not enough memory available.")
            return allocated_pages

        for page in available_pages[:num_pages]:
            page.is_allocated = True
            frame = self._get_free_frame()
            if frame is None:
                print("Error: Not enough free frames available.")
                return allocated_pages

            frame.is_allocated = True
            frame.page_number = page.page_number
            page.frame_number = frame.frame_number
            page.process_id = process.pid
            allocated_pages.append(page)

        print(f"{num_pages} pages allocated for Process {process.pid} of size {process.size}.\n")
        return allocated_pages

    def deallocate_memory(self, process:process):
        deallocated_pages = [page for page in self.pages if page.is_allocated and page.process_id == process.pid]
        for page in deallocated_pages:
            page.is_allocated = False
            frame = self.frames[page.frame_number]
            frame.is_allocated = False
            frame.page_number = None
            page.frame_number = None
            page.process_id = None

        print(f"All pages allocated for Process {process.pid} deallocated.\n")
        return deallocated_pages

    def print_memory_status(self):
        print("Frames:")
        for frame in self.frames:
            print(f"Frame {frame.frame_number}: Allocated={frame.is_allocated} \t|\t Page Number={frame.page_number}")

        print("\nPages:")
        for page in self.pages:
            print(f"Page {page.page_number}: \tAllocated={page.is_allocated}\t| Frame Number={page.frame_number}\t| Process ID={page.process_id}")

    def _get_free_frame(self):
        for frame in self.frames:
            if not frame.is_allocated:
                return frame
        return None

memory_manager = MemoryManager(total_frames=10, total_pages=15)

process1 = process(pid=1, size=35)
process2 = process(pid=2, size=24)

allocated_pages = memory_manager.allocate_memory(process1)
memory_manager.allocate_memory(process2)
memory_manager.print_memory_status()
print("\n\n\n")
memory_manager.deallocate_memory(process1)
memory_manager.print_memory_status()

