# Verilog-auto-tbgen
Automatic generator for verilog testbenches: A utility that gets a Verilog module (MUV) and generates a testbench skeleton.



# How to use the tool
The program can be invoked from the command line by using:
```tbgen -rand input_verilog_file_name```
where the input file is a verilog module, and the flag ```-rand``` is an optional random values assignment to all registers, one register at a
time every fixed amount of time (parameterized). 


# Dependencies
HDL Parser https://kevinpt.github.io/hdlparse/


# Code structure
### General Specifications
- Module file prefixed with _tb
- Timeframe 1ns/1ps
- Invoke command by: tbgen [-rand] input_filename
- Dumping changes in .vcd file


#### Parameters
- Clk, rst
- Clock period
- Reset assertion duration
- Termination time
- I/O



### Pseudo Code
- If (sequential) “clk/rst” ? Generate clock 
- Connect input ports to reg variables
- Connect output ports to wires
- Assign register values = 0
- [optional] assign random values to input registers
- 1 register per time interval
- Add “$monitor()” to output the signal changes
- Dump testbench to stdout



# Problems
