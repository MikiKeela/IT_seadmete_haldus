from models.device import Device
from storage.csv_storage import CsvStorage
from storage.json_storage import JsonStorage


class DeviceManager:
    """
    Seadmete haldurklass, mis tegeleb seadmete lisamise, kuvamise,
    seisundi muutmise ja kustutamisega.
    """

    def __init__(self):
        """
        Loob seadmete halduri ja valmistab ette tühja seadmete loendi.
        """
        self.devices: list[Device] = []

    def add_device(self, device: Device) -> None:
        """
        Lisab seadmete loendisse uue seadme.

        :param device: Device objekt, mis lisatakse loendisse
        """
        self.devices.append(device)

    def list_devices(self) -> list[Device]:
        """
        Tagastab kõik seadmed loendina.

        :return: Seadmete list
        """
        return self.devices

    def update_device_status(self, index: int, new_status: str) -> None:
        """
        Muudab valitud seadme staatust.

        :param index: Seadme indeks loendis (0-põhine)
        :param new_status: Uus staatus (available, in_use, broken)
        """
        if index < 0 or index >= len(self.devices):
            raise IndexError("Sellise indeksiga seadet ei ole olemas.")

        if new_status not in Device.ALLOWED_STATUSES:
            raise ValueError("Vale staatus. Lubatud: available, in_use, broken")

        self.devices[index].status = new_status

    def delete_device(self, index: int) -> None:
        """
        Kustutab valitud seadme loendist.

        :param index: Seadme indeks loendis (0-põhine)
        """
        if index < 0 or index >= len(self.devices):
            raise IndexError("Sellise indeksiga seadet ei ole olemas.")

        self.devices.pop(index)
    def save_to_csv(self, file_path: str) -> None:
        """
        Salvestab seadmete loendi CSV faili.

        :param file_path: Failitee, kuhu salvestatakse
        """
        CsvStorage.save(file_path, self.devices)

    def load_from_csv(self, file_path: str) -> None:
        """
        Laadib seadmed CSV failist ja asendab olemasoleva loendi.

        :param file_path: Failitee, kust laaditakse
        """
        self.devices = CsvStorage.load(file_path)

    def save_to_json(self, file_path: str) -> None:
        """
        Salvestab seadmete loendi JSON faili.

        :param file_path: Failitee, kuhu salvestatakse
        """
        JsonStorage.save(file_path, self.devices)

    def load_from_json(self, file_path: str) -> None:
        """
        Laadib seadmed JSON failist ja asendab olemasoleva loendi.

        :param file_path: Failitee, kust laaditakse
        """
        self.devices = JsonStorage.load(file_path)
