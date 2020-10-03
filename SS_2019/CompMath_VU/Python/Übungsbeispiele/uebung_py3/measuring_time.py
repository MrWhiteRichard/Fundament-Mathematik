import time

def tic(): # start measuring time
    global start
    start = time.time()

def toc(): # end measuring time
    if 'start' in globals():
        print("time: {}.".format(str(time.time()-start)))
    else:
        print("toc(): start time not set")
