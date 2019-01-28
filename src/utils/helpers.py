"""
Helpers module to auxiliary functions

"""
import getopt
import sys


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


def help_msg():
    print("""
    ** Filters
    
    -a --app = An integer Application ID (Required)
    -s --station = An integer Station ID (Optional)
    -r --resolution = An integer  Resolution ID (Optional)
    -f --filter = An integer  Filter ID (Optional)
    -t --type = An integer  Type ID (Optional)
    -n --network = An integer  Network ID (Optional)
    -q --equipment = An integer  Equipment ID (Optional)

    ** Dates
    -i --start_date = A string with format yyyy-mm-dd (Required)
    -e --end_date = A string with format yyyy-mm-dd (Required)

    ** Path to save the files
    -p --path = A string with the a absolute path to save the files (Required)

    """)


def get_sys_args(argv):
    try:
        options, args = getopt.getopt(argv, "hHa:s:r:i:e:p:f:t:n:q:", [
            "help",
            "app=",
            "station=",
            "resolution=",
            "filter=",
            "type=",
            "network=",
            "equipment="
            "start_date=",
            "end_date=",
            "path="
        ])
    except getopt.GetoptError as error:
        print(error)
        sys.exit(2)

    search = {}
    for opt, arg in options:
        if opt in ('-h', '-H', '--help'):
            help_msg()
            sys.exit()
        elif opt in ("-a", "--app"):
            search['application'] = arg
        elif opt in ("-s", "--station"):
            search['station'] = arg
        elif opt in ('-r', '--resolution'):
            search['resolution'] = arg
        elif opt in ('-f', '--filter'):
            search['swfilter'] = arg
        elif opt in ('-t', '--type'):
            search['swtype'] = arg
        elif opt in ('-n', '--network'):
            search['network'] = arg
        elif opt in ('-q', '--equipment'):
            search['equipment'] = arg
        elif opt in ('-i', '--start_date'):
            search['start_date'] = arg
        elif opt in ('-e', '--end_date'):
            search['end_date'] = arg
        elif opt in ('-p', '--path'):
            search['path_to_save'] = arg

    path = search['path_to_save']
    del search['path_to_save']
    separator = [search, path]
    return separator
