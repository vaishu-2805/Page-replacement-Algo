from collections import defaultdict

def accept():
    pageStr = list(map(int, input("Enter pageStr (comma (,)separated): ").split(',')))
    FrameSize = int(input("Enter number of FrameSize: "))
    return pageStr, FrameSize

def LRU(pageStr, FrameSize):
    memory = []                  
    freq = defaultdict(int)      
    pageFault = 0                   

    for page in pageStr:
        if page not in memory:
            if len(memory) < FrameSize:
                memory.append(page) 
            else:
                least_used = max(memory, key=lambda x: freq[x])
                memory.remove(least_used)
                memory.append(page)
            pageFault += 1
        
        freq[page] += 1          
        print(f"content of  Memory: {memory} → Freq: {dict(freq)}")
    
    print(f"\nTotal pageFault: {pageFault}")


pageStr, FrameSize = accept()
LRU(pageStr, FrameSize)