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
    nuitka_async_iterator_bug/main.py
