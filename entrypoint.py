#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from github import Github


def main():
    for k, v in os.environ.items():
        print(k + ': ' + v)
    with open(os.environ['GITHUB_EVENT_PATH'], 'r') as f:
        print(f.read())


if __name__ == '__main__':
    main()
