#include "LWGW.h"
Define_Module(LWGW);

void LWGW::initialize()
{
    LOG EV << "LoRaWAN Gateway Started"<< endl;
    this->frequency=1;
    this->slot=5;
    this->id = par("id").longValue();

    cDisplayString& dispStr = getDisplayString();
    //dispStr.parse("p=350,20;i=device/antennatower");
    dispStr.setTagArg("i", 0, "device/antennatower");
}

void LWGW::handleMessage(cMessage *msg)
{
    LOG EV << "MSG ID SOURCE: "<<((messageLoRA*)msg)->getIdSrc() << " MSG ID DEST: "<<((messageLoRA*)msg)->getIdDest() << endl;
    if(this->frequency > 0)
    {
        isListeningHandleMessage((messageLoRA*)msg);
    }
    else
    {
        notListeningHandleMessage((messageLoRA*)msg);
    }
    delete msg;
}


void LWGW::notListeningHandleMessage(messageLoRA *msg)
{

    short choose = msg->getKind();

    if(msg->isSelfMessage())
    {
        LOG EV << "LoRaWAN Gateway has received a self message " << endl;
        messageLoRA *m = new messageLoRA();
        switch(choose){
            case 15:
            {
                /*LoRaWANGATEWAY is required to harvest data*/
                LOG EV << "LoRaWAN Gateway is waking up " << endl;
                this->frequency = this->old_phase ;

                break;
            }
            case 16:
            {
                break;
            }
            case 17:
            {
                break;
            }
            default:
            {
                break;
            }
        }
    }
    else
    {
        LOG EV << "LoRaWAN Gateway has received a message but is sleeping and waiting a self-message " << endl;
    }
}

int LWGW::getSlot() const
{
    return slot;
}

void LWGW::setSlot(int slot)
{
    this->slot = slot;
}

void LWGW::isListeningHandleMessage(messageLoRA *msg)
{
   LOG EV << "LoRaWAN Gateway has received message during a listening Phase" << endl;
   messageLoRA *m = new messageLoRA();
   m->setIdDest(msg->getIdSrc());
   m->setIdSrc(this->id);
   switch(msg->getKind())
   {
       case 0 :
       {
           m->setName("Join Accept");
           m->setKind(6);
           m->setSlots(this->slot);
           int i;
           for (i = 0; i < this->gateSize("channelsO"); i++)
           {
              messageLoRA *copy = m->dup();
              send(copy, "channelsO", i);
           }
           LOG EV << "LoRaWAN Gateway registered a LoRa Gateway" << endl;
           this->discovered=true;
           this->idRegistered.push_back(msg->getIdSrc());
           break;
       }
       case 20 :
       {
           if(msg->getIdDest() == this->id)
           {
               if(find(idRegistered.begin(), idRegistered.end(), msg->getIdSrc()) != idRegistered.end())
               {
                   /* We had  registered this Node yet, but it's possible he don't know yet */
               }
               else
               {
                   /* v does not contain x */
                   idRegistered.push_back (msg->getIdSrc());
                   LOG for (unsigned i=0; i<this->idRegistered.size(); ++i)
                   LOG      EV <<"Id registered ARRAY i:"<< i << " : "<< this->idRegistered[i] <<endl;

               }
           }
           break;
       }
       case 7 :
       {
           if(msg->getIdDest() == this->id)
           {
               LOG EV <<  "received data : " << msg->getName() << " " << endl;
               if(msg->isIsolated() && find(idRegistered.begin(), idRegistered.end(), msg->getIdSrc()) != idRegistered.end())
               {
                  /* We had  registered this Node yet, but it's possible he don't know yet */
               }
               else
               {
                  /* v does not contain x */
                  idRegistered.push_back (msg->getIdSrc());
                  LOG for (unsigned i=0; i<this->idRegistered.size(); ++i)
                  LOG      EV <<"Id registered ARRAY i:"<< i << " : "<< this->idRegistered[i] <<endl;

               }
               /*On va faire hiberner le tout .*/
               this->frequency=0;
               messageLoRA *mHibernate = new messageLoRA();
               mHibernate->setName("Hibernate_deactivate");
               mHibernate->setKind(15);
               scheduleAt(simTime()+this->slot, mHibernate);
               break;
           }
           else
           {
               LOG EV << "I received a message that was not destined to me"<< endl;
           }
       }
   }


}

bool LWGW::isDiscovered() const
{
    return discovered;
}

void LWGW::setDiscovered(bool discovered)
{
    this->discovered = discovered;
}

const double LWGW::getFrequency() const
{
    return frequency;
}


void LWGW::setFrequency(double frequency)
{
    this->frequency = frequency;
}

const vector<int>& LWGW::getIdRegistered() const
{
    return idRegistered;
}


const vector<int>& LWGW::getIdRegisteredLgw() const
{
    return idRegisteredLGW;
}


double LWGW::getOldPhase() const
{
    return old_phase;
}

void LWGW::setOldPhase(double oldPhase)
{
    old_phase = oldPhase;
}

