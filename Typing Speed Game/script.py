from time import time # Zamanı kaydetmek için

def tperror(prompt):
    global inwords

    words = prompt.split()
    errors=0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i+1]) & (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors = errors + 1
            else:
                errors += 1
    return errors

# Zaman hesaplayıcı çağırıyoruz
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

def elapsedtime(stime,etime):
    time = etime - stime # etime = end time, stime = start time
    return time

if __name__ == '__main__':
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
    # yazmamız istenen ve kontrol edeceğimiz cümle
    print("Type this : -- ",prompt)

    input("Press enter when you are ready to chck your speed !!!")

    # recording time
    stime = time()
    inprompt = input()
    etime = time()


    # collect all the information returned by the functions

    time = round(elapsedtime(stime,etime),2) # round off the time
    speed = speed(inprompt,stime,etime)
    errors = tperror(prompt)

    # printin all the required data to see result
    print("######################################################################")
    print("###Total time elapsed : ", time, " seconds")
    print("###Your Average Typing speed was ", speed, " words per minute(w/m)")
    print("###With the total of ", errors, " errors")
    print("######################################################################")
