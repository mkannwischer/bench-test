#!/bin/env python3
import random



v = [
    {
        "name": "keygen",
        "unit": "cycles",
        "value": random.randint(0,10000)
    },
    {
        "name": "encaps",
        "unit": "cycles",
        "value": random.randint(0,10000)
    },
    {
        "name": "decaps",
        "unit": "cycles",
        "value": random.randint(0,10000)
    },
]

print(v)