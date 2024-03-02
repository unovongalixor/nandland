library ieee;
use ieee.std_logic_1164.all;

entity Switch_Debounce_Top is
    generic (DEBOUNCE_LIMIT : integer := 250000);
    port (
    i_Clk       : in  std_logic;
    i_Switch_1  : in  std_logic;
    o_LED_1     : out std_logic);
end entity Switch_Debounce_Top;

architecture RTL of Switch_Debounce_Top is
    signal w_Debounced_Switch : std_logic;
begin
    Debounce_Filter_Inst : entity work.Debounce_Filter
    generic map (DEBOUNCE_LIMIT => DEBOUNCE_LIMIT)
    port map (
                 i_Clk => i_Clk,
                 i_Bouncy => i_Switch_1,
                 o_Debounced => w_Debounced_Switch);

    LED_Toggle_Inst : entity work.LED_Toggle
    port map (
                 i_Clk => i_Clk,
                 i_Switch_1 => w_Debounced_Switch,
                 o_LED_1 => o_LED_1);
end architecture RTL;
