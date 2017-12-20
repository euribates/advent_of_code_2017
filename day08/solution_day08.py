#!/usr/bin/env python3

import re
from collections import defaultdict

pat_cmd = re.compile('([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (<|<=|>|>=|==|!=) (-?\d+)')

registers = defaultdict(int)
all_values = []

class CMD:

    def __init__(self, line):
        m = pat_cmd.match(line)
        if not m:
            raise ValeuError('line "{}" doesn\'t match'.format(line))
        self.name = m.group(1)
        self.cod_op = m.group(2)
        self.value = int(m.group(3))
        self.target = m.group(4)
        self.cmp_op = m.group(5)
        self.cmp_value = int(m.group(6))

    def __repr__(self):
        buff = [
            self.name,
            '[{:d}]'.format(registers[self.name]),
            self.cod_op,
            str(self.value),
            self.target,
            '[{:d}]'.format(registers[self.target]),
            self.cmp_op,
            str(self.cmp_value)
        ]
        return ' '.join(buff)

    def evaluate(self):
        op1 = registers[self.target]
        if self.cmp_op == '==':
            return op1 == self.cmp_value
        if self.cmp_op == '!=':
            return op1 != self.cmp_value
        if self.cmp_op == '<=':
            return op1 <= self.cmp_value
        if self.cmp_op == '<':
            return op1 < self.cmp_value
        if self.cmp_op == '>=':
            return op1 >= self.cmp_value
        if self.cmp_op == '>':
            return op1 > self.cmp_value
        else:
            raise ValueError("Bad compare operator")

    def execute(self):
        if self.evaluate():
            if self.cod_op == 'inc':
                registers[self.name] = registers[self.name] + self.value
            elif self.cod_op == 'dec':
                registers[self.name] = registers[self.name] - self.value
            else:
                raise ValueError("Bad operation")
            all_values.append(registers[self.name])



# with open('test_data.txt', 'r') as f:
with open('data.txt', 'r') as f:
    lines = [s.strip() for s in f if s.strip()]

for line in lines:
    cmd = CMD(line)
    print(repr(cmd))
    cmd.execute()
else:
    print('All is ok')

print('Registers')
for name in registers:
    print('{} : {}'.format(name, registers[name]))

print('sol. 1:', max(registers.values()))
print('sol. 2:', max(all_values))
