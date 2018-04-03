/*
 * frequency.h
 *
 *  Created on: 22 janv. 2018
 *      Author: JoffreyHerard
 */

#ifndef FREQUENCY_H_
#define FREQUENCY_H_

#define LOG if(0)
#define DEBUG if(0)

/*EU 863-870MHz ISM Band*/
#define EU_A_1 868.10   /* as 1 in receivePhase */
#define EU_A_2 868.30   /* as 2 in receivePhase */
#define EU_A_3 868.50   /* as 3 in receivePhase */
#define EU_A_4 864.10   /* as 4 in receivePhase */
#define EU_A_5 864.30   /* as 5 in receivePhase */
#define EU_A_6 864.50   /* as 6 in receivePhase */
#define EU_B_1 869.525  /* as 7 in receivePhase*/

#define RECEIVE_DELAY1 1
#define RECEIVE_DELAY2 2
#define JOIN_ACCEPT_DELAY1 5
#define JOIN_ACCEPT_DELAY2 6
#define MAX_FCNT_GAP 16384
#define ADR_ACK_LIMIT 64
#define ADR_ACK_DELAY 32
#define ACK_TIMEOUT 2
#endif /* FREQUENCY_H_ */
