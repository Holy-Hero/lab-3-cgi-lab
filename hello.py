#!/usr/bin/env python

import os
import json

print("Content-Type: application/json")
print()
print(json.dump(dict(os.environ), indent=2))