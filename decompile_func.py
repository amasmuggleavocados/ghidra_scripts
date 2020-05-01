"""
Usage:

./analyzeHeadless [GHIDRA WORKING DIR] [PROJECT NAME] -import [BINARY] -overwrite \
-postscript decompile_func.py [FUNCTION] [OUTPUT DIR]

"""

import os
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

args = getScriptArgs()
print("[+] Decompiling '{}' now...".format(args[0]))

program = getCurrentProgram()
decompiface = DecompInterface()
decompiface.openProgram(program)

func = getGlobalFunctions(args[0])[0]
res = decompiface.decompileFunction(func, 0, ConsoleTaskMonitor())

if not os.path.exists(args[1]):
	os.makedirs(args[1])

fname = "{}/{}.c".format(args[1], args[0])
f = open(fname, 'w')
f.write(res.getDecompiledFunction().getC())
f.close()
