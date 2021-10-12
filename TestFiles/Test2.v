module adder_implicit (
result, 
carry, 
r1, 
r2, 
ci              
);

input[3:0] r1;
input[3:0] r2;
input ci;

output[3:0] result;
output carry;

addbit u0 (
r1[0]           ,
r2[0]           ,
ci              ,
result[0]       ,
c1
);

addbit u1 (
r1[1]          ,
r2[1]          ,
c1             ,
result[1]      ,
c2
);

addbit u2 (
r1[2]          ,
r2[2]          ,
c2             ,
result[2]      ,
c3
);

addbit u3 (
r1[3]          ,
r2[3]          ,
c3             ,
result[3]      ,
carry
); 

endmodule 
