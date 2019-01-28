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


def final_msg(path, countsuccess, countfail):
    """
    Print the final message
    :param countfail: An integer value
    :param countsuccess: An integer value
    :param path: Path to save the files
    :return: Print message
    """
    print("""

    *****************************************************
    Download success: {1}
    Download Failed: {2} 
    
    Done! {1} files are in your path {0}
    """.format(path, countsuccess, countfail))


def error_msg(file, error):
    """
    Print the error message
    :param error: Error message
    :param file: File name
    :return: Print message
    """
    print("""
    *** Failed: Something went wrong when trying to download the file "{}"
    *** Error message: {}    
    """.format(file, error))
