# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:37:41 2021

@author: Juan Antonio

Title: launcher of server

ver: 1.0
"""

import os

def main():
    os.system('bokeh serve --show myapp.py')


if __name__ == "__main__":
    main()