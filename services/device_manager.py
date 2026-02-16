from models.device import Device
from storage.csv_storage import CsvStorage
from storage.json_storage import JsonStorage


class DeviceManager:

    def __init__(self):
        self.devices: list[Device] = []

    def add_device(self, device: Device) -> None:
        self.devices.append(device)

    def list_devices(self) -> list[Device]:
        return self.devices

    def update_device_status(self, index: int, new_status: str) -> None:
        if index < 0 or index >= len(self.devices):
            raise IndexError("Sellise indeksiga seadet ei ole olemas.")

        if new_status not in Device.ALLOWED_STATUSES:
            raise ValueError("Vale staatus. Lubatud: available, in_use, broken")

        self.devices[index].status = new_status

    def delete_device(self, index: int) -> None:
        if index < 0 or index >= len(self.devices):
            raise IndexError("Sellise indeksiga seadet ei ole olemas.")

        self.devices.pop(index)
    def save_to_csv(self, file_path: str) -> None:

        CsvStorage.save(file_path, self.devices)

    def load_from_csv(self, file_path: str) -> None:
       self.devices = CsvStorage.load(file_path)

    def save_to_json(self, file_path: str) -> None:
        JsonStorage.save(file_path, self.devices)

    def load_from_json(self, file_path: str) -> None:
        self.devices = JsonStorage.load(file_path)
