from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], includes = ["sys", "PyQt5", "math"], include_files = ["GUI.ui", "colors/"])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('main.py', base=base)
]
setup(
    name='Calculator',
    version = '1.0',
    description = 'A PyQt Calculator',
    options = dict(build_exe = buildOptions),
    executables = executables
)