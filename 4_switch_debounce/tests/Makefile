# Makefile

# defaults
SIM ?= ghdl
TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES += $(PWD)/../hdl/*

TOPLEVEL = switch_debounce_top
MODULE = test_top,test_led_toggle,test_debounce_filter

# SIM_ARGS ?= --vcd=waveform.vcd
SIM_ARGS += -gDEBOUNCE_LIMIT=30

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
