#!/bin/sh
rm -rf build dist && powershell.exe -Command python3.exe -m PyInstaller gui.py
