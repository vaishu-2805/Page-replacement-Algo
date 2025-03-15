def accept():
    PageStr= list(map(int,input("Enter a string of Pages (comma (,) seperates): ").split(',')))
    FrameSize= int(input("Enter a frame size of memory: "))
    return PageStr, FrameSize

def MRU(PageStr, Framesize):
    FrameContent=[]
    PageFault=0
    for page in PageStr:
        if page not in FrameContent:
            if len(FrameContent)<Framesize:
                FrameContent.append(page)
            else:
                FrameContent.pop(-1)
                FrameContent.append(page)
            PageFault+=1
        else:
            FrameContent.remove(page)
            FrameContent.append(page)
        print(f"Pages in memory: {FrameContent}")
    print(f"Total Page Fault: {PageFault}")

PageStr , Framesize = accept()
MRU(PageStr, Framesize)