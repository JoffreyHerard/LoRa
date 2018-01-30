package lora.simulations;

import lora.*;
network Net
{
    @display("bgb=849,509");
	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[4]: LGW; 
		 IN[6]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> {delay=910ms;} --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- {delay=310ms;} <-- LGW[0].channelsO++;
			LWGW[0].channelsO++ --> {delay=1164ms;} --> LGW[1].channelsI++;
			LWGW[0].channelsI++ <-- {delay=1084ms;} <-- LGW[1].channelsO++;
			LGW[0].channelsO++ --> {delay=960ms;} --> LGW[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=577ms;} <-- LGW[1].channelsO++;
			LWGW[0].channelsO++ --> {delay=535ms;} --> LGW[2].channelsI++;
			LWGW[0].channelsI++ <-- {delay=879ms;} <-- LGW[2].channelsO++;
			LGW[0].channelsO++ --> {delay=621ms;} --> LGW[2].channelsI++;
			LGW[0].channelsI++ <-- {delay=177ms;} <-- LGW[2].channelsO++;
			LGW[1].channelsO++ --> {delay=654ms;} --> LGW[2].channelsI++;
			LGW[1].channelsI++ <-- {delay=82ms;} <-- LGW[2].channelsO++;
			LWGW[0].channelsO++ --> {delay=323ms;} --> LGW[3].channelsI++;
			LWGW[0].channelsI++ <-- {delay=37ms;} <-- LGW[3].channelsO++;
			LGW[0].channelsO++ --> {delay=1021ms;} --> LGW[3].channelsI++;
			LGW[0].channelsI++ <-- {delay=464ms;} <-- LGW[3].channelsO++;
			LGW[1].channelsO++ --> {delay=225ms;} --> LGW[3].channelsI++;
			LGW[1].channelsI++ <-- {delay=110ms;} <-- LGW[3].channelsO++;
			LGW[2].channelsO++ --> {delay=229ms;} --> LGW[3].channelsI++;
			LGW[2].channelsI++ <-- {delay=237ms;} <-- LGW[3].channelsO++;
			LGW[0].channelsO++ --> {delay=825ms;} --> IN[0].channelsI++;
			LGW[0].channelsI++ <-- {delay=573ms;} <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> {delay=706ms;} --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=591ms;} <-- IN[1].channelsO++;
			LGW[2].channelsO++ --> {delay=446ms;} --> IN[2].channelsI++;
			LGW[2].channelsI++ <-- {delay=921ms;} <-- IN[2].channelsO++;
			LGW[2].channelsO++ --> {delay=532ms;} --> IN[3].channelsI++;
			LGW[2].channelsI++ <-- {delay=1110ms;} <-- IN[3].channelsO++;
			LGW[3].channelsO++ --> {delay=899ms;} --> IN[4].channelsI++;
			LGW[3].channelsI++ <-- {delay=1147ms;} <-- IN[4].channelsO++;
			LGW[0].channelsO++ --> {delay=424ms;} --> IN[5].channelsI++;
			LGW[0].channelsI++ <-- {delay=978ms;} <-- IN[5].channelsO++;
			LGW[0].channelsO++ --> {delay=814ms;} --> IN[4].channelsI++;
			LGW[0].channelsI++ <-- {delay=30ms;} <-- IN[4].channelsO++;
			LGW[3].channelsO++ --> {delay=122ms;} --> IN[5].channelsI++;
			LGW[3].channelsI++ <-- {delay=682ms;} <-- IN[5].channelsO++;
			IN[1].channelsO++ --> {delay=326ms;} --> IN[3].channelsI++;
			IN[1].channelsI++ <-- {delay=82ms;} <-- IN[3].channelsO++;
			IN[2].channelsO++ --> {delay=628ms;} --> IN[4].channelsI++;
			IN[2].channelsI++ <-- {delay=902ms;} <-- IN[4].channelsO++;
}	
