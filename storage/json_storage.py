import json
from models.device import Device


class JsonStorage:
    """
    JSON (JavaScript Object Notation) salvestus- ja laadimisklass seadmete jaoks.
    Salvestab ja loeb kõik seadme väljad.
    """

    @staticmethod
    def save(file_path: str, devices: list[Device]) -> None:
        """
        Salvestab seadmete loendi JSON faili.

        :param file_path: Failitee, kuhu salvestatakse
        :param devices: Seadmete list
        """
        data = []
        for device in devices:
            data.append({
                "name": device.name,
                "device_type": device.device_type,
                "status": device.status,
                "location": device.location
            })

        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def load(file_path: str) -> list[Device]:
        """
        Laadib seadmed JSON failist.

        :param file_path: Failitee, kust laaditakse
        :return: Seadmete list
        """
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)

        devices: list[Device] = []
        for item in data:
            devices.append(Device(
                name=item["name"],
                device_type=item["device_type"],
                status=item["status"],
                location=item["location"]
            ))

        return devices
