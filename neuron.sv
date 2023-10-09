

module Neurone #(parameter weight_1, parameter weight_2, parameter weight_3, parameter weight_4,
                 parameter weight_5, parameter weight_6, parameter weight_7, parameter weight_8,
                 parameter weight_9);
    //------INPUTS------
    input clk;
    input wire start_;
    input wire [8:0][8:0] inputs;
    //------OUTPUTS-----
    output [8:0] out;
    output end_;
    //------LOGICS______
    reg reg_end_;
    integer reg_out;
    reg [3:0] state;

    always @(posedge start_) begin
        if (state != 0) begin
            state = 0;
        end
    end

    always @(posedge clk) begin
        case (state)
            0: begin
                reg_out = 0;
                reg_end_ = 0;
                state = state + 1;
            end
            1: begin
                if (weight_1 < 0) begin
                    weight_1 = - weight_1;
                    reg_out = reg_out - weight_1 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_1 * inputs[1];
                end
                state = state + 1;
            end
            2: begin
                if (weight_2 < 0) begin
                    weight_2 = - weight_2;
                    reg_out = reg_out - weight_2 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_2 * inputs[1];
                end
                state = state + 1;
            end
            3: begin
                if (weight_3 < 0) begin
                    weight_3 = - weight_3;
                    reg_out = reg_out - weight_3 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_3 * inputs[1];
                end
                state = state + 1;
            end
            4: begin
                if (weight_4 < 0) begin
                    weight_4 = - weight_4;
                    reg_out = reg_out - weight_4 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_4 * inputs[1];
                end
                state = state + 1;
            end
            5: begin
                if (weight_5 < 0) begin
                    weight_5 = - weight_5;
                    reg_out = reg_out - weight_5 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_5 * inputs[1];
                end
                state = state + 1;
            end
            6: begin
                if (weight_6 < 0) begin
                    weight_6 = - weight_6;
                    reg_out = reg_out - weight_6 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_6 * inputs[1];
                end
                state = state + 1;
            end
            7: begin
                if (weight_7 < 0) begin
                    weight_7 = - weight_7;
                    reg_out = reg_out - weight_7 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_7 * inputs[1];
                end
                state = state + 1;
            end
            8: begin
                if (weight_8 < 0) begin
                    weight_8 = - weight_8;
                    reg_out = reg_out - weight_8 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_8 * inputs[1];
                end
                state = state + 1;
            end
            9: begin
                if (weight_9 < 0) begin
                    weight_9 = - weight_9;
                    reg_out = reg_out - weight_9 * inputs[1];
                end
                else begin
                    reg_out = reg_out + weight_9 * inputs[1];
                end
                state = state + 1;
            end
            10: begin
                if (reg_out < 0) begin
                    reg_out = 0;
                end
                reg_end_ = 1;
            end
        endcase
    end

    assign out = reg_out;
    assign end_ = reg_end_;

    initial begin
        reg_end_ = 0;
        reg_out = 0;
        state = 0;
    end

endmodule : Neurone