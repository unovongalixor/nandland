all: build_dir analyze place pack program

test:
	$(MAKE) -C tests

build_dir:
	@mkdir -p build

analyze: hdl/demux_1_4.vhd hdl/lfsr_22.vhd hdl/top.vhd
	yosys -m ghdl -p 'ghdl hdl/debounce_filter.vhd -e Debounce_Filter; ghdl hdl/demux_1_4.vhd -e Demux_1_To_4; ghdl hdl/lfsr_22.vhd -e LFSR_22; ghdl hdl/top.vhd -e Selective_Led_Blink_Top; synth_ice40 -json build/top.json'

place: constraints/go_board.pcf constraints/pre.py build/top.json
	nextpnr-ice40 --hx1k --package vq100 --pcf constraints/go_board.pcf --pre-pack constraints/pre.py --asc build/top.asc --json build/top.json

pack: build/top.asc
	icepack build/top.asc build/top.bin

program: build/top.bin
	iceprog build/top.bin
