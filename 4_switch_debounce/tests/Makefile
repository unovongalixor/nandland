# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES += $(PWD)/../hdl/debounce_filter.vhd
VHDL_SOURCES += $(PWD)/../hdl/led_toggle.vhd
VHDL_SOURCES += $(PWD)/../hdl/top.vhd

TOPLEVEL = switch_debounce_top
MODULE = test_led_toggle

SIM_ARGS ?= --vcd=waveform.vcd

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
