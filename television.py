class Television:
    Min_VOLUME = 0
    Max_VOLUME = 2
    Min_CHANNEL = 0
    Max_CHANNEL = 3

    def __init__(self):
        self.__status = False # The TV is off by default
        self.__muted = False # The TV is not muted by default
        self.__volume = Television.Min_VOLUME # The minimum volume is default
        self.__channel = Television.Min_CHANNEL # the minimum channel is default

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            self.__muted = self.__muted

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.Max_CHANNEL + 1)

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.Max_CHANNEL + 1)

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.Max_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.Max_VOLUME:
                self.__volume -= 1

    def __str__(self):
        power_status = "on" if self.__status else "off"
        return f"power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}"


