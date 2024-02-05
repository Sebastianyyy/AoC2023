#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict
import re

if '__main__' == __name__:
    with open(file='input.txt') as f:
        lines = f.readlines()
    flops = defaultdict(list)
    conj = defaultdict(list)
    flip_states = {}
    conj_mem = defaultdict(dict)
    broadcasters = []
    for i in lines:
        pattern = r'(\w{2})'
        index = i.find('->')
        f = re.findall(pattern=pattern, string=i[index + 3:])
        if i.startswith('broadcaster'):
            broadcasters = f.copy()
        elif i.startswith('%'):
            flops[i[1:3]].extend(f.copy())
        elif i.startswith('&'):
            conj[i[1:3]].extend(f.copy())

    for i in flops.keys():
        flip_states[i] = 0
        for j in flops[i]:
            if j in conj.keys():
                conj_mem[j][i] = 0
        for (k, v) in conj.items():
            for j in v:
                if j in conj.keys():
                    conj_mem[j][k] = 0
    low = 0
    high = 0
    for _ in range(1000):
        q = [('broadcaster', 0, 'button')]
        while q:
            element = q.pop(0)
            (dst, signal, src) = element
            if signal == 1:
                high += 1
            else:
                low += 1
            if dst == 'broadcaster':
                for b in broadcasters:
                    q.append((b, signal, dst))
            elif dst in flops.keys():
                if signal == 0:
                    flip_states[dst] = 1 if flip_states[dst]==0 else 0
                    for new_dest in flops[dst]:
                        q.append((new_dest, flip_states[dst],dst))
            elif dst in conj.keys():
                conj_mem[dst][src] = signal
                snd = not all(v for v in conj_mem[dst].values())
                for new_dest in conj[dst]:
                    q.append((new_dest, snd, dst))
    print(low * high)
