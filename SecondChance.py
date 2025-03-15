from collections import deque

def accept():
    pageStr = list(map(int, input("enter a string of pageStr (comma (,) seperated): ").split(',')))
    frameSize = int(input("ente a frameSize: "))
    return pageStr, frameSize

def second_chance(pageStr, frameSize):
    mem = deque()      
    ref = {}           
    pageFault = 0         

    for p in pageStr:
        if p in ref:     # Page hit
            ref[p] = 1
        else:            # Page fault
            pageFault += 1
            if len(mem) < frameSize:  # Space available
                mem.append(p)
                ref[p] = 1
            else:                  # Memory full, evict a page
                while ref[mem[0]] == 1:
                    ref[mem[0]] = 0
                    mem.rotate(-1)
                del ref[mem.popleft()]
                mem.append(p)
                ref[p] = 1
        print(f"content of  Memory: {list(mem)}")
    
    print(f"pageFault: {pageFault}")

# Main execution
pageStr, frameSize = accept()
second_chance(pageStr, frameSize)