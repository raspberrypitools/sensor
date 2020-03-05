#include <wiringPi.h>
#include <stdio.h>
#include <sys/time.h>

#define FIRE    29

int main(void)
{

    if (wiringPiSetup() == -1) 
    { 
        printf("setup wiringPi failed !");
        return 1; 
    }
    
    pinMode(FIRE, INPUT);        
    
    while (1) 
    {
        if (digitalRead(FIRE) == 1)
        {
            printf("no fire\n");
            delay(333);
        }
        else
        {
            printf("fire detected\n");
            delay(333);
        }
    }
        
    return 0;
}
