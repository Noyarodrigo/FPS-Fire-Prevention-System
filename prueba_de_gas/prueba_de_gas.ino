// Pin del Arduino donde conectamos la pata A0 del módulo
#define GAS_PIN A0
// Cambio en las lecturas (en porcentaje) que consideraremos significativo
#define CAMBIO_SIGNIFICATIVO 3

void setup() {
  Serial.begin(9600);
  Serial.println("Deteccion de gas con MQ-2...");
}

// Para guardar el valor anterior y solo mostrar cambios significativos
int analogValue = -1;

void loop() {
 Serial.println(analogRead(0));
  delay(1500);
}
