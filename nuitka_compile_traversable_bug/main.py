from importlib.resources import files
import json


if __name__ == '__main__':
    traversable = files("json")
    print(traversable / 'dir')
