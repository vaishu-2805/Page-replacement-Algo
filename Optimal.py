def accept():
    PageStr = list(map(int, input("Enter page reference string (comma (,) separated): ").split(',')))
    FrameSize = int(input("Enter number of frames: "))
    return PageStr, FrameSize

def optimal_page_replacement(PageStr, FrameSize):
    FrameContent = []          
    pageFaults = 0

    for i, page in enumerate(PageStr):
        if page not in FrameContent:
            if len(FrameContent) < FrameSize:
                FrameContent.append(page)    
            else:
                replaceIdx = max(
                    range(len(FrameContent)),
                    key=lambda idx: PageStr[i+1:].index(FrameContent[idx]) 
                                 if FrameContent[idx] in PageStr[i+1:] 
                                 else len(PageStr)
                )
                FrameContent[replaceIdx] = page    
            pageFaults += 1
            
        print(f"Content of  Memory: {FrameContent}")
    
    print(f"\nTotal Page Faults: {pageFaults}")

PageStr, FrameSize = accept()
optimal_page_replacement(PageStr, FrameSize)