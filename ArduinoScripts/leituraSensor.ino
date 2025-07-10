// Array com os números dos pinos analógicos a serem lidos
const int pinosAnalogicos[] = {14, 25, 26, 27, 32, 33, 34, 35, 36, 39};
const int numPinos = sizeof(pinosAnalogicos) / sizeof(pinosAnalogicos[0]);

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < numPinos; i++) {
    pinMode(pinosAnalogicos[i], INPUT);
  }
}

void loop() {
  int maiorValor = 0;
  int pinoDoMaior = -1;

  // Percorre todos os pinos e identifica o maior valor
  for (int i = 0; i < numPinos; i++) {
    int valorLido = analogRead(pinosAnalogicos[i]);
    if (valorLido > maiorValor) {
      maiorValor = valorLido;
      pinoDoMaior = pinosAnalogicos[i];
    }
  }

  // Imprime no estilo "PinoXX:valor" somente se o valor for relevante
  if (maiorValor > 400 && pinoDoMaior != -1) {
    Serial.print("Pino");
    Serial.print(pinoDoMaior);
    Serial.print(":");
    Serial.println(maiorValor);
  }

  delay(300);
}
