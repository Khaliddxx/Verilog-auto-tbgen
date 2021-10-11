import hdlparse.verilog_parser as vlog
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

# HDL Parse Declarations
vlog_ex = vlog.VerilogExtractor()
vlog_mods = vlog_ex.extract_objects_from_source('example.v')

with open('example.v', 'rt') as fh:
  code = fh.read()
vlog_mods = vlog_ex.extract_objects_from_source(code)

vlog_mods = vlog_ex.extract_objects('example.v')


print ('\n')
print('`timescale 1ns/1ps')
for m in vlog_mods:
  print('Module {}'.format(m.name),'_tb')
  print('(')
  for p in m.generics:
   # f.write('\t{:20}{:8}{}'.format("reg", p.name, p.mode, p.data_type))
    print('\t{:20}{:8}{},'.format(p.name, p.mode, p.data_type))
  print(');')
  
        
  for p in m.ports:
    if p.mode== 'input':
      print('\t{:20}{:8}{}'.format("reg", p.name, p.mode, p.data_type))
    else:
      print('\t{:20}{:8}{}'.format("wire", p.name, p.mode, p.data_type))


print ('\n')
with open('testbench.txt', 'w') as f:
  f.write('Module "{}":'.format(m.name))
  for m in vlog_mods:
    
      f.write('\t{:20}{:8}{}'.format("reg", p.name, p.mode, p.data_type))

# generate some integers
  print('initial begin')
  for p in m.generics:
    print('\t{:20}{:8}{}'.format(p.name, '=', randint(0, 10)))
  print('$monitor()')
print('end\n','endmodule')