import shutil
import sys
import site
from pathlib import Path

import mypy

def post_build():
    output_dir = Path(__file__).parent.parent / 'main.dist'
    mypyc_id = "3204bda914b7f2c6f497__mypyc"
    for sitepackage_path in site.getsitepackages():
        # black
        try:
            mypyc_file_str = next(p for p in Path(sitepackage_path).glob(f'{mypyc_id}.*.*'))
        except StopIteration:
            raise Exception("mypy lib not found")

    lib_path = Path(mypyc_file_str)
    shutil.copyfile(lib_path, output_dir / lib_path.name)


if __name__ == '__main__':
    post_build()
