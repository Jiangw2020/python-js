import math
import random
import requests
import time
import pywasm

vm = pywasm.load('猿人学web-20.wasm')

print(vm.exec('__wbindgen_add_to_stack_pointer', -16))
