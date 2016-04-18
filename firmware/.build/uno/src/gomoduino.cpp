#include <Arduino.h>

void setup();
void loop();
#line 1 "src/gomoduino.ino"
#define LED_POMODORO_PIN 11
#define LED_RECESS_PIN 12

int pomodoro = LOW; // Are we on a pomodoro?
int recess = LOW; // Are we on a recess?
int val; // Value read from the serial port

void setup()
{
    pinMode(LED_POMODORO_PIN, OUTPUT); // sets the digital pin as output
    pinMode(LED_RECESS_PIN, OUTPUT); // sets the digital pin as output
    pomodoro = LOW;
    recess = LOW;
    Serial.begin(9600);
    Serial.flush();
}

void loop()
{
    // Read from serial port
    if (Serial.available())
    {
        val = Serial.read();
        Serial.println(val);
        if (val == 'P') {
                pomodoro = HIGH;
                recess = LOW;
        }
        else if (val == 'R') {
                pomodoro = LOW;
                recess = HIGH;
        }
    }

    // Set the status of the output pin
    digitalWrite(LED_POMODORO_PIN, pomodoro);
    digitalWrite(LED_RECESS_PIN, recess);
}