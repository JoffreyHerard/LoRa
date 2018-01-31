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

#ifndef __LORA_LGW_H_
#define __LORA_LGW_H_

#include <omnetpp.h>
#include <time.h>       /* time */
#include <unistd.h>
#include <vector>
#include "messageLoRA.h"

using namespace omnetpp;
using namespace std;
/**
 * TODO - Generated class
 */
class LGW : public cSimpleModule{
public:
    bool isDiscovered() const;
    void setDiscovered(bool discovered);
    double getFrequency() const;
    void setFrequency(double frequency);
    int getId() const;
    void setId(int id);
    int getNbIn() const;
    void setNbIn(int nbIn);
    const vector<int>& getIdRegistered() const;
    void setIdRegistered(const vector<int>& idRegistered);
    double getOldPhase() const;
    void setOldPhase(double oldPhase);
    int getSlot() const;
    void setSlot(int slot);

  private:
    int id,time;
    int NbIN;
    vector<int> idRegistered;
    vector<bool> isRegistered;
    double frequency;
    bool discovered;
    double old_phase;
    int slot;
    int MyLW;
    int nb_harvest;
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
    void notListeningHandleMessage(messageLoRA *msg);
    void isListeningHandleMessage(messageLoRA *msg);
};

#endif
