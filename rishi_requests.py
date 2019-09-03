#!/usr/bin/env python
import requests
from config import Url
import sys

def main():

    args = sys.argv[1:]
    if not args:
        url=Url
    else:
        url=args[0]

    response=requests.get(url)
    print(response)



if __name__ == '__main__':
    main()
