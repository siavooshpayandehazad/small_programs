library IEEE;
use IEEE.std_logic_1164.all;


entity game_of_life_tb is
end game_of_life_tb;

architecture Bench of game_of_life_tb is

  --Component declaration for ALU


 signal clk: std_logic:= '0';
 signal rst: std_logic:= '0';
 constant clock_period : time := 1ns;
   component game_of_life is
     port (  rst, clk: in std_logic);
   end component;

begin



gof: game_of_life port map(rst, clk);

CLOCK_GEN:process
begin
  clk <= '0';
  wait for clock_period/2;
  clk <= '1';
  wait for clock_period/2;
end process;

RST_GEN:process
begin
  rst <= '1';
  wait for 0.5*clock_period;
  rst <=  '0';
  wait;
end process;

 
end Bench;
