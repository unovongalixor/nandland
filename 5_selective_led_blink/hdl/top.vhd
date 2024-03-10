library ieee;
use ieee.std_logic_1164.all;

entity Selective_Led_Blink_Top is 
    generic (DEBOUNCE_LIMIT : integer := 250000);
    port (
        i_Clk       : in std_logic;
        i_Switch_1  : in std_logic;
        i_Switch_2  : in std_logic;
        o_LED_1     : out std_logic;
        o_LED_2     : out std_logic;
        o_LED_3     : out std_logic;
        o_LED_4     : out std_logic);
end entity Selective_Led_Blink_Top;

architecture RTL of Selective_Led_Blink_Top is
    signal r_LFSR_Toggle : std_logic := '0';
    signal w_LFSR_Done   : std_logic;
    signal w_Debounced_Switch_1 : std_logic;
    signal w_Debounced_Switch_2 : std_logic;
begin

    LFSR_22_Inst : entity work.LFSR_22
    port map (
        i_Clk       => i_Clk,
        o_LFSR_Data => open, -- unconnected
        o_LFSR_Done => w_LFSR_Done);

    process (i_Clk) is 
    begin
        if rising_edge(i_Clk) then
            if w_LFSR_Done = '1' then
                r_LFSR_Toggle <= not r_LFSR_Toggle;
            end if;
        end if;
    end process;


    Debounce_Filter_Inst_1 : entity work.Debounce_Filter
    generic map (DEBOUNCE_LIMIT => DEBOUNCE_LIMIT)
    port map (
                 i_Clk => i_Clk,
                 i_Bouncy => i_Switch_1,
                 o_Debounced => w_Debounced_Switch_1);


    Debounce_Filter_Inst_2 : entity work.Debounce_Filter
    generic map (DEBOUNCE_LIMIT => DEBOUNCE_LIMIT)
    port map (
                 i_Clk => i_Clk,
                 i_Bouncy => i_Switch_2,
                 o_Debounced => w_Debounced_Switch_2);

    
    Demux_1_To_4_Inst : entity work.Demux_1_To_4
    port map (
        i_Data  => r_LFSR_Toggle,
        i_Sel0  => w_Debounced_Switch_1,
        i_Sel1  => w_Debounced_Switch_2,
        o_Data0 => o_LED_1,
        o_Data1 => o_LED_2,
        o_Data2 => o_LED_3,
        o_Data3 => o_LED_4);

end architecture RTL;
