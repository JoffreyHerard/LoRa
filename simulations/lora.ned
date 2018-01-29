package lora.simulations;

import lora.*;
network Net
{

	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[1]: LGW; 
		 IN[2]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- LGW[0].channelsO++;
			LGW[0].channelsO++ --> IN[0].channelsI++;
			LGW[0].channelsI++ <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- IN[1].channelsO++;
			IN[0].channelsO++ --> IN[1].channelsI++;
			IN[0].channelsI++ <-- IN[1].channelsO++;
}