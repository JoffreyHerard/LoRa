#include "IsoN.h"
#include <string.h>
Define_Module(IsoN);
using namespace std;
long long IsoN::sumMessagesend;
void IsoN::initialize()
{
    int i;
    this->myLoRa=-1;
    this->frequency=0;
    this->data = 0 ;
    this->discovered=false;
    this->registered=false;
    this->id = par("id").longValue();
    this->file= par("file").stringValue();
    this->batterie= par("battery").longValue();
    this->tv=0;
    this->cout_envoi=this->te*this->ce;
    this->cout_receive=this->tr*this->cr;
    this->slot=1;
    this->cout_veille=this->slot*this->cv;
    //this->batterie=this->batterie-this->cout_envoi;
    //this->batterie=this->batterie-this->cout_receive;
    //this->batterie=this->batterie-this->cout_veille;
    this->messageSend = 0 ;
    cDisplayString& dispStr = getDisplayString();
    dispStr.setTagArg("i",0,"device/devicegreen");
    /*if(this->id == 22){
        dispStr.parse("p=250,350;i=device/devicegreen");
    }

    if( this->id == 25){
        dispStr.parse("p=550,350;i=device/devicegreen");
    }*/


    /* generate number between 1 and 100: */
    this->time = this->slot;

    LOG EV << "Isolated Node Starting: " << id << endl;

    messageLoRA *m = new messageLoRA();
    m->setName("Discover");
    m->setKind(1);
    m->setFrequency(1);
    m->setIdSrc(this->id);
    m->setIdDest(-1);

    for (i = 0; i < this->gateSize("channelsO"); i++)
    {
        messageLoRA *copy = m->dup();
        send(copy, "channelsO", i);

    }

    this->batterie=this->batterie-this->cout_envoi;
    this->messageSend++;
    if(this->batterie<0){
        finish();
    }
    delete m;

    LOG EV << "Discovery Message sent from: " << this->id <<" number: "<< data << endl;


    messageLoRA *mDiscover = new messageLoRA();
    mDiscover->setIdSrc(this->id);
    mDiscover->setName("Hibernate__discover");
    mDiscover->setKind(16);
    scheduleAt(simTime()+this->time, mDiscover);

    this->data++;
}


void IsoN::handleMessage(cMessage *msg)
{
    DEBUG EV << "MSG ID SOURCE: "<<((messageLoRA*)msg)->getIdSrc() << " MSG ID DEST: "<<((messageLoRA*)msg)->getIdDest() << " MSG kind: "<<((messageLoRA*)msg)->getKind() << endl;
    DEBUG EV << "Mon id de LoRaGATEWAY c'est: " <<this->myLoRa << endl;

    if(this->frequency > 0)
    {

         this->batterie=this->batterie-this->cout_receive;
         if(this->batterie<0){
             finish();
         }
         DEBUG EV << "Je vais la 1" << endl;
         isListeningHandleMessage((messageLoRA*)msg);
    }
    else
    {
         DEBUG EV << "Je vais la 2" << endl;
         notListeningHandleMessage((messageLoRA*)msg);

    }
    if( ( !((messageLoRA*)msg)->isSelfMessage() ) && (this->frequency == 0) && !(this->registered))
    {
        /*special section dedicate to managed special thing like timeOut on registering*/
        DEBUG EV << "Je vais la 3" << endl;
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        /* I receive an accept request*/
        this->batterie=this->batterie-this->cout_receive;
        if(this->batterie<0){
            finish();
        }
        if(msg->getKind() == 2)
        {
            if(!(this->discovered) && ((messageLoRA*)msg)->getIdDest()==this->id){
                cDisplayString& dispStr = getDisplayString();

                /*There is a LoRa Gateway Near and I'm not registered yet*/
                this->myLoRa=((messageLoRA*)msg)->getIdSrc();
                switch(this->myLoRa){
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

                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);

                this->frequency= ((messageLoRA*)msg)->getFrequency();
                this->old_phase =this->frequency;
                m->setName("Register");
                m->setKind(3);
                m->setIdDest(this->myLoRa);
                m->setIdSrc(this->id);
                int i;
                for (i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m->dup();
                    send(copy, "channelsO", i);
                }

                this->batterie=this->batterie-this->cout_envoi;
                this->messageSend++;
                if(this->batterie<0){
                    finish();
                }
                delete m;
                LOG EV << "Register Message sent from: " << this->id << endl;
                this->discovered=true;
                this->slot=((messageLoRA*)msg)->getSlots();
                this->cout_veille=this->slot*this->cv;
                dispStr.setTagArg("i", 0, "device/devicered");
                messageLoRA *mHibernate = new messageLoRA();
                mHibernate->setIdSrc(this->id);
                mHibernate->setName("Hibernate_registered?");
                mHibernate->setKind(17);
                scheduleAt(simTime()+this->slot, mHibernate);
                this->frequency =0 ;
            }
        }
        if(msg->getKind() == 4 && ((messageLoRA*)msg)->getIdDest()==this->id)
        {

            cDisplayString& dispStr = getDisplayString();
            this->myLoRa=((messageLoRA*)msg)->getIdSrc();
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
            int i;
            for (i = 0; i < this->gateSize("channelsO"); i++)
            {
                messageLoRA *copy = m->dup();
                send(copy, "channelsO", i);
            }

            this->batterie=this->batterie-this->cout_envoi;
            this->messageSend++;
            if(this->batterie<0){
                finish();
            }
            delete m;
            LOG EV << "Data Response sent from: " << this->id << endl;

            /*Everybody will sleep right now .*/
            this->frequency=0;
            messageLoRA *mHibernate = new messageLoRA();
            mHibernate->setIdSrc(this->id);
            mHibernate->setName("Hibernate_deactivate");
            mHibernate->setKind(15);
            scheduleAt(simTime()+this->slot, mHibernate);

            const char* tmpColor= this->mycolor.c_str();
            dispStr.setTagArg("i", 0, tmpColor);
        }

    }
    delete msg;
}

void IsoN::notListeningHandleMessage(messageLoRA *msg)
{
    messageLoRA *mDiscover = new messageLoRA();
    short choose = msg->getKind();
    if(msg->isSelfMessage())
    {
        messageLoRA *m = new messageLoRA();
        m->setIdSrc(this->id);
        switch(choose)
        {
            case 15:
            {

                this->batterie=this->batterie-this->cout_veille;
                if(this->batterie<0){
                    finish();
                }
                /*LoRaGateway is required to harvest data*/
                LOG EV << "Isolated Node is waking up " << endl;
                this->frequency = this->old_phase ;
                cDisplayString& dispStr = getDisplayString();
                const char* tmpColor= this->mycolor.c_str();
                dispStr.setTagArg("i", 0, tmpColor);
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
                    /*We are not already discovered*/
                    //this->myLoRa=((messageLoRA*)msg)->getIdSrc();
                    cDisplayString& dispStr = getDisplayString();
                    dispStr.setTagArg("i", 0, "device/devicegreen");
                    m->setName("Discover");
                    m->setKind(1);
                    m->setFrequency(1);
                    int i;
                    for (i = 0; i < this->gateSize("channelsO"); i++)
                    {
                        messageLoRA *copy = m->dup();
                        send(copy, "channelsO", i);
                    }

                    this->batterie=this->batterie-this->cout_envoi;
                    this->messageSend++;
                    if(this->batterie<0){
                        finish();
                    }
                    delete m;
                    LOG EV << "Discovery Message sent from: " << this->id <<" number: "<< data << endl;


                    messageLoRA *mDiscover = new messageLoRA();
                    mDiscover->setIdSrc(this->id);
                    mDiscover->setName("Hibernate__discover");
                    mDiscover->setKind(16);
                    scheduleAt(simTime()+this->time, mDiscover);
                    dispStr.setTagArg("i", 0, "device/devicered");
                }
                break;
            }
            case 17:
            {
                /*I am registered???*/
                /*We are not already registered*/
                if(!this->registered)
                {
                    cDisplayString& dispStr = getDisplayString();
                    const char* tmpColor= this->mycolor.c_str();
                    dispStr.setTagArg("i", 0, tmpColor);
                    m->setName("Register");
                    m->setKind(3);
                    m->setIdDest(this->myLoRa);
                    m->setIdSrc(this->id);
                    int i;
                    for (i = 0; i < this->gateSize("channelsO"); i++)
                    {
                        messageLoRA *copy = m->dup();
                        send(copy, "channelsO", i);
                    }

                    this->batterie=this->batterie-this->cout_envoi;
                    this->messageSend++;
                    if(this->batterie<0){
                        finish();
                    }
                    delete m;
                    LOG EV << "NotListeningPhase : Register Message sent from: " << this->id << endl;
                    mDiscover->setIdSrc(this->id);
                    mDiscover->setName("Hibernate_registered");
                    mDiscover->setKind(17);
                    scheduleAt(simTime()+this->time, mDiscover);
                    dispStr.setTagArg("i", 0, "device/devicered");
                }
                else
                {
                    this->frequency = this->old_phase ;
                }
                break;
            }
            default:{
                break;
            }
        }
    }
    else
    {
        LOG EV <<"Not a self message"<<endl;
    }
}

double IsoN::getOldPhase() const
{
    return old_phase;
}

void IsoN::setOldPhase(double oldPhase)
{
    old_phase = oldPhase;
}

int IsoN::getSlot() const
{
    return slot;
}

void IsoN::setSlot(int slot)
{
    this->slot = slot;
}

void IsoN::isListeningHandleMessage(messageLoRA *msg)
{
    messageLoRA *m = new messageLoRA();
    LOG EV <<  "received: " << msg->getName() << " kind " << msg->getKind() << endl;

    switch(msg->getKind())
    {
        case 2:
        {
            if(!(this->discovered))
            {
                /*There is a LoRa Gateway Near and I'm not registered yet*/
                cDisplayString& dispStr = getDisplayString();
                dispStr.setTagArg("i", 0, "device/devicegreen");
                this->myLoRa=((messageLoRA*)msg)->getIdSrc();
                this->frequency= msg->getFrequency();
                this->old_phase =this->frequency;
                m->setName("Register");
                m->setKind(3);
                m->setIdDest(this->myLoRa);
                m->setIdSrc(this->id);
                int i;
                for (int i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m->dup();
                    send(copy, "channelsO", i);
                }

                this->batterie=this->batterie-this->cout_envoi;
                this->messageSend++;
                if(this->batterie<0){
                    finish();
                }
                delete m;
                LOG EV << "Register Message sent from: " << this->id << endl;
                this->discovered=true;
                this->slot=msg->getSlots();
                this->cout_veille=this->slot*this->cv;
                messageLoRA *mHibernate = new messageLoRA();
                mHibernate->setIdSrc(this->id);
                mHibernate->setName("Hibernate_registered?");
                mHibernate->setKind(17);
                scheduleAt(simTime()+this->slot, mHibernate);
                this->frequency =0 ;
                dispStr.setTagArg("i", 0, "device/devicered");
            }
            break;
        }
        case 4:
        {
            if(msg->getIdDest() == this->id){ /*There is a LoRa Gateway Near and this one want my data*/
                if (!this->registered)
                    this->registered=true;
                char numstr[21];
                sprintf(numstr, "%d", this->data);
                string tmp =numstr;
                const char * c = tmp.c_str();

                cDisplayString& dispStr = getDisplayString();
                dispStr.setTagArg("i", 0, "device/devicegreen");

                m->setFrequency(2);
                m->setName(c);
                m->setKind(5);
                m->setIdDest(this->myLoRa);
                m->setIdSrc(this->id);
                int i;
                for (int i = 0; i < this->gateSize("channelsO"); i++)
                {
                    messageLoRA *copy = m->dup();
                    send(copy, "channelsO", i);
                }

                this->batterie=this->batterie-this->cout_envoi;
                this->messageSend++;
                if(this->batterie<0){
                    finish();
                }
                delete m;
                LOG EV << "Data Response sent from: " << this->id << endl;

                /*Everybody will sleep right now .*/
                this->frequency=0;
                messageLoRA *mHibernate = new messageLoRA();
                mHibernate->setIdSrc(this->id);
                mHibernate->setName("Hibernate_deactivate");
                mHibernate->setKind(15);
                scheduleAt(simTime()+this->slot, mHibernate);

                //this->batterie=this->batterie-this->cout_veille;
                dispStr.setTagArg("i", 0, "device/deviceblack");
                break;
                }
        }
    }
    this->data++;

}

void IsoN::finish()
{
    this->sumMessagesend= this->sumMessagesend+ this->messageSend;
    //this->sumMessagesend= this->sumMessagesend+ this->messageSend;
    ofstream objetfichier;
    string path="results/"+this->file+"/IN_"+std::to_string(this->id);
    objetfichier.open(path, ios::out);
    if (objetfichier.bad())
    {
       LOG EV << "Failed to open file"<< endl;
    }
    else{
       objetfichier <<this->messageSend << endl;
       objetfichier <<this->batterie << endl;
       objetfichier.close();
    }
}
int IsoN::getData() const
{
    return data;
}

void IsoN::setData(int data)
{
    this->data = data;
}

bool IsoN::isDiscovered() const
{
    return discovered;
}

void IsoN::setDiscovered(bool discovered)
{
    this->discovered = discovered;
}

double IsoN::getFrequency() const
{
    return frequency;
}

void IsoN::setFrequency(double frequency)
{
    this->frequency = frequency;
}

int IsoN::getId() const
{
    return id;
}

void IsoN::setId(int id)
{
    this->id = id;
}


