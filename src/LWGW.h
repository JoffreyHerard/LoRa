#ifndef __LORA_LWGW_H_
#define __LORA_LWGW_H_
#include <omnetpp.h>
#include "messageLoRA.h"

using namespace omnetpp;
using namespace std;
class LWGW : public cSimpleModule
{
public:
    bool isDiscovered() const;
    void setDiscovered(bool discovered);
    const double getFrequency() const;
    void setFrequency(double frequency);
    const vector<int>& getIdRegistered() const;
    void setIdRegistered(const vector<int>& idRegistered);
    const vector<int>& getIdRegisteredLgw() const;
    void setIdRegisteredLgw(const vector<int>& idRegisteredLgw);
    double getOldPhase() const;
    void setOldPhase(double oldPhase);
    int getSlot() const;
    void setSlot(int slot);

  private:
    bool discovered;
    double frequency;
    double old_phase;
    vector<int> idRegistered;
    vector<int> idRegisteredLGW;
    int slot,id;
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
    void notListeningHandleMessage(messageLoRA *msg);
    void isListeningHandleMessage(messageLoRA *msg);
};

#endif
