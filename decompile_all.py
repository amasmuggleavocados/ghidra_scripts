"""
Usage:

./analyzeHeadless [GHIDRA WORKING DIR] [PROJECT NAME] -import [BINARY] -overwrite \
-postscript decompile_all.py [OUTPUT PATH]

"""

import os
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

args = getScriptArgs()

program = currentProgram
decompinterface = DecompInterface()
decompinterface.openProgram(program);
functions = program.getFunctionManager().getFunctions(True)
for function in list(functions):
		print("[+] Decompiling '{}' now...".format(function))

		if not os.path.exists(args[0]):
			os.makedirs(args[0])			

		tokengrp = decompinterface.decompileFunction(function, 0, ConsoleTaskMonitor())

		fname = "{}/{}.c".format(args[0], str(function))
		f = open(fname, 'w')
		f.write(tokengrp.getDecompiledFunction().getC())
		f.close()
