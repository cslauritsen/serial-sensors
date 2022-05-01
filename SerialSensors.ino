
#define MAX_REPORT_MILLIS 1000L * 60L * 10L // 10 minutes
#define LINEBUF_LEN 512
#define INPUT_PIN_COUNT 64
int digitalInputPins[] = { 22, 24, 26, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, -1 };
int values1[INPUT_PIN_COUNT];
int values2[INPUT_PIN_COUNT];
char inbuf[LINEBUF_LEN];
char outbuf[LINEBUF_LEN];
void setup()
{
    Serial.begin(9600);
    for (int *p = digitalInputPins; *p >= 0; p++) {
        pinMode(*p, INPUT_PULLUP);
        Serial.print("# input on ");
        Serial.print(*p);
        Serial.print('=');
        Serial.println(digitalRead(*p));
    }

    memset(inbuf, 0, LINEBUF_LEN);
    memset(values1, -1, sizeof(*values1) * INPUT_PIN_COUNT);
    memset(values2, -1, sizeof(*values2) * INPUT_PIN_COUNT);
}

int *theseValues = values1;
int *lastValues = values2;
long lastMillis = -1;
long thisMillis = -1;
void loop() {
    delay(100);

    thisMillis = millis();
    memset(inbuf, 0, LINEBUF_LEN);
    memset(outbuf, 0, LINEBUF_LEN);
    for (int i=0; Serial.available() && i < LINEBUF_LEN; i++) {
        inbuf[i] = Serial.read(); 
        if (inbuf[i] == '\n') {
            break;
        }
    }

    int t=0;
    int pos = 0;
    for (int *p = digitalInputPins; *p != -1; p++) {
        theseValues[t] = digitalRead(*p);
        if (lastMillis == -1 
            || thisMillis - lastMillis > MAX_REPORT_MILLIS 
            || theseValues[t] != lastValues[t]) {
                pos += snprintf(outbuf+pos, 
                    LINEBUF_LEN, 
                    "%s%d=%d", 
                    pos>0?";":"", 
                    *p, 
                    theseValues[t]);
        }
        t++;
    }

    // swap these with last
    if (theseValues == values1) {
        lastValues = values1;
        theseValues = values2;
    }
    else {
        lastValues = values2;
        theseValues = values1;
    }

    if (strlen(outbuf) > 0) {
        Serial.println(outbuf);
        lastMillis = thisMillis;
    }
}
