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

#include "LWGW.h"

Define_Module(LWGW);

void LWGW::initialize()
{
    // TODO - Generated method body
    LOG EV << "LoRaWAN Gateway Started"<< endl;
    this->frequency=1;
    this->slot=5;
    this->id = par("id").longValue();
}

void LWGW::handleMessage(cMessage *msg)
{
    LOG EV << "MSG ID SOURCE: "<<((messageLoRA*)msg)->getIdSrc() << "MSG ID DEST: "<<((messageLoRA*)msg)->getIdDest() << endl;
    if(this->frequency > 0){
        isListeningHandleMessage((messageLoRA*)msg);
    }
    else{
        notListeningHandleMessage((messageLoRA*)msg);
    }
}


void LWGW::notListeningHandleMessage(messageLoRA *msg){

    short choose = msg->getKind();

    if(msg->isSelfMessage()){
        LOG EV << "LoRaWAN Gateway has received a self message " << endl;
        messageLoRA *m = new messageLoRA();
        switch(choose){
            case 15:{
                /*LoRaWANGATEWAY is required to harvest data*/
                LOG EV << "LoRaWAN Gateway is waking up " << endl;
                this->frequency = this->old_phase ;

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
        LOG EV << "LoRaWAN Gateway has received a message but is sleeping and waiting a self-message " << endl;
    }
}

int LWGW::getSlot() const {
    return slot;
}

void LWGW::setSlot(int slot) {
    this->slot = slot;
}

void LWGW::isListeningHandleMessage(messageLoRA *msg){
   LOG EV << "LoRaWAN Gateway has received message during a listening Phase" << endl;
   messageLoRA *m = new messageLoRA();
   m->setIdDest(msg->getIdSrc());
   m->setIdSrc(this->id);
   switch(msg->getKind()){
       case 0 :{
           m->setName("Join Accept");
           m->setKind(6);
           m->setSlots(this->slot);
           send(m,"LWGWtoLGW");
           LOG EV << "LoRaWAN Gateway registered a LoRa Gateway" << endl;
           this->discovered=true;
           this->idRegistered.push_back(msg->getIdSrc());
           break;
       }
       case 2 :{
           m->setName("Join Accept isolated node");
           m->setKind(21);
           this->idRegisteredLGW.push_back(msg->getIdSrc());
           send(m,"LWGWtoLGW");
           LOG EV << "LoRaWAN Gateway registered a isolated node from LoRa Gateway" << endl;
           this->discovered=true;
           break;
       }
       case 7 :{
           if(msg->getIdDest() == this->id){
               LOG EV <<  "received data : " << msg->getName() << " " << endl;
               this->discovered=true;
               /*On va faire hiberner le tout .*/
               this->frequency=0;
               messageLoRA *mHibernate = new messageLoRA();
               mHibernate->setName("Hibernate_deactivate");
               mHibernate->setKind(15);
               scheduleAt(simTime()+this->slot, mHibernate);
               break;
           }else{
               LOG EV << "I received a message that was not destined to me"<< endl;
           }
       }
   }


}

bool LWGW::isDiscovered() const {
    return discovered;
}

void LWGW::setDiscovered(bool discovered) {
    this->discovered = discovered;
}

const double LWGW::getFrequency() const {
    return frequency;
}


void LWGW::setFrequency(double frequency) {
    this->frequency = frequency;
}

const vector<int>& LWGW::getIdRegistered() const {
    return idRegistered;
}


const vector<int>& LWGW::getIdRegisteredLgw() const {
    return idRegisteredLGW;
}


double LWGW::getOldPhase() const {
    return old_phase;
}

void LWGW::setOldPhase(double oldPhase) {
    old_phase = oldPhase;
}

