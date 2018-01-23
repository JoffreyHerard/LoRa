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

#include "IsoN.h"

Define_Module(IsoN);
using namespace std;

void IsoN::initialize()
{

    this->frequency=1;
    this->data = 0 ;
    this->discovered=false;
    this->registered=false;
    this->id = par("id").longValue();
    this->slot=1;


    /* generate number between 1 and 100: */
    this->time = this->slot +1;

    EV << "Isolated Node Starting: " << id << endl;

    messageLoRA *m = new messageLoRA();
    m->setName("Discover");
    m->setKind(1);
    m->setFrequency(1);
    m->setIdSrc(this->id);
    send(m,"INtoLGW");
    EV << "Discovery Message sent from: " << this->id <<" number: "<< data << endl;


    messageLoRA *mDiscover = new messageLoRA();
    mDiscover->setIdSrc(this->id);
    mDiscover->setName("Hibernate__discover");
    mDiscover->setKind(16);
    scheduleAt(simTime()+this->time, mDiscover);

    this->data++;
}


void IsoN::handleMessage(cMessage *msg){
    if(this->frequency > 0){
         isListeningHandleMessage((messageLoRA*)msg);

    }
    else{
         notListeningHandleMessage((messageLoRA*)msg);
    }
    if( ( !((messageLoRA*)msg)->isSelfMessage() ) && (this->frequency == 0) && !(this->registered)){
        /*special section dedicate to managed special thing like timeOut on registering*/
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        /* I receive a data request*/
        if(msg->getKind() == 4)
        {
            /*There is a LoRa Gateway Near and this one want my data*/
            if (!this->registered)
                this->registered=true;
            char numstr[21];
            sprintf(numstr, "%d", this->data);
            string tmp =numstr;
            const char * c = tmp.c_str();

            m->setFrequency(2);
            m->setName(c);
            m->setKind(5);
            m->setIdDest(((messageLoRA*)msg)->getIdSrc());
            send(m,"INtoLGW");
            EV << "Data Response sent from: " << this->id << endl;

            /*Everybody will sleep right now .*/
            this->frequency=0;
            messageLoRA *mHibernate = new messageLoRA();
            mHibernate->setIdSrc(this->id);
            mHibernate->setName("Hibernate_deactivate");
            mHibernate->setKind(15);
            scheduleAt(simTime()+this->slot, mHibernate);
        }
    }
}

void IsoN::notListeningHandleMessage(messageLoRA *msg){
    messageLoRA *mDiscover = new messageLoRA();
    short choose = msg->getKind();
    if(msg->isSelfMessage()){
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        switch(choose){
            case 15:{
                /*LoRaGateway is required to harvest data*/
                EV << "Isolated Node is waking up " << endl;
                this->frequency = this->old_phase ;
                break;
            }
            case 16:{
                if(this->discovered){
                    /*We are already discovered*/
                }else{
                    /*We are not already discovered*/
                    m->setName("Discover");
                    m->setKind(1);
                    m->setFrequency(1);
                    m->setIdSrc(this->id);
                    send(m,"INtoLGW");
                    EV << "Discovery Message sent from: " << this->id <<" number: "<< data << endl;


                    messageLoRA *mDiscover = new messageLoRA();
                    mDiscover->setIdSrc(this->id);
                    mDiscover->setName("Hibernate__discover");
                    mDiscover->setKind(16);
                    scheduleAt(simTime()+this->time, mDiscover);
                }
                break;
            }
            case 17:{
                /*I am registered???*/
                /*We are not already discovered*/
                if(!this->registered){
                    m->setName("Register");
                    m->setKind(3);
                    send(m,"INtoLGW");
                    EV << "NotListeningPhase : Register Message sent from: " << this->id << endl;
                    mDiscover->setIdSrc(this->id);
                    mDiscover->setName("Hibernate_registered");
                    mDiscover->setKind(16);
                    scheduleAt(simTime()+this->time, mDiscover);

                }else{
                    this->frequency = this->old_phase ;
                }
                break;
            }
            default:{
                break;
            }
        }
    }
    else{
    }
}

double IsoN::getOldPhase() const {
    return old_phase;
}

void IsoN::setOldPhase(double oldPhase) {
    old_phase = oldPhase;
}

int IsoN::getSlot() const {
    return slot;
}

void IsoN::setSlot(int slot) {
    this->slot = slot;
}

void IsoN::isListeningHandleMessage(messageLoRA *msg){
    messageLoRA *m = new messageLoRA();
    m->setIdSrc(this->id);
    m->setIdDest(msg->getIdSrc());
    EV <<  "received: " << msg->getName() << " kind " << msg->getKind() << endl;

    if(msg->getKind() == 2 && !(this->discovered)){
        /*There is a LoRa Gateway Near and I'm not registered yet*/
        this->frequency= msg->getFrequency();
        this->old_phase =this->frequency;
        m->setName("Register");
        m->setKind(3);
        send(m,"INtoLGW");
        EV << "Register Message sent from: " << this->id << endl;
        this->discovered=true;
        this->slot=msg->getSlots();

        messageLoRA *mHibernate = new messageLoRA();
        mHibernate->setIdSrc(this->id);
        mHibernate->setName("Hibernate_registered?");
        mHibernate->setKind(17);
        scheduleAt(simTime()+this->slot, mHibernate);
        this->frequency =0 ;
    }

    /* I receive a data request*/
    if(msg->getKind() == 4 )
    {
        /*There is a LoRa Gateway Near and this one want my data*/
        if (!this->registered)
            this->registered=true;
        char numstr[21];
        sprintf(numstr, "%d", this->data);
        string tmp =numstr;
        const char * c = tmp.c_str();

        m->setFrequency(2);
        m->setName(c);
        m->setKind(5);
        m->setIdDest(msg->getIdSrc());
        send(m,"INtoLGW");
        EV << "Data Response sent from: " << this->id << endl;

        /*Everybody will sleep right now .*/
        this->frequency=0;
        messageLoRA *mHibernate = new messageLoRA();
        mHibernate->setIdSrc(this->id);
        mHibernate->setName("Hibernate_deactivate");
        mHibernate->setKind(15);
        scheduleAt(simTime()+this->slot, mHibernate);
    }
    this->data++;
    delete msg;
}

int IsoN::getData() const {
    return data;
}

void IsoN::setData(int data) {
    this->data = data;
}

bool IsoN::isDiscovered() const {
    return discovered;
}

void IsoN::setDiscovered(bool discovered) {
    this->discovered = discovered;
}

double IsoN::getFrequency() const {
    return frequency;
}

void IsoN::setFrequency(double frequency) {
    this->frequency = frequency;
}

int IsoN::getId() const {
    return id;
}

void IsoN::setId(int id) {
    this->id = id;
}


