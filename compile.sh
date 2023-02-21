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
    nuitka_compile_traversable_bug/main.py
