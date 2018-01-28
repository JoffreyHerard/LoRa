package lora.simulations;

import lora.*;
network Net
{

	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[3]: LGW; 
		 IN[6]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- LGW[0].channelsO++;
			LWGW[0].channelsO++ --> LGW[1].channelsI++;
			LWGW[0].channelsI++ <-- LGW[1].channelsO++;
			LGW[0].channelsO++ --> LGW[1].channelsI++;
			LGW[0].channelsI++ <-- LGW[1].channelsO++;
			LWGW[0].channelsO++ --> LGW[2].channelsI++;
			LWGW[0].channelsI++ <-- LGW[2].channelsO++;
			LGW[0].channelsO++ --> LGW[2].channelsI++;
			LGW[0].channelsI++ <-- LGW[2].channelsO++;
			LGW[1].channelsO++ --> LGW[2].channelsI++;
			LGW[1].channelsI++ <-- LGW[2].channelsO++;
			LGW[1].channelsO++ --> IN[0].channelsI++;
			LGW[1].channelsI++ <-- IN[0].channelsO++;
			LGW[1].channelsO++ --> IN[1].channelsI++;
			LGW[1].channelsI++ <-- IN[1].channelsO++;
			LGW[1].channelsO++ --> IN[2].channelsI++;
			LGW[1].channelsI++ <-- IN[2].channelsO++;
			LGW[2].channelsO++ --> IN[3].channelsI++;
			LGW[2].channelsI++ <-- IN[3].channelsO++;
			LGW[0].channelsO++ --> IN[4].channelsI++;
			LGW[0].channelsI++ <-- IN[4].channelsO++;
			LGW[0].channelsO++ --> IN[5].channelsI++;
			LGW[0].channelsI++ <-- IN[5].channelsO++;
			LGW[2].channelsO++ --> IN[0].channelsI++;
			LGW[2].channelsI++ <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> IN[2].channelsI++;
			LGW[0].channelsI++ <-- IN[2].channelsO++;
			LGW[2].channelsO++ --> IN[4].channelsI++;
			LGW[2].channelsI++ <-- IN[4].channelsO++;
}
