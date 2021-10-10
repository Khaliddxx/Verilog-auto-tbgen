import hdlparse.verilog_parser as vlog



vlog_ex = vlog.VerilogExtractor()
vlog_mods = vlog_ex.extract_objects_from_source('Test_1.v')

with open('Test_1.v', 'rt') as fh:
  code = fh.read()
vlog_mods = vlog_ex.extract_objects_from_source(code)

vlog_mods = vlog_ex.extract_objects('Test_1.v')

for m in vlog_mods:
  print('Module "{}":'.format(m.name))

  print('  Parameters:')
  for p in m.generics:
    print('\t{:20}{:8}{}'.format(p.name, p.mode, p.data_type))

  print('  Ports:')
  for p in m.ports:
    print('\t{:20}{:8}{}'.format(p.name, p.mode, p.data_type))


