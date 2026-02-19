from sympy.physics.vector.printing import params

from sns_toolbox.backends import Backend
import json

def save(params: dict, filename: str) -> None:
    json.dump(params, open(filename,'w'))

def load(filename) -> dict:
    params = json.load(open(filename, 'r'))
    return params
