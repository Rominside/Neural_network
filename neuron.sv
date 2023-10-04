

module Neurone();
    //------INPUTS------
    input clk;
    input wire [8:0][8:0] weight;
    input wire [8:0][8:0] inputs;
    input wire start;
    //------OUTPUTS-----
    output [8:0] out;
    //------LOGICS______
    reg [8:0] reg_out;
    reg [3:0] i;

    always_comb @(clk and start) begin
        if (i < 4'b1010) begin
            reg_out = reg_out + weight[i] * inputs[i];
        end
        i = i + 1;
    end

    assign out = reg_out;

    initial begin
        reg_out = 8'b00000000;
        i = 1'b0;
    end

endmodule



