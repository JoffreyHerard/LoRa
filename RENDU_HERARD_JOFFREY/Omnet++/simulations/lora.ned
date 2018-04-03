package lora.simulations;

import lora.*;
network Net
{
   
	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[1]: LGW; 
		 IN[3]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> {delay=10ms;} --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- {delay=10ms;} <-- LGW[0].channelsO++;
			LGW[0].channelsO++ --> {delay=10ms;} --> IN[0].channelsI++;
			LGW[0].channelsI++ <-- {delay=10ms;} <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> {delay=10ms;} --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=10ms;} <-- IN[1].channelsO++;
			LGW[0].channelsO++ --> {delay=10ms;} --> IN[2].channelsI++;
			LGW[0].channelsI++ <-- {delay=10ms;} <-- IN[2].channelsO++;
			IN[0].channelsO++ --> {delay=10ms;} --> IN[1].channelsI++;
			IN[0].channelsI++ <-- {delay=10ms;} <-- IN[1].channelsO++;
			IN[0].channelsO++ --> {delay=10ms;} --> IN[2].channelsI++;
			IN[0].channelsI++ <-- {delay=10ms;} <-- IN[2].channelsO++;
			IN[1].channelsO++ --> {delay=10ms;} --> IN[2].channelsI++;
			IN[1].channelsI++ <-- {delay=10ms;} <-- IN[2].channelsO++;
}