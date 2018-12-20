"""
Helpers module to auxiliary functions

"""


def initial_msg(size):
    """
    Print the initial message
    :param size: The length of files list
    :return: Print message
    """
    if size > 0:
        msg = 'Start Download the files from Space Weather Data Share API'
    else:
        msg = 'This search didn\'t find files from Space Weather Data Share API'

    total = 'Total: ' + str(size) + ' file(s)'

    print("""
    *****************************************************
    
    {}
    {}
    
    *****************************************************
    """.format(msg, total))


def final_msg(path):
    """
    Print the final message
    :param path: Path to save the files
    :return: Print message
    """
    print("""

    *****************************************************

    Done! All files are in your path {}
    """.format(path))
