#include "LGW.h"

Define_Module(LGW);

void LGW::initialize()
{
   LOG  EV << "LoRA Gateway started"<< endl;
   this->slot=5;
   this->discovered=false;
   this->frequency=0;
   this->id = par("id").longValue();
   this->idRegistered =  vector<int>();
   this->isRegistered =  vector<bool>();
   this->MyLW=-1;
   this->nb_harvest=0;
   /* generate number between 1 and 100: */
   this->time = this->slot +1;


   cDisplayString& dispStr = getDisplayString();
   //dispStr.parse("p=200,100,r,100");
   const char* tmpColor= this->mycolor.c_str();
   dispStr.setTagArg("i", 0, tmpColor);

   messageLoRA *m = new messageLoRA();
   char numstr[21];
   sprintf(numstr, "%d", this->id);
   string tmp = "Join request";
   const char * c = tmp.c_str();


   switch(this->id){
       case 9:{
           this->mycolor="device/device_cyan";
           break;
       }
       case 10:{
           this->mycolor="device/device_pink";
           break;
       }
       case 11:{
           this->mycolor="device/device_purple";
           break;
       }
       case 12:{
           this->mycolor="device/device_yellow";
           break;
       }
       case 13:{
           this->mycolor="device/device_cyan";
           break;
       }
       case 14:{
           this->mycolor="device/device_pink";
           break;
       }
       case 15:{
           this->mycolor="device/device_purple";
           break;
       }
       case 16:{
           this->mycolor="device/device_yellow";
           break;
       }
       case 17:{
           this->mycolor="device/device_cyan";
           break;
       }
       case 18:{
           this->mycolor="device/device_pink";
           break;
       }
       case 19:{
           this->mycolor="device/device_purple";
           break;
       }
       case 20:{
           this->mycolor="device/device_yellow";
           break;
       }
       case 21:{
           this->mycolor="device/device_cyan";
           break;
       }
       case 22:{
           this->mycolor="device/device_pink";
           break;
       }
       case 23:{
           this->mycolor="device/device_purple";
           break;
       }
       case 24:{
           this->mycolor="device/device_yellow";
           break;
       }
   }


   m->setName(c);
   m->setKind(0);
   m->setIdSrc(this->id);
   m->setIdDest(-1);
   int i;
   for (i = 0; i < this->gateSize("channelsO"); i++)
   {
       messageLoRA *copy = m->dup();
       send(copy, "channelsO", i);
   }
   delete m;
   LOG EV << "Join Request LoRaWAN message sent from: " << this->id  << endl;
   this->old_phase =2;
   this->frequency=2;
   messageLoRA *mDiscover = new messageLoRA();
   mDiscover->setIdSrc(this->id);
   mDiscover->setName("Hibernate__discover");
   mDiscover->setKind(16);
   scheduleAt(simTime()+this->time, mDiscover);
   dispStr.setTagArg("i", 0, "device/devicered");
}

const vector<int>& LGW::getIdRegistered() const
{
    return idRegistered;
}

void LGW::setIdRegistered(const vector<int>& idRegistered)
{
    this->idRegistered = idRegistered;
}
void LGW::handleMessage(cMessage *msg)
{


    DEBUG EV << "MSG ID SOURCE: "<<((messageLoRA*)msg)->getIdSrc() << " MSG ID DEST: "<<((messageLoRA*)msg)->getIdDest() << endl;
    DEBUG for (unsigned i=0; i<this->idRegistered.size(); ++i)
    DEBUG  EV <<"Id registered ARRAY i:"<< i << " : "<< this->idRegistered[i] <<endl;
    if(this->frequency > 0)
    {
        isListeningHandleMessage((messageLoRA*)msg);
    }
    else
    {
        notListeningHandleMessage((messageLoRA*)msg);
    }
    if( ( !((messageLoRA*)msg)->isSelfMessage() ) && (this->frequency == 0) && !(this->discovered))
    {
        /*There is a LoRaWAN Gateway Near and I'm not registered yet*/
        LOG EV << "LoRa Gateway has received the Join request Message with timeout process " << endl;
        this->discovered=true;
        this->MyLW=((messageLoRA*)msg)->getIdSrc();
        this->slot=((messageLoRA*)msg)->getSlots();
        LOG EV << "Slot receive: "<< ((messageLoRA*)msg)->getSlots() <<endl;
        this->frequency=2;
        cDisplayString& dispStr = getDisplayString();
       const char* tmpColor= this->mycolor.c_str();
        dispStr.setTagArg("i", 0, tmpColor);
    }
    delete msg;
}

void LGW::notListeningHandleMessage(messageLoRA *msg)
{
    short choose = msg->getKind();
    if(msg->isSelfMessage())
    {
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        m->setIdDest(msg->getIdSrc());
        switch(choose)
        {
            case 15:
            {

                /*LoRaGateway is required to harvest data*/

                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
                LOG EV << "LoRa Gateway is waking up " << endl;
                this->frequency = this->old_phase ;

                messageLoRA *m1 = new messageLoRA();
                m1->setName("Data request");
                m1->setKind(4);
                m1->setIdSrc(this->id);
                int i,j;
                this->nb_harvest=0;
                for(j=0;j<this->idRegistered.size();j++)
                {
                    m1->setIdDest(this->idRegistered[j]);
                    for (i = 0; i < this->gateSize("channelsO"); i++)
                    {
                        messageLoRA *copy = m1->dup();
                        send(copy, "channelsO", i);
                    }
                }
                delete m1;
                LOG EV << "Data request Message sent from: " << this->id  << endl;

                break;
            }
            case 16:
            {
                if(this->discovered)
                {
                    /*We are already discovered*/
                }
                else
                {

                    cDisplayString& dispStr = getDisplayString();
                    const char* tmpColor= this->mycolor.c_str();
                    dispStr.setTagArg("i", 0, tmpColor);
                    messageLoRA *m = new messageLoRA();
                    char numstr[21];
                    sprintf(numstr, "%d", this->id);
                    string tmp = "Join request";
                    string tmp2 =tmp+numstr;
                    const char * c = tmp2.c_str();
                    this->MyLW=((messageLoRA*)msg)->getIdSrc();
                    m->setName(c);
                    m->setKind(0);
                    m->setIdSrc(this->id);
                    m->setIdDest(-1);
                    int i;
                    for (i = 0; i < this->gateSize("channelsO"); i++)
                    {
                        messageLoRA *copy = m->dup();
                        send(copy, "channelsO", i);
                    }
                    delete m;
                    LOG EV << "Join Request LoRaWAN message sent from: " << this->id  << endl;

                    messageLoRA *mDiscover = new messageLoRA();
                    mDiscover->setIdSrc(this->id);
                    mDiscover->setName("Hibernate__discover");
                    mDiscover->setKind(16);
                    scheduleAt(simTime()+this->time, mDiscover);

                    dispStr.setTagArg("i", 0, "device/devicered");
                }
                break;
            }
            case 17:{
                break;
            }
            default:{
                break;
            }
        }
    }
    else{
        LOG EV << "LoRa Gateway has received a message but is sleeping and waiting a self-message " << endl;
        LOG EV << " Message was from : " << this->id  << endl;

    }
}

double LGW::getOldPhase() const
{
    return old_phase;
}

void LGW::setOldPhase(double oldPhase)
{
    old_phase = oldPhase;
}

int LGW::getSlot() const
{
    return slot;
}

void LGW::setSlot(int slot)
{
    this->slot = slot;
}

void LGW::isListeningHandleMessage(messageLoRA *msg)
{

    LOG EV <<  "LGW: received: " << msg->getName() << " kind " << msg->getKind() << endl;

    messageLoRA *m = new messageLoRA();
    m->setSlots(this->slot);
    m->setIdSrc(this->id);
    m->setIdDest(msg->getIdSrc());
    switch(msg->getKind())
    {
        case 1:
        {
            if(this->discovered==true)
            {

                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
                m->setIdSrc(this->id);
                m->setIdDest(msg->getIdSrc());
                string result ;


                char numstr[21]; // enough to hold all numbers up to 64-bits
                sprintf(numstr, "%lu", msg->getIdSrc());
                string tmp ="Accept,";
                result = tmp + numstr;

                m->setName(result.c_str());
                m->setKind(2);
                m->setFrequency(2);
                int i;
                for (i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m->dup();
                    send(copy, "channelsO", i);
                }
                delete m;
                LOG EV << "Accept Message sent from: " << this->id  << endl;
            }
            break;
        }
        case 3: {
            if(this->discovered==true && msg->getIdDest()==this->id)
            {
                /*We received a Register message*/
                /*Check if we are the gateway of the device.*/
                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
                if(find(idRegistered.begin(), idRegistered.end(), msg->getIdSrc()) != idRegistered.end())
                {
                        /* We had  registered this Node yet, but it's possible he don't know yet */
                }
                else
                {
                        /* v does not contain x */

                        char numstr[21]; // enough to hold all numbers up to 64-bits
                        sprintf(numstr, "%lu", msg->getIdSrc());
                        string tmp ="END PAIRING W ";
                        string result = tmp + numstr;
                        bubble(result.c_str());

                        idRegistered.push_back (msg->getIdSrc());

                        LOG for (unsigned i=0; i<this->idRegistered.size(); ++i)
                        LOG  EV <<"Id registered ARRAY i:"<< i << " : "<< this->idRegistered[i] <<endl;

                }
                int i;
                messageLoRA *m_ACK_J_IN = new messageLoRA();
                m_ACK_J_IN->setSlots(this->slot);
                m_ACK_J_IN->setIdSrc(msg->getIdSrc());
                m_ACK_J_IN->setIdDest(this->MyLW);
                //Confirmed pairing with an IN
                m_ACK_J_IN->setName("CP_IN");
                m_ACK_J_IN->setKind(20);

                dispStr.setTagArg("i", 0, "device/devicered");
                for (i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m_ACK_J_IN->dup();
                    send(copy,"channelsO", i);
                }
                delete m_ACK_J_IN;

                m->setName("Data request");
                m->setKind(4);

                for (i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m->dup();
                    sendDelayed(copy,0.1, "channelsO", i);
                }
                delete m;
                LOG EV << "Data request Message sent from: " << this->id  << endl;


            }

            break;
        }
        case 5:
        {
            if(this->discovered==true && msg->getIdDest() == this->id)
            {
                /*We received a Data message*/
                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
                m->setName(msg->getName());
                m->setKind(7);
                LOG EV << "myLW: " << this->MyLW << endl;
                m->setIdSrc(msg->getIdSrc());
                m->setIdDest(this->MyLW);
                m->setIsolated(true);
                int i;
                for (i = 0; i < this->gateSize("channelsO"); i++)
                {
                   messageLoRA *copy = m->dup();
                   send(copy, "channelsO", i);
                }
                this->nb_harvest++;
                LOG EV << "Forwarding Data Message sent from: " << msg->getIdSrc()<< endl;
                /*On va faire hiberner le tout .*/
                if(this->nb_harvest == this->idRegistered.size()){
                    this->frequency=0;
                    messageLoRA *mHibernate = new messageLoRA();
                    mHibernate->setName("Hibernate_deactivate");
                    mHibernate->setKind(15);
                    mHibernate->setIdSrc(this->id);
                    scheduleAt(simTime()+this->slot, mHibernate);

                    dispStr.setTagArg("i", 0, "device/deviceblack");
                }
            }
            break;
        }
        case 6:
        {
            if(!(this->discovered))
            {
                /*There is a LoRaWAN Gateway Near and I'm not registered yet*/

                cDisplayString& connDispStr =  msg->getArrivalGate()->getDisplayString();
                connDispStr.parse("ls=red,3");

                connDispStr =  msg->getSenderGate()->getDisplayString();
                connDispStr.parse("ls=red,3");

                this->discovered=true;
                this->slot=msg->getSlots();
                this->MyLW=msg->getIdSrc();
                LOG EV << "Slot receive: "<< msg->getSlots() <<endl;
                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
            }
            break;
        }
        case 21: {

            break;
        }
    }


}


bool LGW::isDiscovered() const
{
    return discovered;
}

void LGW::setDiscovered(bool discovered)
{
    this->discovered = discovered;
}

double LGW::getFrequency() const
{
    return frequency;
}

void LGW::setFrequency(double frequency)
{
    this->frequency = frequency;
}

int LGW::getId() const
{
    return id;
}

void LGW::setId(int id)
{
    this->id = id;
}

int LGW::getNbIn() const
{
    return NbIN;
}

void LGW::setNbIn(int nbIn)
{
    NbIN = nbIn;
}
