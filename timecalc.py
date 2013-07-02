#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@file
timecalc.py

@description
Simple time calculator

@license
The MIT License (MIT)
Copyright (c) 2013 Sergey A. Khasanov <s.a.khasanov@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

@example
$python timecalc.py 16:20 10:00 2:30 1:00
Result is = 2:50
'''

import sys

class Time:
    def __init__(self, time):
        h, m = time.split(":")
        self.hh, self.mm = int(h), int(m)

    def __str__(self):
        return "Result is = " + str(self.hh) + ":" + str(self.mm)

    def subtract(self, time):
        self.hh -= time.hh
        self.mm -= time.mm

        if (self.mm < 0):
            self.hh -= 1
            self.mm += 60
        elif (self.mm > 59):
            self.hh += 1
            self.mm -= 60
        return self
 
print reduce(lambda x, y: x.subtract(y), map(Time, sys.argv[1:]))
