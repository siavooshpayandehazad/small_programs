################################################
# Copyright (C) 2016 siavoosh Payandeh Azad    #
################################################

vlib work

# Include files and compile them
vcom "game_of_life.vhd"

vcom "tb.vhd"


# Start the simulation
vsim work.game_of_life_tb


# Run the simulation
do wave.do
run 1000 ns
