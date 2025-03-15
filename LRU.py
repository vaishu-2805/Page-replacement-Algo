def accept():
    PageStr= list(map(int,input("Enter A string of pages (comma(,) seperated): ").split(',')))
    FrameSize = int(input("Eneter a Frame size of memory: "))
    return PageStr, FrameSize

def LRU(PageStr, Framesize):
    FrameContent= []
    PageFault= 0
    for page in PageStr:
        if page not in FrameContent:
            if len(FrameContent)< Framesize:
                FrameContent.append(page)
            else:
                FrameContent.pop(0)
                FrameContent.append(page)
            PageFault+=1
        else:
            FrameContent.remove(page)
            FrameContent.append(page)
        print(f"Content of memory: {FrameContent}")
    print(f"Total Page Faults: {PageFault}")

PageStr, FrameSize= accept()
LRU(PageStr,FrameSize) 