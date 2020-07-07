from sys import *
import webbrowser
import re
import urllib
from urllib.request import urlopen
import urllib.error


def is_connected ():
    try:
        urllib.urlopen ( "http://www.google.com", timeout=1 )
        return True
    except urllib.error as err:
        return False


def find (string):
    """

    :param string:
    :return:
    """
    url = re.findall ( "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*, ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string )
    return url


def webLauncher (path):
    with open ( path ) as fp:
        for line in fp:
            print ( line )
            url = find ( line )
            print ( url )
            for str in url:
                webbrowser.open ( str, new=2 )


connected = is_connected ()
webLauncher ( "F:\\Python Programming\site.txt" )
