import cocotb
from cocotb.triggers import FallingEdge, Timer


async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(10):
        dut.i_Clk.value = 0
        await Timer(1, units="ns")
        dut.i_Clk.value = 1
        await Timer(1, units="ns")


@cocotb.test()
async def my_second_test(dut):
    """Try accessing the design."""

    await cocotb.start(generate_clock(dut))  # run the clock "in the background"

    await Timer(5, units="ns")  # wait a bit
    await FallingEdge(dut.i_Clk)  # wait for falling edge/"negedge"

    dut._log.info("o_LED_1 is %s", dut.led_toggle_inst.o_LED_1.value)
    assert dut.led_toggle_inst.o_LED_1.value[0] == 0, "o_LED_1[0] is not 0!"
