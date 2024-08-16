class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Private parameters for TV status, mute, volume, channel
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    
    def power(self) -> None:
        '''
        Method to power TV on and off
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Method to mute TV volume to minimum
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume += 1
            else:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        '''
        Method to increase TV channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Method to decrease TV channel
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        '''
        Method to increase TV volume
        '''
        if self.__status:
            if self.__muted:
                self.__volume += 1
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrease TV volume
        '''
        if self.__status:
            if self.__muted:
                self.__volume += 2
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to show TV status.
        :return: tv status.
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'