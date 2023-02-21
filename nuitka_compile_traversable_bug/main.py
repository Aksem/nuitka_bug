from importlib.resources import files


if __name__ == '__main__':
    traversable = files("nuitka_compile_traversable_bug")
    print(traversable / 'dir')
