import hdlparse.verilog_parser as vlog
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

MODULE_PATH = "TestFiles/Test1.v"

# HDL Parse Declarations
vlog_ex = vlog.VerilogExtractor()
vlog_mods = vlog_ex.extract_objects_from_source(MODULE_PATH)

with open(MODULE_PATH, 'rt') as fh:
    code = fh.read()
vlog_mods = vlog_ex.extract_objects(MODULE_PATH)


print('\n')
print('`timescale 1ns/1ps')
for m in vlog_mods:
    print('Module {}'.format(m.name), '_tb ();')
    for p in m.ports:
        if p.mode == 'input':
            print('\t{:8}{};'.format("reg", p.name))
        else:
            print('\t{:8}{};'.format("wire", p.name))
    print('\ninitial begin')
    print('\t$dumpfile(testbench.vcd);')

    for p in m.ports:
        print('\t{}{}{}'.format(p.name, ' = ', randint(0, 10)))
    print('$dumpvars;')
    print('end\nendmodule')


# with open('testbench.txt', 'w') as f:
