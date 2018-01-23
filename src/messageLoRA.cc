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

#include "messageLoRA.h"

messageLoRA::messageLoRA() {
    // TODO Auto-generated constructor stub
    this->slots= 0;
    this->messageName="Not set yet";
    this->frequency=2;
}

double messageLoRA::getFrequency() const {
    return frequency;
}

void messageLoRA::setFrequency(double frequency) {
    this->frequency = frequency;
}

const string& messageLoRA::getMessageName() const {
    return messageName;
}

void messageLoRA::setMessageName(const string& messageName) {
    this->messageName = messageName;
}

messageLoRA::~messageLoRA() {
    // TODO Auto-generated destructor stub
}

long int messageLoRA::getIdSrc() const {
    return id_src;
}

void messageLoRA::setIdSrc(long int idSrc) {
    id_src = idSrc;
}

int messageLoRA::getSlots() const {
    return slots;
}

void messageLoRA::setSlots(int slots) {
    this->slots = slots;
}

long int messageLoRA::getIdDest() const {
    return id_dest;
}

void messageLoRA::setIdDest(long int idDest) {
    id_dest = idDest;
}
