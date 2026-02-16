class Device:
    """
    Seadme klass, mis kirjeldab ühte IT-seadet.
    """

    ALLOWED_STATUSES = ["available", "in_use", "broken"]

    def __init__(self, name: str, device_type: str, status: str, location: str):
        """
        Initsialiseerib uue seadme objekti.

        :param name: Seadme nimi
        :param device_type: Seadme tüüp
        :param status: Seadme staatus (available, in_use, broken)
        :param location: Seadme asukoht
        """

        if status not in self.ALLOWED_STATUSES:
            raise ValueError("Vale staatus. Lubatud: available, in_use, broken")

        self.name = name
        self.device_type = device_type
        self.status = status
        self.location = location

    def __str__(self):
        return f"{self.name} | {self.device_type} | {self.status} | {self.location}"
