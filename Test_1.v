
module addbit (
a      , 
b      , 
ci     , 
sum    , 
co       
);
input              clk       ; 
input  [15:0]      data_in   ; 
output [7:0]       count     ; 
inout              data_bi   ; 


input a;
input b;
input ci;

output sum;
output co;

wire  a;
wire  b;
wire  ci;
wire  sum;
wire  co;

assign {co,sum} = a + b + ci;

endmodule
