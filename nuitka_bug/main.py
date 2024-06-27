from pathlib import Path

from black import reformat_one, WriteBack
from black.mode import Mode, TargetVersion
from black.report import Report

mode = Mode(target_versions=set([TargetVersion.PY311]))
report = Report()

reformat_one(
    src=Path(__file__),
    fast=False,
    write_back=WriteBack.YES,
    mode=mode,
    report=report,
)
