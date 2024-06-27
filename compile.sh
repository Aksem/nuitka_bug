#!/bin/sh

#     --static-libpython=yes \
poetry run python -m nuitka \
    --clang \
    --standalone \
    --assume-yes-for-downloads \
    --plugin-enable=pylint-warnings \
    --warn-unusual-code \
    --warn-implicit-exceptions \
    --show-memory \
    --show-modules \
    --trace-execution \
    --include-module=black.brackets \
    --include-module=black.debug \
    --include-module=black.numerics \
    --include-module=black.rusty \
    --include-module=black.schema \
    --include-module=black.strings \
    --include-module=black.trans \
    --include-module=black._width_table \
    --include-module=blib2to3.pygram \
    --include-module=blib2to3.pgen2.conv \
    --include-module=blib2to3.pgen2.driver \
    --include-module=blib2to3.pgen2.grammar \
    --include-module=blib2to3.pgen2.literals \
    --include-module=blib2to3.pgen2.parse \
    --include-module=blib2to3.pgen2.pgen \
    --include-module=blib2to3.pgen2.tokenize \
    --include-package-data=blib2to3 \
    nuitka_bug/main.py
