package lora.simulations;

import lora.*;
network Net
{
    @display("bgb=699,632");
    submodules:
        well: LWGW {
            @display("is=l;p=37,314");
        }
        LGW: LGW {
            @display("p=39,181");
        }
        IN: IsoN {
            @display("p=40,61");
        }
        IN4: IsoN {
            @display("p=40,582");
        }
        LGW4: LGW {
            @display("p=37,450");
        }
        IN1: IsoN {
            @display("p=133,61");
        }
        IN2: IsoN {
            @display("p=133,582");
        }
        LGW1: LGW {
            @display("p=132,181");
        }
        LGW2: LGW {
            @display("p=130,450");
        }
        well1: LWGW {
            @display("is=l;p=130,314");
        }
        IN3: IsoN {
            @display("p=212,62");
        }
        IN5: IsoN {
            @display("p=305,62");
        }
        IN6: IsoN {
            @display("p=305,583");
        }
        IN7: IsoN {
            @display("p=212,583");
        }
        LGW3: LGW {
            @display("p=211,182");
        }
        LGW5: LGW {
            @display("p=304,182");
        }
        LGW6: LGW {
            @display("p=302,451");
        }
        LGW7: LGW {
            @display("p=209,451");
        }
        well2: LWGW {
            @display("is=l;p=209,315");
        }
        well3: LWGW {
            @display("is=l;p=302,315");
        }
        IN8: IsoN {
            @display("p=387,62");
        }
        IN9: IsoN {
            @display("p=480,62");
        }
        IN10: IsoN {
            @display("p=480,583");
        }
        IN11: IsoN {
            @display("p=559,63");
        }
        IN12: IsoN {
            @display("p=387,583");
        }
        IN13: IsoN {
            @display("p=652,63");
        }
        IN14: IsoN {
            @display("p=652,584");
        }
        IN15: IsoN {
            @display("p=559,584");
        }
        LGW8: LGW {
            @display("p=386,182");
        }
        LGW9: LGW {
            @display("p=479,182");
        }
        LGW10: LGW {
            @display("p=477,451");
        }
        LGW11: LGW {
            @display("p=558,183");
        }
        LGW12: LGW {
            @display("p=384,451");
        }
        LGW13: LGW {
            @display("p=651,183");
        }
        LGW14: LGW {
            @display("p=649,452");
        }
        LGW15: LGW {
            @display("p=556,452");
        }
        well4: LWGW {
            @display("is=l;p=384,315");
        }
        well5: LWGW {
            @display("is=l;p=477,315");
        }
        well6: LWGW {
            @display("is=l;p=556,316");
        }
        well7: LWGW {
            @display("is=l;p=649,316");
        }
    connections:
        well.channelsO++ --> {  delay = 120ms; } --> LGW.channelsI++;
        well.channelsI++ <-- {  delay = 260ms; } <-- LGW.channelsO++;
        LGW.channelsO++ --> {  delay = 260ms; } --> IN.channelsI++;
        LGW.channelsI++ <-- {  delay = 10ms; } <-- IN.channelsO++;
        well.channelsI++ <-- {  delay = 120ms; } <-- LGW4.channelsO++;
        LGW4.channelsI++ <-- {  delay = 10ms; } <-- IN4.channelsO++;
        LGW4.channelsO++ --> {  delay = 10ms; } --> IN4.channelsI++;
        LGW4.channelsI++ <-- {  delay = 10ms; } <-- IN4.channelsO++;
        well1.channelsI++ <-- {  delay = 120ms; } <-- LGW1.channelsO++;
        LGW1.channelsO++ --> {  delay = 10ms; } --> IN1.channelsI++;
        LGW1.channelsI++ <-- {  delay = 120ms; } <-- IN1.channelsO++;
        LGW2.channelsI++ <-- {  delay = 260ms; } <-- IN2.channelsO++;
        LGW2.channelsI++ <-- {  delay = 10ms; } <-- IN2.channelsO++;
        well1.channelsO++ --> {  delay = 120ms; } --> LGW1.channelsI++;
        well1.channelsI++ <-- {  delay = 10ms; } <-- LGW2.channelsO++;
        LGW2.channelsO++ --> {  delay = 120ms; } --> IN2.channelsI++;
        well2.channelsI++ <-- {  delay = 120ms; } <-- LGW3.channelsO++;
        LGW3.channelsO++ --> {  delay = 10ms; } --> IN3.channelsI++;
        well3.channelsI++ <-- {  delay = 10ms; } <-- LGW5.channelsO++;
        LGW5.channelsO++ --> {  delay = 260ms; } --> IN5.channelsI++;
        LGW3.channelsI++ <-- {  delay = 260ms; } <-- IN3.channelsO++;
        LGW5.channelsI++ <-- {  delay = 120ms; } <-- IN5.channelsO++;
        LGW7.channelsI++ <-- {  delay = 10ms; } <-- IN7.channelsO++;
        LGW7.channelsI++ <-- {  delay = 10ms; } <-- IN7.channelsO++;
        well3.channelsO++ --> {  delay = 10ms; } --> LGW5.channelsI++;
        well3.channelsI++ <-- {  delay = 120ms; } <-- LGW6.channelsO++;
        LGW6.channelsO++ --> {  delay = 10ms; } --> IN6.channelsI++;
        well2.channelsO++ --> {  delay = 10ms; } --> LGW3.channelsI++;
        LGW6.channelsI++ <-- {  delay = 120ms; } <-- IN6.channelsO++;
        LGW6.channelsI++ <-- {  delay = 10ms; } <-- IN6.channelsO++;
        well2.channelsI++ <-- {  delay = 10ms; } <-- LGW7.channelsO++;
        LGW7.channelsO++ --> {  delay = 10ms; } --> IN7.channelsI++;
        well7.channelsO++ --> {  delay = 260ms; } --> LGW13.channelsI++;
        LGW8.channelsI++ <-- {  delay = 10ms; } <-- IN8.channelsO++;
        LGW9.channelsI++ <-- {  delay = 10ms; } <-- IN9.channelsO++;
        LGW11.channelsI++ <-- {  delay = 120ms; } <-- IN11.channelsO++;
        LGW12.channelsI++ <-- {  delay = 10ms; } <-- IN12.channelsO++;
        LGW12.channelsI++ <-- {  delay = 10ms; } <-- IN12.channelsO++;
        well7.channelsI++ <-- {  delay = 120ms; } <-- LGW13.channelsO++;
        LGW13.channelsO++ --> {  delay = 10ms; } --> IN13.channelsI++;
        well4.channelsO++ --> {  delay = 120ms; } --> LGW8.channelsI++;
        LGW10.channelsI++ <-- {  delay = 10ms; } <-- IN10.channelsO++;
        LGW10.channelsI++ <-- {  delay = 10ms; } <-- IN10.channelsO++;
        well6.channelsI++ <-- {  delay = 120ms; } <-- LGW11.channelsO++;
        LGW11.channelsO++ --> {  delay = 10ms; } --> IN11.channelsI++;
        well4.channelsI++ <-- {  delay = 260ms; } <-- LGW8.channelsO++;
        LGW8.channelsO++  --> {  delay = 260ms; } --> IN8.channelsI++;
        well5.channelsI++ <-- {  delay = 260ms; } <-- LGW9.channelsO++;
        LGW9.channelsO++  --> {  delay = 10ms; } --> IN9.channelsI++;
        LGW15.channelsI++ <-- {  delay = 10ms; } <-- IN15.channelsO++;
        LGW15.channelsI++ <-- {  delay = 120ms; } <-- IN15.channelsO++;
        LGW13.channelsI++ <-- {  delay = 10ms; } <-- IN13.channelsO++;
        LGW14.channelsI++ <-- {  delay = 10ms; } <-- IN14.channelsO++;
        LGW14.channelsI++ <-- {  delay = 120ms; } <-- IN14.channelsO++;
        well5.channelsO++ --> {  delay = 10ms; } --> LGW9.channelsI++;
        well7.channelsI++ <-- {  delay = 10ms; } <-- LGW14.channelsO++;
        LGW14.channelsO++ --> {  delay = 120ms; } --> IN14.channelsI++;
        well5.channelsI++ <-- {  delay = 10ms; } <-- LGW10.channelsO++;
        LGW10.channelsO++ --> {  delay = 260ms; } --> IN10.channelsI++;
        well6.channelsI++ <-- {  delay = 10ms; } <-- LGW15.channelsO++;
        LGW15.channelsO++ --> {  delay = 260ms; } --> IN15.channelsI++;
        well6.channelsO++ --> {  delay = 260ms; } --> LGW11.channelsI++;
        well4.channelsI++ <-- {  delay = 10ms; } <-- LGW12.channelsO++;
        LGW12.channelsO++ --> {  delay = 120ms; } --> IN12.channelsI++;
        well.channelsO++  --> {  delay = 10ms; } --> well1.channelsI++;
        well1.channelsO++ --> {  delay = 10ms; } --> well.channelsI++;
        well1.channelsO++ --> {  delay = 120ms; } --> well2.channelsI++;
        well2.channelsO++ --> {  delay = 260ms; } --> well1.channelsI++;
        well3.channelsO++ --> {  delay = 10ms; } --> well2.channelsI++;
        well2.channelsO++ --> {  delay = 120ms; } --> well3.channelsI++;
        well4.channelsO++ --> {  delay = 10ms; } --> well3.channelsI++;
        well3.channelsO++ --> {  delay = 120ms; } --> well4.channelsI++;
        well4.channelsO++ --> {  delay = 10ms; } --> well5.channelsI++;
        well5.channelsO++ --> {  delay = 260ms; } --> well4.channelsI++;
        well5.channelsO++ --> {  delay = 120ms; } --> well6.channelsI++;
        well6.channelsO++ --> {  delay = 10ms; } --> well5.channelsI++;
        well6.channelsO++ --> {  delay = 260ms; } --> well7.channelsI++;
        well7.channelsO++ --> {  delay = 120ms; } --> well6.channelsI++;
        well.channelsO++  --> {  delay = 120ms; } --> LGW4.channelsI++;
        well1.channelsO++ --> {  delay = 10ms; } --> LGW2.channelsI++;
        well2.channelsO++ --> {  delay = 10ms; } --> LGW7.channelsI++;
        well3.channelsO++ --> {  delay = 260ms; } --> LGW6.channelsI++;
        well4.channelsO++ --> {  delay = 120ms; } --> LGW12.channelsI++;
        well5.channelsO++ --> {  delay = 10ms; } --> LGW10.channelsI++;
        well6.channelsO++ --> {  delay = 10ms; } --> LGW15.channelsI++;
        well7.channelsO++ --> {  delay = 260ms; } --> LGW14.channelsI++;
}
