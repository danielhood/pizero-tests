from time import sleep
from gpiozero import LED

try:
    print ('Ready')

    # Pin number can be BCM or physical
    # gpiozero uses BCM by default
    led1 = LED(5)
    led2 = LED(7)
    led3 = LED(9)
    led4 = LED(11)
    led5 = LED(15) # pin 13 is used for pcm audio

    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()

    while True:
        print ("sparkling!")
        for i in range(1, 32):
            if i % 2 == 0:
                led1.on()
            else:
                led1.off()
            if i % 3 == 0:
                led2.on()
            else:
                led2.off()
            if i % 2 != 0:
                led3.on()
            else:
                led3.off()
            if i % 4 == 0:
                led4.on()
            else:
                led4.off()
            if i % 5 == 0:
                led5.on()
            else:
                led5.off()
            sleep(0.1)

        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()

        sleep(1)

except KeyboardInterrupt:
    print ("Exiting on user abort\n")

except Exception as e:
    print ("General error occurred\n")
    print (e)
