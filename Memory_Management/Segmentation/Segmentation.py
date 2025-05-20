class Segment:
    def __init__(self, name, base, limit):
        self.name = name
        self.base = base
        self.limit = limit
        self.process_id = None

class Process:
    def __init__(self, pid, segments):
        self.pid = pid
        self.segments = segments
    def __str__(self):
        return f"Process ID: {self.pid}, Segments: {[(segment.name,segment.limit) for segment in self.segments]}\n"

class MemoryManager:
    def __init__(self):
        self.segments = []

    def add_segment(self, name, size):
        if self.segments:
            base = self.segments[-1].base + self.segments[-1].limit
        else:
            base = 0
        self.segments.append(Segment(name, base, size))

    def allocate_memory(self, process):
        for segment in process.segments:
            for existing_segment in self.segments:
                if existing_segment.process_id is None and existing_segment.limit >= segment.limit:
                    existing_segment.process_id = process.pid
                    segment.base = existing_segment.base
                    segment.limit = existing_segment.limit
                    break
            else:
                print(f"Error: Not enough memory for segment {segment.name} of Process {process.pid}")

    def deallocate_memory(self, process):
        for segment in process.segments:
            for existing_segment in self.segments:
                if existing_segment.process_id == process.pid:
                    existing_segment.process_id = None

    def print_memory_status(self):
        for segment in self.segments:
            print(f"Segment {segment.name}:\t Base={segment.base}\t| Limit={segment.limit}\t| Process ID={segment.process_id}")
        
        print("\n")


# Driver code


memory_manager = MemoryManager()

memory_manager.add_segment("Text", size=1024)
memory_manager.add_segment("Data", size=2048)
memory_manager.add_segment("Stack", size=512)
memory_manager.add_segment("Text", size=1024)
memory_manager.add_segment("Data", size=2048)
memory_manager.add_segment("Stack", size=512)


process1 = Process(pid=1, segments=[Segment("Text", 0, 256), Segment("Data", 0, 512), Segment("Stack", 0, 128)])
process2 = Process(pid=2, segments=[Segment("Text", 0, 512), Segment("Data", 0, 1024), Segment("Stack", 0, 256)])

print(process1)
print(process2)

print("Allocation of memory for Process 1 and Process 2:")
memory_manager.allocate_memory(process1)
memory_manager.allocate_memory(process2)

memory_manager.print_memory_status()

print("\nDeallocation of memory for Process 1:")

memory_manager.deallocate_memory(process1)

memory_manager.print_memory_status()
