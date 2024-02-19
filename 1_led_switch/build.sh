mkdir -p build

# analyze
yosys -m ghdl -p 'ghdl led.vhd -e Switches_To_LEDs; synth_ice40 -json build/led.json'

# place
nextpnr-ice40 --hx1k --package vq100 --pcf led.pcf --asc build/led.asc --json build/led.json

# build
icepack build/led.asc build/led.bin

# flash
iceprog build/led.bin
