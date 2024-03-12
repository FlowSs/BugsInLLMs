import os
def is_gitbash():
    """
    returns True if you run in a Windows gitbash

    :return: True if gitbash
    """
    try:
        exepath = os.environ['EXEPATH']
        return "Git" in exepath
    except:
        return False
