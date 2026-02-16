import csv
from models.device import Device


class CsvStorage:
    """
    CSV (Comma-Separated Values) salvestus- ja laadimisklass seadmete jaoks.

    Nõue: Eesti CSV - eraldaja on semikoolon (;), olemas on päiserida,
    ning kõik seadme väljad salvestatakse.
    """

    FIELDNAMES = ["name", "device_type", "status", "location"]

    @staticmethod
    def save(file_path: str, devices: list[Device]) -> None:
        """
        Salvestab seadmete loendi CSV faili.

        :param file_path: Failitee, kuhu salvestatakse
        :param devices: Seadmete list
        """
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CsvStorage.FIELDNAMES, delimiter=";")
            writer.writeheader()

            for device in devices:
                writer.writerow({
                    "name": device.name,
                    "device_type": device.device_type,
                    "status": device.status,
                    "location": device.location
                })

    @staticmethod
    def load(file_path: str) -> list[Device]:
        """
        Laadib seadmed CSV failist.

        :param file_path: Failitee, kust laaditakse
        :return: Seadmete list
        """
        devices: list[Device] = []

        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                devices.append(Device(
                    name=row["name"],
                    device_type=row["device_type"],
                    status=row["status"],
                    location=row["location"]
                ))

        return devices
