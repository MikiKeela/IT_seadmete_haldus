import json
from models.device import Device


class JsonStorage:
    """
    JSON salvestamise ja laadimise klass.
    Vastutab seadmete andmete kirjutamise ja lugemise eest JSON failist.
    """

    @staticmethod
    def save(file_path: str, devices: list[Device]) -> None:
        """
        Salvestab seadmete loendi JSON faili.

        :param file_path: Failitee, kuhu andmed salvestatakse
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
        Laeb seadmed JSON failist ja tagastab need loendina.

        :param file_path: Failitee, kust andmed loetakse
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
