#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def load_kernel():
    with open('input.txt', 'r') as f:
        return [ int(x.strip()) for x in f ]

k = load_kernel()
print(k[0:5])

class Processor():
    
    def __init__(self, memory):
        self.pos = 0
        self.memory = list(memory)[:]
        self._size = len(self.memory)
        self.counter = 0
    
    def exec(self):
        self.counter += 1
        data = self.memory[self.pos]
        self.memory[self.pos] += 1
        self.pos = self.pos + data
        return self.pos >= self._size
            
    def debug(self):
        print('- Iter. {:05d} [pos: {}]'.format(self.counter, self.pos), end=': ')
        for i, num in enumerate(self.memory):
            if i == self.pos:
                print('({})'.format(num), end=' ')
            else:
                print(num, end=' ')
        print()

# test
kernel = [0, 3, 0, 1, -3]
proc = Processor(kernel)
while True:
    proc.debug()
    last = proc.exec()
    if last:
        break
proc.debug()
print(proc.counter)

# Part One

proc = Processor(load_kernel())
while True:
    last = proc.exec()
    if last:
        break
print('Part 1:', proc.counter)

# Part Two

class Processor2(Processor):
    
    def exec(self):
        self.counter += 1
        data = self.memory[self.pos]
        if data >= 3:
            self.memory[self.pos] -= 1
        else:
            self.memory[self.pos] += 1
        self.pos = self.pos + data
        return self.pos >= self._size

# test
kernel = [0, 3, 0, 1, -3]
proc = Processor2(kernel)
while True:
    proc.debug()
    last = proc.exec()
    if last:
        break
proc.debug()        
print(proc.counter)

# real
proc = Processor2(load_kernel())
while True:
    last = proc.exec()
    if last:
        break
print('Part 2:', proc.counter)
