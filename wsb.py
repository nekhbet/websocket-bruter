import sys
import os
import threading
import urllib.request

print("WebSocket Bruter v0.1 - https://github.com/nekhbet/websocket-bruter")

# read CLI params
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-u", "--url", dest="url",
                    help="Target URL", required=True)
parser.add_argument("-t", "--threads",
                    dest="threads_number", default="10",
                    help="Threads to open")
args = parser.parse_args()

def open_url(url):
    try:
        urllib.request.urlopen(url, None, 30000)
    except:
        # ignore
        pass

class cli_colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def thread_function(url, index):
    print(cli_colors.YELLOW, "\tThread " + str(index) + " started")
    open_url(url)
    print(cli_colors.YELLOW, "\tThread " + str(index) + " ended")


print(cli_colors.BLUE + "Starting threads ")
for i in range(1, int(args.threads_number) + 1):
    print(cli_colors.GREEN, "Thread " + str(i))
    x = threading.Thread(target = thread_function, args=(args.url, i, ))
    x.start()
print(cli_colors.BLUE + "Done spawning")
