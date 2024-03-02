import cocotb
from cocotb.triggers import FallingEdge, Timer


async def generate_clock(dut):
    """Generate clock pulses."""

    while True:
        dut.i_Clk.value = 0
        await Timer(1, units="ns")
        dut.i_Clk.value = 1
        await Timer(1, units="ns")


@cocotb.test()
async def debounce_test(dut):
    """
    test the output filter

    note that DEBOUNCE_LIMIT is set to 30 in tests/Makefile
    """
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    await FallingEdge(dut.i_Clk)  # wait for falling edge/"negedge"

    # debounce filter output starts low
    assert dut.debounce_filter_inst.o_Debounced.value[0] == 0, "o_Debounced is not 0!"

    # toggle input
    dut.debounce_filter_inst.i_Bouncy.value = 1

    await FallingEdge(dut.i_Clk)
    assert dut.debounce_filter_inst.i_Bouncy.value[0] == 1, "i_Bouncy is not 1!"

    # validate that output isn't set (enough time hasn't elapsed)
    assert dut.debounce_filter_inst.o_Debounced.value[0] == 0, "o_Debounced is not 0!"

    # wait a bit (not enough to trigger the led)
    await Timer(25, units="ns")

    count = int(dut.debounce_filter_inst.r_Count.value)

    # validate that led isn't set (enough time hasn't elapsed)
    assert dut.debounce_filter_inst.o_Debounced.value[0] == 0, "o_Debounced is not 0!"

    # wait more than DEBOUNCE_LIMIT
    await Timer(50, units="ns")

    # validate that output is high
    assert dut.debounce_filter_inst.o_Debounced.value[0] == 1, "o_Debounced is not 1!"

