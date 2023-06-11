import RPi.GPIO as gpio
import time

#Pinos das leds
led1 = 26
led2 = 10
led3 = 17
led4 = 19
led5 = 9
led6 = 27
led7 = 13
led8 = 11
led9 = 23
 
gpio.setmode(gpio.BCM)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
gpio.setup(led4,gpio.OUT)
gpio.setup(led5,gpio.OUT)
gpio.setup(led6,gpio.OUT)
gpio.setup(led7,gpio.OUT)
gpio.setup(led8,gpio.OUT)
gpio.setup(led9,gpio.OUT)

#Botoes com entrada BCM
gpio.setup(4,gpio.IN,pull_up_down=gpio.PUD_DOWN)
gpio.setup(14,gpio.IN,pull_up_down=gpio.PUD_DOWN)

def ON(led):
    gpio.setup(led,gpio.OUT)
    gpio.output(led,gpio.HIGH)

def OFF(led):
    gpio.setup(led,gpio.OUT)
    gpio.output(led,gpio.LOW)


#COMBINAÇÂO 1
def sequencia3():
    ON(led3)
    time.sleep(1)
    OFF(led3)
    time.sleep(1)
    ON(led2)
    ON(led6)
    time.sleep(1)
    OFF(led2)
    OFF(led6)
    time.sleep(1)
    ON(led1)
    ON(led5)
    ON(led9)
    time.sleep(1)
    OFF(led1)
    OFF(led5)
    OFF(led9)
    time.sleep(1)
    ON(led4)
    ON(led8)
    time.sleep(1)
    OFF(led4)
    OFF(led8)
    time.sleep(1)
    ON(led7)
    time.sleep(1)
    OFF(led7)

def sequencia7():
    ON(led7)
    time.sleep(1)
    ON(led4)
    ON(led8)
    time.sleep(1)
    ON(led1)
    ON(led5)
    ON(led9)
    time.sleep(1)
    ON(led2)
    ON(led6)
    time.sleep(1)
    ON(led3)
    time.sleep(1)
    OFF(led7)
    OFF(led4)
    OFF(led8)
    OFF(led9)
    OFF(led5)
    OFF(led1)
    OFF(led6)
    OFF(led2)

def sequencia11():
    ON(led3)
    time.sleep(1)
    ON(led2)
    ON(led6)
    time.sleep(1)
    ON(led1)
    ON(led5)
    ON(led9)
    time.sleep(1)
    ON(led4)
    ON(led8)
    time.sleep(1)
    ON(led7)
    time.sleep(1)
    OFF(led3)
    OFF(led2)
    OFF(led6)
    OFF(led9)
    OFF(led5)
    OFF(led1)
    OFF(led8)
    OFF(led4)
    OFF(led7)

def sequencia15():
    ON(led1)
    ON(led2)
    time.sleep(1)
    ON(led3)
    ON(led6)
    time.sleep(1)
    ON(led9)
    ON(led8)
    time.sleep(1)
    ON(led7)
    ON(led4)
    time.sleep(1)
    ON(led5)
    time.sleep(1)
    OFF(led3)
    OFF(led2)
    OFF(led6)
    OFF(led1)
    OFF(led5)
    OFF(led9)
    OFF(led4)
    OFF(led8)
    OFF(led7)

def sequencia19():
    ON(led5)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led9)
    ON(led7)
    time.sleep(1)
    OFF(led1)
    OFF(led3)
    OFF(led9)
    OFF(led7)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led9)
    ON(led7)
    time.sleep(1)
    OFF(led3)
    OFF(led1)
    OFF(led9)
    OFF(led7)
    time.sleep(1)
    OFF(led5)

def sequencia23():
    ON(led1)
    ON(led5)
    ON(led9)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    ON(led3)
    ON(led7)
    time.sleep(1)
    OFF(led1)
    OFF(led5)
    OFF(led9)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    OFF(led3)
    OFF(led7)

#COMBINAÇÂO 2
def sequencia1():
    ON(led1)
    time.sleep(1)
    OFF(led1)
    time.sleep(1)
    ON(led2)
    ON(led4)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    time.sleep(1)
    ON(led3)
    ON(led5)
    ON(led7)
    time.sleep(1)
    OFF(led3)
    OFF(led5)
    OFF(led7)
    time.sleep(1)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led9)
    time.sleep(1)
    OFF(led9)

def sequencia5():
    ON(led5)
    time.sleep(1)
    OFF(led5)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led5)
    ON(led7)
    ON(led9)
    time.sleep(1)
    OFF(led1)
    OFF(led3)
    OFF(led5)
    OFF(led7)
    OFF(led9)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led7)
    ON(led9)
    time.sleep(1)
    OFF(led1)
    OFF(led3)
    OFF(led6)
    OFF(led9)
    time.sleep(1)

def sequencia9():
    ON(led1)
    time.sleep(1)
    ON(led2)
    ON(led4)
    time.sleep(1)
    ON(led3)
    ON(led5)
    ON(led7)
    time.sleep(1)
    ON(led6)
    ON(led8)
    time.sleep(1)
    ON(led9)
    time.sleep(1)
    OFF(led1)
    OFF(led2)
    OFF(led3)
    OFF(led4)
    OFF(led5)
    OFF(led6)
    OFF(led7)
    OFF(led8)
    OFF(led9)
    time.sleep(1)
    
def sequencia13():
    ON(led9)
    time.sleep(1)
    ON(led6)
    ON(led8)
    time.sleep(1)
    ON(led3)
    ON(led5)
    ON(led7)
    time.sleep(1)
    ON(led2)
    ON(led4)
    time.sleep(1)
    ON(led1)
    time.sleep(1)
    OFF(led1)
    OFF(led2)
    OFF(led3)
    OFF(led4)
    OFF(led5)
    OFF(led6)
    OFF(led7)
    OFF(led8)
    OFF(led9)
    time.sleep(1)

def sequencia17():
    ON(led1)
    ON(led9)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    ON(led3)
    ON(led5)
    ON(led7)
    time.sleep(1)
    OFF(led1)
    OFF(led9)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    OFF(led3)
    OFF(led5)
    OFF(led7)
    time.sleep(1)

def sequencia21():
    ON(led5,gpio.HIGH)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led7)
    ON(led9)
    time.sleep(1)
    OFF(led1)
    OFF(led3)
    OFF(led7)
    OFF(led9)
    time.sleep(1)
    OFF(led5)
    time.sleep(1)

#COMBINAÇÂO 3
def sequencia4():
    ON(led9)
    time.sleep(1)
    OFF(led9)
    time.sleep(1)
    ON(led6)
    ON(led8)
    time.sleep(1)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    ON(led3)
    ON(led5)
    ON(led7)
    time.sleep(1)
    OFF(led3)
    OFF(led5)
    OFF(led7)
    time.sleep(1)
    ON(led2)
    ON(led4)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    time.sleep(1)
    ON(led1)
    time.sleep(1)
    OFF(led1)
    time.sleep(1)

def sequencia8():
    ON(led1)
    ON(led2)
    ON(led3)
    ON(led4)
    ON(led5)
    ON(led6)
    ON(led7)
    ON(led8)
    ON(led9)
    time.sleep(1)
    OFF(led7)
    time.sleep(1)
    OFF(led4)
    OFF(led8)
    time.sleep(1)
    OFF(led1)
    OFF(led5)
    OFF(led9)
    time.sleep(1)
    OFF(led2)
    OFF(led6)
    time.sleep(1)
    OFF(led3)
    time.sleep(1)

def sequencia12():
    ON(led1)
    ON(led2)
    ON(led3)
    ON(led4)
    ON(led5)
    ON(led6)
    ON(led7)
    ON(led8)
    ON(led9)
    time.sleep(1)
    OFF(led3)
    time.sleep(1)
    OFF(led2)
    OFF(led6)
    time.sleep(1)
    OFF(led1)
    OFF(led5)
    OFF(led9)
    time.sleep(1)
    OFF(led4)
    OFF(led8)
    time.sleep(1)
    OFF(led7)
    time.sleep(1)

def sequencia20():
    ON(led1)
    ON(led2)
    ON(led3)
    ON(led4)
    ON(led5)
    ON(led6)
    ON(led7)
    ON(led8)
    ON(led9)
    time.sleep(1)
    OFF(led5)
    time.sleep(1)
    OFF(led1)
    OFF(led3)
    OFF(led7)
    OFF(led9)
    time.sleep(1)
    OFF(led2)
    ON(led1)
    OFF(led4)
    ON(led3)
    OFF(led6)
    ON(led7)
    OFF(led8)
    ON(led9)
    time.sleep(1)
    ON(led2)
    OFF(led1)
    ON(led4)
    OFF(led3)
    ON(led6)
    OFF(led7)
    ON(led8)
    OFF(led9)
    time.sleep(1)
    ON(led1)
    ON(led3)
    ON(led7)
    ON(led9)
    time.sleep(1)
    ON(led5)
    time.sleep(1)

def sequencia24():
    ON(led1)
    ON(led5)
    ON(led7)
    time.sleep(1)
    ON(led2)
    ON(led4)
    ON(led6)
    ON(led8)
    time.sleep(1)
    ON(led1)
    ON(led9)
    time.sleep(1)
    OFF(led3)
    OFF(led5)
    OFF(led7)
    time.sleep(1)
    OFF(led2)
    OFF(led4)
    OFF(led6)
    OFF(led8)
    time.sleep(1)
    OFF(led1)
    OFF(led9)
    time.sleep(1)

while True:
    #Combinação1
    if gpio.input(4) == gpio.HIGH and gpio.input(14) == gpio.LOW:
        sequencia3();sequencia7();sequencia11();sequencia15();sequencia19();sequencia23()

    #Combinação2
    if gpio.input(4) == gpio.LOW and gpio.input(14) == gpio.HIGH:
        sequencia1();sequencia5();sequencia9();sequencia13();sequencia17();sequencia21()

    #Combinação3
    if gpio.input(4) == gpio.HIGH and gpio.input(14) == gpio.HIGH:
        sequencia4();sequencia8();sequencia12();sequencia20();sequencia24()
    
