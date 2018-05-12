#ifndef __LORA_LGW_H_
#define __LORA_LGW_H_
#include <omnetpp.h>
#include <time.h>
#include <unistd.h>
#include <vector>
#include "messageLoRA.h"
using namespace omnetpp;
using namespace std;
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
        int id,time,NbIN,slot,MyLW,nb_harvest;
        vector<int> idRegistered;
        vector<bool> isRegistered;
        double frequency;
        bool discovered;
        double old_phase;
        string mycolor;
        long long messageSend;
        static long long sumMessagesend;
        string filename_result;
        bool agreg;
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
