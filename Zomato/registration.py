import abc


class Registration():
    @abc.abstractmethod
    def Register(self):
        pass


class CreateRestaurant(Registration):

    def Register(self):
        return super().Register()


class CreateDeliveryBoy(Registration):

    def Register(self):
        return super().Register()


class CreateUser(Registration):

    def Register(self):
        return super().Register()
