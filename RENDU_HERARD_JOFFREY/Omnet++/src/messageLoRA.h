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
        messageLoRA(const messageLoRA&);
        virtual messageLoRA *dup() const {return new messageLoRA(*this);}
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
