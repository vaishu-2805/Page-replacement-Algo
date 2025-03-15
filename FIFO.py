def accept():
    refStr= list(map(int,input("Enter a string of Pages : (Comma (,) seperated) ::").split(',')))
    FrameSize= int(input("Ebter a frame size of memory: "))
    return refStr , FrameSize

def FIFO(refStr, FrameSize):
    FrameContent=[]
    PageFault=0
    for page in refStr:
        if page not in FrameContent:
            if len(FrameContent)<FrameSize:
                FrameContent.append(page)
            else:
                FrameContent.pop(0)
                FrameContent.append(page)
            PageFault+=1
        print(f"Content of Memory:{FrameContent} ")
    print(f"Total Page Fault : {PageFault}")


refStr, FrameSize = accept()
FIFO(refStr,FrameSize)