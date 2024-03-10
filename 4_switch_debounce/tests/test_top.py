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
async def top_test(dut):
    """
    test the output filter

    note that DEBOUNCE_LIMIT is set to 30 in tests/Makefile
    """
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"
    await Timer(5, units="ns")
    await FallingEdge(dut.i_Clk)  # wait for falling edge/"negedge"

    # toggle input
    dut.i_Switch_1.value = 0

    await FallingEdge(dut.i_Clk)
    await FallingEdge(dut.i_Clk)
    assert dut.i_Switch_1.value[0] == 0, "i_Switch_1 is not 0!"

    # toggle input
    dut.i_Switch_1.value = 1

    await FallingEdge(dut.i_Clk)
    await FallingEdge(dut.i_Clk)
    assert dut.i_Switch_1.value[0] == 1, "i_Switch_1 is not 1!"

    # validate that output isn't set (enough time hasn't elapsed)
    assert dut.o_LED_1.value[0] == 0, "o_LED_1 is not 0!"

    # wait a bit (not enough to trigger the led)
    await Timer(25, units="ns")

    # validate that led isn't set (enough time hasn't elapsed)
    assert dut.o_LED_1.value[0] == 0, "o_LED_1 is not 0!"

    # wait more than DEBOUNCE_LIMIT
    await Timer(50, units="ns")

    # validate that output is high
    assert dut.w_Debounced_Switch.value[0] == 1, "o_LED_1 is not 1!"
