//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

#include "LGW.h"

Define_Module(LGW);

void LGW::initialize()
{

   EV << "LoRA Gateway started"<< endl;
   this->frequency=0;
   messageLoRA *m = new messageLoRA();
   this->id = par("id").longValue();

   char numstr[21];
   sprintf(numstr, "%d", this->id);
   string tmp = "Join request";
   string tmp2 =tmp+numstr;
   const char * c = tmp2.c_str();

   m->setName(c);
   m->setKind(0);
   m->setIdSrc(this->id);
   send(m,"LGWtoLWGW");
   EV << "Join Request LoRaWAN message sent from: " << this->id  << endl;
   this->frequency=2;
   this->old_phase =this->frequency;
}

const vector<int>& LGW::getIdRegistered() const {
    return idRegistered;
}

void LGW::setIdRegistered(const vector<int>& idRegistered) {
    this->idRegistered = idRegistered;
}
void LGW::handleMessage(cMessage *msg)
{
    if(this->frequency > 0){
        isListeningHandleMessage((messageLoRA*)msg);
    }
    else{
        notListeningHandleMessage((messageLoRA*)msg);
    }
}

void LGW::notListeningHandleMessage(messageLoRA *msg){
    EV << "LoRa Gateway has received a message " << endl;
    short choose = msg->getKind();
    if(msg->isSelfMessage()){
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        switch(choose){
            case 15:{
                /*LoRaGateway is required to harvest data*/
                EV << "LoRa Gateway is waking up " << endl;
                this->frequency = this->old_phase ;

                messageLoRA *m1 = new messageLoRA();
                m1->setName("Data request");
                m1->setKind(4);
                send(m1,"LGWtoIN");
                EV << "Data request Message sent from: " << this->id  << endl;

                break;
            }
            case 16:{
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
        EV << "LoRa Gateway has received a message but is sleeping and waiting a self-message " << endl;
        EV << " Message was from : " << this->id  << endl;

    }
}

double LGW::getOldPhase() const {
    return old_phase;
}

void LGW::setOldPhase(double oldPhase) {
    old_phase = oldPhase;
}

int LGW::getSlot() const {
    return slot;
}

void LGW::setSlot(int slot) {
    this->slot = slot;
}

void LGW::isListeningHandleMessage(messageLoRA *msg){
    messageLoRA *m = new messageLoRA();
    m->setSlots(this->slot);
    EV <<  "LGW: received: " << msg->getName() << " kind " << msg->getKind() << endl;
    m->setIdSrc(this->id);
    if(msg->getKind() == 6 && !(this->discovered) )
    {
        /*There is a LoRaWAN Gateway Near and I'm not registered yet*/
        this->discovered=true;
        this->slot=msg->getSlots();
        EV << "Slot receive: "<< msg->getSlots() <<endl;
    }
    if(msg->getKind() == 21 )
    {
        m->setName("Accept");
        m->setKind(2);
        m->setFrequency(2);
        idRegistered.push_back(msg->getIdSrc());
        send(m,"LGWtoIN");
        EV << "Accept Message sent from: " << this->id  << endl;
    }
    if(msg->getKind() == 1 )
    {
        /*We received a Discover message and we attempt to register it to the LoRaWAN Gateway*/
        messageLoRA *mjoin = new messageLoRA();
        mjoin->setName("Registering isolated node");
        mjoin->setKind(2);
        mjoin->setIdSrc(msg->getIdSrc());
        mjoin->setSlots(this->slot);

        send(mjoin,"LGWtoLWGW");
        EV << "Join Request LoRaWAN message sent from: " << this->id  << endl;

     }

    if(msg->getKind() == 3 )
    {
        /*We received a Register message*/
        //idRegistered.push_back (NbIN);
        NbIN++;
        m->setName("Data request");
        m->setKind(4);
        send(m,"LGWtoIN");
        EV << "Data request Message sent from: " << this->id  << endl;
    }

    if(msg->getKind() == 5 )
    {
        /*We received a Data message*/
        m->setName(msg->getName());
        m->setKind(7);
        send(m,"LGWtoLWGW");
        EV << "Data Message sent from: " << this->id << endl;
        /*On va faire hiberner le tout .*/
        this->frequency=0;
        messageLoRA *mHibernate = new messageLoRA();
        mHibernate->setName("Hibernate_deactivate");
        mHibernate->setKind(15);
        mHibernate->setIdSrc(this->id);

        scheduleAt(simTime()+this->slot, mHibernate);
    }
    delete msg;
}


bool LGW::isDiscovered() const {
    return discovered;
}

void LGW::setDiscovered(bool discovered) {
    this->discovered = discovered;
}

double LGW::getFrequency() const {
    return frequency;
}

void LGW::setFrequency(double frequency) {
    this->frequency = frequency;
}

int LGW::getId() const {
    return id;
}

void LGW::setId(int id) {
    this->id = id;
}

int LGW::getNbIn() const {
    return NbIN;
}

void LGW::setNbIn(int nbIn) {
    NbIN = nbIn;
}
