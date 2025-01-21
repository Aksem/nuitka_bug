import shutil
import sys
from pathlib import Path

import mypy


def post_build():
    output_dir = Path(__file__).parent.parent / 'main.dist'
    mypyc_id = "8357f96abe52477c085b__mypyc"

    lib_path = list(Path(__file__).parent.parent.glob(f'{mypyc_id}.*.*'))[0]
    shutil.copyfile(lib_path, output_dir / lib_path.name)


if __name__ == '__main__':
    post_build()
