

module test_neuron();
    reg clk;
    reg start_;
    reg signed [32:0] inputs [8:0];
    reg signed [32:0] weight [8:0];
    wire signed [33:0] out;
    wire end_;

    always #10 begin
        clk = ~clk;
    end

    always #10 begin
        start_ = 0;
    end

    Neurone neurone_1(.clk(clk), .weight_0(weight[0]), .weight_1(weight[1]), .weight_2(weight[2]), .weight_3(weight[3]),
                      .weight_4(weight[4]), .weight_5(weight[5]), .weight_6(weight[6]), .weight_7(weight[7]),
                      .weight_8(weight[8]), .input_0(inputs[0]), .input_1(inputs[1]), .input_2(inputs[2]),
                      .input_3(inputs[3]), .input_4(inputs[4]), .input_5(inputs[5]), .input_6(inputs[6]),
                      .input_7(inputs[7]), .input_8(inputs[8]), .start_(start_), .out(out), .end_(end_));

    initial begin
        clk = 0;
        start_ = 1;
        inputs[0] = 1;
        inputs[1] = 2;
        inputs[2] = 3;
        inputs[3] = 4;
        inputs[4] = 5;
        inputs[5] = 6;
        inputs[6] = 7;
        inputs[7] = 8;
        inputs[8] = 9;       
        //------weight-----
        weight[0] = 14264025;
        weight[1] = 20602356;
        weight[2] = 62294483;
        weight[3] = -5274598;
        weight[4] = 61604893;
        weight[5] = -5720134;
        weight[6] = 27585557;
        weight[7] = -11946924;
        weight[8] = 17072096;
    end
    
endmodule