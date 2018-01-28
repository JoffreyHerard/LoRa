package lora.simulations;

import lora.*;
network Net
{

    submodules:
        LWGW[1]: LWGW;
        LGW[1]: LGW;
        IN[1]: IsoN;
    connections:
        IN[0].channelsO++ --> LGW[0].channelsI++;
        LGW[0].channelsO++ --> IN[0].channelsI++;

        LGW[0].channelsO++ --> LWGW[0].channelsI++;
        LWGW[0].channelsO++ --> LGW[0].channelsI++;
}
