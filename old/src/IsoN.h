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

#ifndef __LORA_ISON_H_
#define __LORA_ISON_H_

#include <omnetpp.h>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <unistd.h>
#include "messageLoRA.h"

using namespace omnetpp;
using namespace std;
/**
 * TODO - Generated class
 */
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
    int id,time,data;
    bool discovered,registered;
    double frequency,old_phase;
    int slot;
    int myLoRa;
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
    void notListeningHandleMessage(messageLoRA *msg);
    void isListeningHandleMessage(messageLoRA *msg);
};

#endif
