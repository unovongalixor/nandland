all: analyze place pack program

analyze: hdl/debounce_filter.vhd hdl/led_toggle.vhd hdl/top.vhd
	yosys -m ghdl -p 'ghdl hdl/debounce_filter.vhd -e Debounce_Filter; ghdl hdl/led_toggle.vhd -e LED_Toggle; ghdl hdl/top.vhd -e Switch_Debounce_Top; synth_ice40 -json build/top.json'

place: constraints/go_board.pcf constraints/pre.py build/top.json
	nextpnr-ice40 --hx1k --package vq100 --pcf constraints/go_board.pcf --pre-pack constraints/pre.py --asc build/top.asc --json build/top.json

pack: build/top.asc
	icepack build/top.asc build/top.bin

program: build/top.bin
	iceprog build/top.bin


