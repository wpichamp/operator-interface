@echo off
title .ui to .py converter
pyuic5 gui_view.ui -o gui_view.py
echo converting .ui file to .py file