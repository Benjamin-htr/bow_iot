import paho.mqtt.client as mqtt


class mqtt_observer:
    onButton1Pressed = None
    onButton1Released = None
    onButton2Pressed = None
    onButton2Released = None
    onPotarChanged = None
    setRfid = None
    onUltChanged = None

    def sendVictory(self):
        self.client.publish("AP5iot/victory", "youhou", 2)

    def sendScore(self, score):
        self.client.publish("AP5iot/score", score, 2)

    def on_mes(self, client, userdata, mes):
        msg = mes.payload.decode("utf-8")
        if mes.topic == "AP5iot/btn/1":
            if int(msg) and self.onButton1Pressed:
                self.onButton1Pressed()
            elif self.onButton1Released:
                print("controller relaese")
                self.onButton1Released()
        elif mes.topic == "AP5iot/btn/2":
            if int(msg) and self.onButton2Pressed:
                self.onButton2Pressed()
            elif self.onButton2Released:
                self.onButton2Released()
        elif mes.topic == "AP5iot/potar":
            if self.onPotarChanged:
                self.onPotarChanged(int(msg))
        elif mes.topic == "AP5iot/ult":
            if self.onUltChanged:
                print("control distance")
                self.onUltChanged(float(msg))
        elif mes.topic == "AP5iot/card":
            if self.setRfid:
                self.setRfid(msg)

    def __init__(
        self,
        onButton1Pressed=None,
        onButton1Released=None,
        onButton2Pressed=None,
        onButton2Released=None,
        onPotarChanged=None,
        setRfid=None,
        onUltChanged=None,
    ):
        self.onButton1Pressed = onButton1Pressed
        self.onButton1Released = onButton1Released
        self.onButton2Pressed = onButton2Pressed
        self.onButton2Released = onButton2Released
        self.onPotarChanged = onPotarChanged
        self.setRfid = setRfid
        self.onUltChanged = onUltChanged
        self.client = mqtt.Client()
        self.client.on_message = self.on_mes
        self.client.connect("192.168.1.102", 1883)
        self.client.subscribe("AP5iot/#", 2)
        self.client.loop_start()

    def reset(self):
        self.onButton1Pressed = None
        self.onButton1Released = None
        self.onButton2Pressed = None
        self.onButton2Released = None
        self.onPotarChanged = None
        self.setRfid = None
        self.onUltChanged = None
