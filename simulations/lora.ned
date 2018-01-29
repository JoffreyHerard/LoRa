package lora.simulations;

import lora.*;
network Net
{
	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[4]: LGW; 
		 IN[9]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> {delay=304ms;} --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- {delay=1192ms;} <-- LGW[0].channelsO++;
			LWGW[0].channelsO++ --> {delay=809ms;} --> LGW[1].channelsI++;
			LWGW[0].channelsI++ <-- {delay=165ms;} <-- LGW[1].channelsO++;
			LGW[0].channelsO++ --> {delay=443ms;} --> LGW[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=216ms;} <-- LGW[1].channelsO++;
			LWGW[0].channelsO++ --> {delay=297ms;} --> LGW[2].channelsI++;
			LWGW[0].channelsI++ <-- {delay=1124ms;} <-- LGW[2].channelsO++;
			LGW[0].channelsO++ --> {delay=1070ms;} --> LGW[2].channelsI++;
			LGW[0].channelsI++ <-- {delay=929ms;} <-- LGW[2].channelsO++;
			LGW[1].channelsO++ --> {delay=1123ms;} --> LGW[2].channelsI++;
			LGW[1].channelsI++ <-- {delay=880ms;} <-- LGW[2].channelsO++;
			LWGW[0].channelsO++ --> {delay=798ms;} --> LGW[3].channelsI++;
			LWGW[0].channelsI++ <-- {delay=1008ms;} <-- LGW[3].channelsO++;
			LGW[0].channelsO++ --> {delay=449ms;} --> LGW[3].channelsI++;
			LGW[0].channelsI++ <-- {delay=670ms;} <-- LGW[3].channelsO++;
			LGW[1].channelsO++ --> {delay=977ms;} --> LGW[3].channelsI++;
			LGW[1].channelsI++ <-- {delay=1076ms;} <-- LGW[3].channelsO++;
			LGW[2].channelsO++ --> {delay=1119ms;} --> LGW[3].channelsI++;
			LGW[2].channelsI++ <-- {delay=296ms;} <-- LGW[3].channelsO++;
			LGW[0].channelsO++ --> {delay=480ms;} --> IN[0].channelsI++;
			LGW[0].channelsI++ <-- {delay=115ms;} <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> {delay=450ms;} --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=372ms;} <-- IN[1].channelsO++;
			LGW[3].channelsO++ --> {delay=861ms;} --> IN[2].channelsI++;
			LGW[3].channelsI++ <-- {delay=117ms;} <-- IN[2].channelsO++;
			LGW[1].channelsO++ --> {delay=983ms;} --> IN[3].channelsI++;
			LGW[1].channelsI++ <-- {delay=126ms;} <-- IN[3].channelsO++;
			LGW[3].channelsO++ --> {delay=44ms;} --> IN[4].channelsI++;
			LGW[3].channelsI++ <-- {delay=563ms;} <-- IN[4].channelsO++;
			LGW[3].channelsO++ --> {delay=685ms;} --> IN[5].channelsI++;
			LGW[3].channelsI++ <-- {delay=202ms;} <-- IN[5].channelsO++;
			LGW[3].channelsO++ --> {delay=663ms;} --> IN[6].channelsI++;
			LGW[3].channelsI++ <-- {delay=180ms;} <-- IN[6].channelsO++;
			LGW[3].channelsO++ --> {delay=232ms;} --> IN[7].channelsI++;
			LGW[3].channelsI++ <-- {delay=748ms;} <-- IN[7].channelsO++;
			LGW[0].channelsO++ --> {delay=115ms;} --> IN[8].channelsI++;
			LGW[0].channelsI++ <-- {delay=973ms;} <-- IN[8].channelsO++;
			LGW[1].channelsO++ --> {delay=969ms;} --> IN[2].channelsI++;
			LGW[1].channelsI++ <-- {delay=101ms;} <-- IN[2].channelsO++;
			LGW[2].channelsO++ --> {delay=176ms;} --> IN[4].channelsI++;
			LGW[2].channelsI++ <-- {delay=635ms;} <-- IN[4].channelsO++;
			LGW[2].channelsO++ --> {delay=221ms;} --> IN[6].channelsI++;
			LGW[2].channelsI++ <-- {delay=1007ms;} <-- IN[6].channelsO++;
			LGW[2].channelsO++ --> {delay=930ms;} --> IN[8].channelsI++;
			LGW[2].channelsI++ <-- {delay=404ms;} <-- IN[8].channelsO++;
			IN[4].channelsO++ --> {delay=121ms;} --> IN[5].channelsI++;
			IN[4].channelsI++ <-- {delay=581ms;} <-- IN[5].channelsO++;
}