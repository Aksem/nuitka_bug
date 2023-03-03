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
    --include-package=nuitka_compile_dynamic_import_bug.custom_package \
    --include-module=nuitka_compile_dynamic_import_bug.custom_package.mod \
    nuitka_compile_dynamic_import_bug/main.py
