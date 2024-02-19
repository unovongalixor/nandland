mkdir -p build

# analyze
yosys -m ghdl -p 'ghdl led.vhd -e LED_Toggle; synth_ice40 -json build/led.json'

# place
nextpnr-ice40 --hx1k --package vq100 --pcf led.pcf --pre-pack pre.py --asc build/led.asc --json build/led.json

# build
icepack build/led.asc build/led.bin

# flash
iceprog build/led.bin
