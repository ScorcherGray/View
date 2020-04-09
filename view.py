import sys
if __name__ == '__main__':
   args = sys.argv #Need to add default viewsize = 25
    #assert(len(args) == 3), "Incorrect arguments "

#print(args)
def view(fname, view_size=25):
    pages = [0]
    words = open(fname, "r")
    #Traverse the entire file collecing positions where each view_size begins
    words.seek(0,2)
    max = words.tell()
    if max == 0:
        print("File is empty!")
        sys.exit()
    words.seek(0)
    #Use fname.tell() to determine position
    while pages[-1] <= max:
        for i in range(view_size):
            words.readline()
            i += 1
        pages.append(words.tell())
        if pages[-1] == max: break
    pages.pop() #Removing the 'page' that starts at the end of the file
    #words.seek(pages[5])
    #print(max,  "\n", pages, '\n', words.read(pages[6] - pages[5]))
    #THEN display first page and give user "Command [u, d, t, b, #, q]: "
    statement = True
    words.seek(0)
    n = 0
    while statement:
        if n == len(pages)-1:
            words.seek(pages[n])
            text = words.read(max - pages[n])
            numlines = text.count('\n')
            print(f"[Page {len(pages)}]:\n", text)
            for i in range(numlines, view_size):
                print('')
        elif 0 < n < len(pages) - 1:
            words.seek(pages[n])
            text = words.read(pages[n+1] - pages[n])
            print(f"[Page {n+1}]:\n", text)
        else:
            n = 0
            words.seek(0)
            print(f"[Page {n+1}]:\n", words.read(pages[1]))
        userin = input("Command [u, d, t, b, #, q]: ")
        if userin.lower() == 'q':
            break
        elif userin.isdigit():
            n = int(userin)-1
        elif userin.lower() == 'u':
            if n > 0:
                n = n-1
            else:
                n = len(pages) -1
        elif userin.lower() == 'b':
            n = len(pages) - 1
        elif userin.lower() == 't':
            n = 0
        else:
            if n < len(pages):
                n = n + 1
            else:
                n = 0

    words.close()

filename = args[1]
#filename = 'yankee.txt'
if len(args) == 3:
    viewsize = int(args[2])
    view(filename, viewsize)
else:
    view(filename)
view(filename, 20)
#Teacher solution is 65 lines including white space.