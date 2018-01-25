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

#ifndef MESSAGELORA_H_
#define MESSAGELORA_H_

#include <omnetpp/cmessage.h>
#include <vector> /*required for slots definition*/
#include <ctime> /*required for slots definition*/

#include "frequency.h"

using namespace std;

class messageLoRA: public omnetpp::cMessage {
    private:
        string messageName;
        double frequency;
        int slots;
        long int id_src;
        long int id_dest;
        bool isolated;
    public:
        messageLoRA();
        virtual ~messageLoRA();
        
        double getFrequency() const;
        void setFrequency(double frequency);
        const string& getMessageName() const;
        void setMessageName(const string& messageName);
        long int getIdSrc() const;
        void setIdSrc(long int idSrc);
        int getSlots() const;
        void setSlots(int slots);
        long int getIdDest() const;
        void setIdDest(long int idDest);
        bool isIsolated() const;
        void setIsolated(bool isolated);
};

#endif /* MESSAGELORA_H_ */
