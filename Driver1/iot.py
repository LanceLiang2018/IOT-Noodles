#!/usr/bin/python
# -*- coding:utf-8 -*-

from speech import Speech
import manege


def main():
    manege.init()
    s = Speech()
    s.record()
    dat = s.get_result()
    if dat != None:
        print(dat)
        manege.main(dat)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print('Connect Error.', e, 'Re connect...')

