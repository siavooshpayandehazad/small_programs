
library IEEE;
use IEEE.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use std.textio.all;

entity game_of_life is
  port (  rst, clk: in std_logic
  );
end game_of_life;



architecture behavioral of game_of_life is
  signal current_state, current_state_in: std_logic_vector(599 downto 0);

  begin

  process(clk, rst)

    begin
    if rst = '1' then
        current_state <= (others => '0');
        -- EXPLODER
        current_state(309) <= '1';
        current_state(311) <= '1';
        current_state(313) <= '1';
        current_state(289) <= '1';
        current_state(293) <= '1';
        current_state(269) <= '1';
        current_state(273) <= '1';
        current_state(249) <= '1';
        current_state(253) <= '1';
        current_state(229) <= '1';
        current_state(231) <= '1';
        current_state(233) <= '1';
        -- SMALL EXPLODER
        --current_state(290) <= '1';
        --current_state(291) <= '1';
        --current_state(292) <= '1';
        --current_state(311) <= '1';
        --current_state(270) <= '1';
        --current_state(272) <= '1';
        --current_state(251) <= '1';

    elsif clk'event and clk = '1' then
        current_state <= current_state_in;
    end if;
  end process;

  process(current_state)
    variable alive_around : integer := 0;
    begin

      for Y in 0 to 29 loop
          for X in 0 to 19 loop
              alive_around := 0;
              if X /= 0 then
                  if current_state(X-1+20*Y) = '1' then
                      alive_around := alive_around + 1;
                  end if;

                  if Y /= 0 and current_state(X-1+20*(Y-1)) = '1'then
			                 alive_around := alive_around + 1;
                  end if;

                  if Y /= 29 and current_state(X-1+20*(Y+1)) = '1' then
                    alive_around := alive_around + 1;
                  end if;

              end if;

              if X /= 19 then
                  if current_state(X+1+20*Y) = '1' then
                      alive_around := alive_around + 1;
                  end if;
                  if Y /= 0 and current_state(X+1+20*(Y-1)) = '1' then
                        alive_around := alive_around + 1;
                  end if;

                  if Y /= 29 and current_state(X+1+20*(Y+1)) = '1'then
                        alive_around := alive_around + 1;
                  end if;
              end if;


              if Y /= 0 and current_state(X+20*(Y-1)) = '1'then
                   alive_around := alive_around + 1;
              end if;

              if Y /= 29 and current_state(X+20*(Y+1)) = '1' then
                alive_around := alive_around + 1;
              end if;


              if current_state(X+20*Y) = '1' then  --cell is alive
                  if alive_around = 2 or alive_around = 3 then
                      current_state_in(X+20*Y) <= '1';
                  else
                      current_state_in(X+20*Y) <= '0';
                  end if;
              else --cell is dead
                  if  alive_around = 3 then
                      current_state_in(X+20*Y) <= '1';
                  else
                      current_state_in(X+20*Y) <= '0';
                  end if;
              end if;

          end loop;
      end loop;
  end process;

end behavioral;
