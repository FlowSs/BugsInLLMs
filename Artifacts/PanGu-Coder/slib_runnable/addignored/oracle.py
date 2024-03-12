import subprocess
def addignored(ignored):
    ''' Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.'''
    fldr=subprocess.run(["git", "-C", ignored, "status", "-s", "--ignored"], capture_output=True, text=True).stdout.strip("\n")
    x = fldr.splitlines()
    sub = "!"
    g = ([s for s in x if sub in s])
    i = [elem.replace(sub, '') for elem in g]
    t = ", ".join(i)
    return t
