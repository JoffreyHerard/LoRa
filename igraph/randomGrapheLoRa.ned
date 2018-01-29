	 submodules:
		 LWGW[1]: LWGW; 
		 LGW[4]: LGW; 
		 IN[4]: IsoN; 
	 connections:
			LWGW[0].channelsO++ --> {delay=779ms;} --> LGW[0].channelsI++;
			LWGW[0].channelsI++ <-- {delay=404ms;} <-- LGW[0].channelsO++;
			LWGW[0].channelsO++ --> {delay=1109ms;} --> LGW[1].channelsI++;
			LWGW[0].channelsI++ <-- {delay=883ms;} <-- LGW[1].channelsO++;
			LGW[0].channelsO++ --> {delay=584ms;} --> LGW[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=761ms;} <-- LGW[1].channelsO++;
			LWGW[0].channelsO++ --> {delay=983ms;} --> LGW[2].channelsI++;
			LWGW[0].channelsI++ <-- {delay=609ms;} <-- LGW[2].channelsO++;
			LGW[0].channelsO++ --> {delay=5ms;} --> LGW[2].channelsI++;
			LGW[0].channelsI++ <-- {delay=423ms;} <-- LGW[2].channelsO++;
			LGW[1].channelsO++ --> {delay=1001ms;} --> LGW[2].channelsI++;
			LGW[1].channelsI++ <-- {delay=277ms;} <-- LGW[2].channelsO++;
			LWGW[0].channelsO++ --> {delay=239ms;} --> LGW[3].channelsI++;
			LWGW[0].channelsI++ <-- {delay=394ms;} <-- LGW[3].channelsO++;
			LGW[0].channelsO++ --> {delay=453ms;} --> LGW[3].channelsI++;
			LGW[0].channelsI++ <-- {delay=1047ms;} <-- LGW[3].channelsO++;
			LGW[1].channelsO++ --> {delay=481ms;} --> LGW[3].channelsI++;
			LGW[1].channelsI++ <-- {delay=784ms;} <-- LGW[3].channelsO++;
			LGW[2].channelsO++ --> {delay=1114ms;} --> LGW[3].channelsI++;
			LGW[2].channelsI++ <-- {delay=614ms;} <-- LGW[3].channelsO++;
			LGW[1].channelsO++ --> {delay=998ms;} --> IN[0].channelsI++;
			LGW[1].channelsI++ <-- {delay=412ms;} <-- IN[0].channelsO++;
			LGW[0].channelsO++ --> {delay=1085ms;} --> IN[1].channelsI++;
			LGW[0].channelsI++ <-- {delay=1042ms;} <-- IN[1].channelsO++;
			LGW[3].channelsO++ --> {delay=255ms;} --> IN[2].channelsI++;
			LGW[3].channelsI++ <-- {delay=682ms;} <-- IN[2].channelsO++;
			LGW[2].channelsO++ --> {delay=901ms;} --> IN[3].channelsI++;
			LGW[2].channelsI++ <-- {delay=616ms;} <-- IN[3].channelsO++;
			LGW[2].channelsO++ --> {delay=1017ms;} --> IN[1].channelsI++;
			LGW[2].channelsI++ <-- {delay=3ms;} <-- IN[1].channelsO++;
			LGW[3].channelsO++ --> {delay=551ms;} --> IN[1].channelsI++;
			LGW[3].channelsI++ <-- {delay=404ms;} <-- IN[1].channelsO++;
}