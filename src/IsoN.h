#ifndef __LORA_ISON_H_
#define __LORA_ISON_H_
#include <omnetpp.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <unistd.h>
#include <fstream>
#include "messageLoRA.h"
using namespace omnetpp;
using namespace std;
class IsoN : public cSimpleModule
{
  public:
    double getFrequency() const;
    void setFrequency(double frequency);
    int getId() const;
    void setId(int id);
    int getX() const;
    void setX(int x);
    bool isDiscovered() const;
    void setDiscovered(bool discovered);
    int getData() const;
    void setData(int data);
    double getOldPhase() const;
    void setOldPhase(double oldPhase);
    int getSlot() const;
    void setSlot(int slot);
  private:
    int id,time,data,tryDiscover;
    bool discovered,registered;
    double frequency,old_phase;
    int slot;
    int myLoRa;
    string mycolor;
    long long messageSend;
    static long long sumMessagesend;
    string file;
    double batterie; // en mAs
    double const ce= 107.3; // en mA
    double const cr = 37 ; // en mA
    double const cv= 0.531; // en mA
    double const te=2; // en secondes
    double const tr=2; // en secondes
    double tv;
    double cout_envoi;
    double cout_receive;
    double cout_veille;
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
    void notListeningHandleMessage(messageLoRA *msg);
    void isListeningHandleMessage(messageLoRA *msg);
    virtual void finish();
};

#endif
