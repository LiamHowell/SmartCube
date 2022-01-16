# Command parser
# Liam Howell - 18/09

import hdmi_funcs


def main_input():
    hdmi_cmd_txt = "Change the HDMI input   : hdmi,{1,2,3} \n"
    relay_cmd_txt= "Turn lights on and off  :light,{1,2,3,4} \n"
    
    print(hdmi_cmd_txt+ relay_cmd_txt)
    
    inp = input (" Please input a command: ")

    print(inp)
