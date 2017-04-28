#include <wiringPi.h>
#include <mcp23017.h>

#define AF_BASE 100
#define I2C_ADD 0x20

#define ROW1   1
#define ROW2   2
#define ROW3   3
#define ROW4   4

#define COL1   115
#define COL2   114
#define COL3   107
#define COL4   108

int main(int argc, char** argv) {

   wiringPiSetup();
   mcp23017Setup(AF_BASE, I2C_ADD);

   /* Inizializzo gli array per le righe e le colonne */
   int rows[4] = {ROW1, ROW2, ROW3, ROW4};
   int cols[4] = {COL1, COL2, COL3, COL4};
   int keypad[4][4] = {{'1', '2', '3', 'A'}, {'4', '5', '6', 'B'},   {'7', '8', '9', 'C'}, {'*', '0', '#', 'D'}};

   int i, j;

   /* imposto le colonne come uscite e le imposto a livello alto */
   for(i=0; i<4; i++){
      pinMode(cols[i], OUTPUT);
      digitalWrite(cols[i], HIGH);
   }

   /* Imposto le righe come ingressi con PULL_UP */
   for(j=0; j<4; j++){
      pinMode(rows[i], INPUT);
      pullUpDnControl(rows[i], PUD_UP);
   }

   printf("Premi un pulsante sulla tastiera:\n");

   /* Inizio il ciclo per vedere che bottone viene premuto */
   while(1){

      for(i=0; i<4; i++){
         /* Metto la colonna corrente a 0 e vedo se qualche riga va a zero */
         digitalWrite(cols[i], LOW);

         /* Controllo lo stato delle righe. Se una va a zero, un bottone è stato premuto */
         for(j=0; j<4; j++){

            if(digitalRead(rows[j])==LOW){
               printf("%c\n", keypad[j][i]);
               /* Attendi che il pulsante sia rilasciato */
               while(digitalRead(rows[j])==0){
               }
            }
         }
         /* Rimetto la colonna corrente a 1 */
         digitalWrite(cols[i], HIGH);
      }
   }

}
