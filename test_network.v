

module test_neuron();
    reg clk;
    reg start_;
    reg signed [32:0] inputs [8:0][99:0];
    reg signed [32:0] weight [8:0];
    wire signed [33:0] out;
    wire end_;

    always #10 begin
        clk = ~clk;
    end

    always #10 begin
        start_ = 0;
    end

    Network network_1(.clk(clk),
                      .input_0(inputs[0]), .input_1(inputs[1]), .input_2(inputs[2]),
                      .input_3(inputs[3]), .input_4(inputs[4]), .input_5(inputs[5]), .input_6(inputs[6]),
                      .input_7(inputs[7]), .input_8(inputs[8]),
                      .start(start_), .out_2(out), .end_2(end_));

    initial begin
        clk = 0;
        start_ = 1;
    //-------DATA-------
        for (i = 0; i < 100; i = i + 1) begin
            for (j = 0; j < 10; j = j + 1) begin
                inputs[i][j] = $fopen("date.txt", "r");
            end
        end
        $fopen();
    end

endmodule