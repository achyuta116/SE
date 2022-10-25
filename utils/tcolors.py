""" https://gist.github.com/nkilm/596f21416b8ce914eee4b0551adcba06 """

import os 

if (os.name=="nt"):
    # Fixes the issue of color not rendering in Windows Powershell/CMD
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'
    BPurple   = '\033[1;35m'
    BIPurple  = '\033[1;95m' # Bold High Intensity


    # To highlight important information
    # usage:
    #    print(bcolor.highlight("My important message"))
    @staticmethod
    def highlight(message:str):
      message = str(message)
      return bcolors.BOLD + message + bcolors.BOLD

    # Method that returns a message with the desired color
    # usage:
    #    print(bcolor.colored("My colored message", bcolor.OKBLUE))
    @staticmethod
    def colored(message:str, color):
      return color + message + bcolors.ENDC

    # Method that returns a yellow warning
    # usage:
    #   print(bcolors.warning("What you are about to do is potentially dangerous. Continue?"))
    @staticmethod
    def warning(message:str):
      return bcolors.WARNING + message + bcolors.ENDC

    # Method that returns a red fail
    # usage:
    #   print(bcolors.fail("What you did just failed massively. Bummer"))
    #   or:
    #   sys.exit(bcolors.fail("Not a valid date"))
    @staticmethod
    def fail(message:str):
      return bcolors.FAIL + message + bcolors.ENDC

    # Method that returns a green ok
    # usage:
    #   print(bcolors.ok("What you did just ok-ed massively. Yay!"))
    @staticmethod
    def ok(message:str):
      return bcolors.OKGREEN + message + bcolors.ENDC

    # Method that returns a blue ok
    # usage:
    #   print(bcolors.okblue("What you did just ok-ed into the blue. Wow!"))
    @staticmethod
    def okblue(message:str):
      return bcolors.OKBLUE + message + bcolors.ENDC

    # Method that returns a header in some purple-ish color
    # usage:
    #   print(bcolors.header("This is great"))
    @staticmethod
    def header(message:str):
      return bcolors.HEADER + message + bcolors.ENDC