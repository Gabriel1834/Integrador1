#include <Streaming.h>

const int analogPin = 4;           // Pino ADC (GPIO36)
const float offsetVoltage = 2500.0; // Tensão de offset (mV) quando I = 0A (ex: ACS712)
const float sensitivity = 185.0;    // Sensibilidade do sensor (mV/A) - ACS712-5A = 185mV/A

// Função que lê o ADC e retorna a corrente em Amperes (A)
float readCurrent() {
  int adcValue = analogRead(analogPin);        // Lê o valor do ADC (0-4095)
  float voltage = (adcValue * 3300.0) / 4095.0; // Converte para mV (3.3V = 3300mV)
  float current = (voltage - offsetVoltage) / sensitivity; // Calcula a corrente (A)
  return current;
}

void setup() {
  Serial.begin(9600);
  analogReadResolution(12); // Configura o ADC para 12 bits (0-4095)
}

void loop() {
  float current = readCurrent(); // Chama a função que retorna a corrente
  
  // Exibe a corrente no Serial Monitor
  Serial.print("Corrente: ");
  Serial.print(current, 3); // 3 casas decimais
  Serial.println(" A");
   // Espera 1 segundo
   delay(500);
}