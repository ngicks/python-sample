import json
import os


with open(
    os.path.dirname(os.path.abspath("__file__")) + "/python_sample/sample.json",
    "r",
    encoding="utf-8",
) as f:
    j = json.load(f)
    print(j)

import cowsay

print(cowsay.get_output_string("trex", "Hello (extinct) World"))
