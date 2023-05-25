if __name__ == '__main__':
    for changes in (((1, 'path11'),), ((2, 'path2'),), ((2, 'path3'),)):
        print('Iteration', changes)
        filtered_items = set(
            [
                change
                for change in changes
                if any(
                    change[1].endswith(suffix)
                    for suffix in [".txt", ".toml"]
                )
            ]
        )
