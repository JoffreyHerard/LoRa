package lora.simulations;

import lora.*;
network Net
{
    @display("bgb=849,509");
	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[1]: LGW; 
		 IN[3]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> {delay=137ms;@display("ls=pink");} --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- {delay=175ms;} <-- LGW[0].channelsO++;
			LGW[0].channelsO++ --> {delay=178ms;} --> IN[0].channelsI++;
			LGW[0].channelsI++ <-- {delay=160ms;} <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> {delay=158ms;} --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=106ms;} <-- IN[1].channelsO++;
			LGW[0].channelsO++ --> {delay=132ms;} --> IN[2].channelsI++;
			LGW[0].channelsI++ <-- {delay=138ms;} <-- IN[2].channelsO++;
}	