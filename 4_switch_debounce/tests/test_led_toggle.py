import cocotb
from cocotb.triggers import FallingEdge, RisingEdge, Timer


async def generate_clock(dut):
    """Generate clock pulses."""

    while(True):
        dut.i_Clk.value = 0
        await Timer(1, units="ns")
        dut.i_Clk.value = 1
        await Timer(1, units="ns")

async def toggle_switch(dut):
    await RisingEdge(dut.led_toggle_inst.i_Clk)  
    dut.led_toggle_inst.i_Switch_1.value = 1;
    await RisingEdge(dut.led_toggle_inst.i_Clk) 
    dut.led_toggle_inst.i_Switch_1.value = 0;
    await RisingEdge(dut.led_toggle_inst.i_Clk)
    await RisingEdge(dut.led_toggle_inst.i_Clk)

@cocotb.test()
async def toggle_test(dut):
    await cocotb.start(generate_clock(dut))  # run the clock "in the background"

    await RisingEdge(dut.led_toggle_inst.i_Clk)

    # led starts off
    assert dut.led_toggle_inst.o_LED_1.value[0] == 0, "o_LED_1[0] is not 0!"

    # toggle switch
    await toggle_switch(dut)

    # led should be on now 
    assert dut.led_toggle_inst.o_LED_1.value[0] == 1, "o_LED_1[0] is not 1!"

    # toggle switch
    await toggle_switch(dut)

    # led should be off now 
    assert dut.led_toggle_inst.o_LED_1.value[0] == 0, "o_LED_1[0] is not 0!"
