import os
import platform


def clear():
    if os_detected() != "Windows":
        os.system('clear')
    else:
        os.system('cls')
        """
        flush function in terminal.  @link{ https://www.zhihu.com/question/293719659 }
        """


def os_detected():
    """
    platform detected by python libs <platform> @link{ https://blog.csdn.net/gatieme/article/details/45674367 }
    """
    return platform.system()