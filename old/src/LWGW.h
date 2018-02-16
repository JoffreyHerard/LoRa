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

#ifndef __LORA_LWGW_H_
#define __LORA_LWGW_H_

#include <omnetpp.h>
#include "messageLoRA.h"

using namespace omnetpp;
using namespace std;
/**
 * TODO - Generated class
 */
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
