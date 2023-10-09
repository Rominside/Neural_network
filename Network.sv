module Network ();
    //------INPUTS------
    input clk;
    input start;
    input [8:0][8:0] inputs_0;
    //------OUTPUTS-----
    output [8:0] out_2_1;
    //------LOGICS______
    wire [8:0][8:0] inputs_1;
    wire [8:0][8:0] inputs_2;

    //--------------------Layer_0------------------------
    wire end_0_1;
    wire end_0_2;
    wire end_0_3;
    wire end_0_4;
    wire end_0_5;
    wire end_0_6;
    wire end_0_7;
    wire end_0_8;
    wire end_0_9;
    wire [8:0] out_0_1;
    wire [8:0] out_0_2;
    wire [8:0] out_0_3;
    wire [8:0] out_0_4;
    wire [8:0] out_0_5;
    wire [8:0] out_0_6;
    wire [8:0] out_0_7;
    wire [8:0] out_0_8;
    wire [8:0] out_0_9;
    Neurone_0_1 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_1), .end_(end_0_1));
    Neurone_0_2 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_2), .end_(end_0_2));
    Neurone_0_3 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_3), .end_(end_0_3));
    Neurone_0_4 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_4), .end_(end_0_4));
    Neurone_0_5 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_5), .end_(end_0_5));
    Neurone_0_6 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_6), .end_(end_0_6));
    Neurone_0_7 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_7), .end_(end_0_7));
    Neurone_0_8 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_8), .end_(end_0_8));
    Neurone_0_9 Neurone(.clk(clk), .start(start), .weight(), .inputs(inputs_0), .out(out_0_9), .end_(end_0_9));

    assign inputs_1 = out_0_1 + out_0_1 + out_0_1 + out_0_1 + out_0_1 +
                      out_0_1 + out_0_1 + out_0_1 + out_0_1;

    //--------------------Layer_1------------------------
    wire end_1_1;
    wire end_1_2;
    wire end_1_3;
    wire end_1_4;
    wire end_1_5;
    wire end_1_6;
    wire end_1_7;
    wire end_1_8;
    wire end_1_9;
    wire [8:0] out_1_1;
    wire [8:0] out_1_2;
    wire [8:0] out_1_3;
    wire [8:0] out_1_4;
    wire [8:0] out_1_5;
    wire [8:0] out_1_6;
    wire [8:0] out_1_7;
    wire [8:0] out_1_8;
    wire [8:0] out_1_9;
    Neurone_1_1 Neurone(.clk(clk), .start(end_0_1), .weight(), .inputs(inputs_1), .out(out_1_1), .end_(end_1_1));
    Neurone_1_2 Neurone(.clk(clk), .start(end_0_2), .weight(), .inputs(inputs_1), .out(out_1_2), .end_(end_1_2));
    Neurone_1_3 Neurone(.clk(clk), .start(end_0_3), .weight(), .inputs(inputs_1), .out(out_1_3), .end_(end_1_3));
    Neurone_1_4 Neurone(.clk(clk), .start(end_0_4), .weight(), .inputs(inputs_1), .out(out_1_4), .end_(end_1_4));
    Neurone_1_5 Neurone(.clk(clk), .start(end_0_5), .weight(), .inputs(inputs_1), .out(out_1_5), .end_(end_1_5));
    Neurone_1_6 Neurone(.clk(clk), .start(end_0_6), .weight(), .inputs(inputs_1), .out(out_1_6), .end_(end_1_6));
    Neurone_1_7 Neurone(.clk(clk), .start(end_0_7), .weight(), .inputs(inputs_1), .out(out_1_7), .end_(end_1_7));
    Neurone_1_8 Neurone(.clk(clk), .start(end_0_8), .weight(), .inputs(inputs_1), .out(out_1_8), .end_(end_1_8));
    Neurone_1_9 Neurone(.clk(clk), .start(end_0_9), .weight(), .inputs(inputs_1), .out(out_1_9), .end_(end_1_9));

    assign inputs_2 = out_1_1 + out_1_2 + out_1_3 + out_1_4 + out_1_5 +
                      out_1_6 + out_1_7 + out_1_8 + out_1_9;

    //--------------------Layer_2------------------------
    Neurone_2_1 Neurone(.clk(clk), .start(end_1_9), .weight(), .inputs(inputs_2), .out(out_2_1), .end_());

endmodule : Network