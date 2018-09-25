"""
Python 3.6
@Author: wrgsRay
"""
import json, requests, sys


def main():
    if len(sys.argv) < 2:
        print('Usage: quickWeather.py location')
        sys.exit()
    location = ' '.join(sys.argv[1:])

    # TODO: Download the JASOn data from OpenweatherMap.org's API

    # TODO: Load JSON data into Python variable.


if __name__ == '__main__':
    main()
