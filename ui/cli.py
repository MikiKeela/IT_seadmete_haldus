from models.device import Device
from services.device_manager import DeviceManager


def run() -> None:
    manager = DeviceManager()

    while True:
        _print_menu()
        choice = input("Vali tegevus: ").strip()

        if choice == "1":
            _add_device_flow(manager)
        elif choice == "2":
            _list_devices(manager)
        elif choice == "3":
            _update_status_flow(manager)
        elif choice == "4":
            _delete_device_flow(manager)
        elif choice == "5":
            _save_flow(manager)
        elif choice == "6":
            _load_flow(manager)
        elif choice == "0":
            print("Head aega!")
            break
        else:
            print("Tundmatu valik. Proovi uuesti.")


def _print_menu() -> None:
    print("\n=== IT seadmete haldus ===")
    print("1) Lisa seade")
    print("2) Kuva seadmed")
    print("3) Muuda seadme seisundit")
    print("4) Kustuta seade")
    print("5) Salvesta (CSV või JSON)")
    print("6) Laadi (CSV või JSON)")
    print("0) Välju")


def _ask_non_empty(prompt_text: str) -> str:
   while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("Sisend ei tohi olla tühi.")


def _ask_int(prompt_text: str) -> int:
    while True:
        raw = input(prompt_text).strip()
        try:
            return int(raw)
        except ValueError:
            print("Sisesta täisarv.")


def _ask_status() -> str:
    while True:
        status = input("Sisesta staatus (available / in_use / broken): ").strip()
        if status in Device.ALLOWED_STATUSES:
            return status
        print("Vale staatus. Lubatud: available, in_use, broken")


def _ask_format() -> str:
    while True:
        fmt = input("Vali formaat (csv/json): ").strip().lower()
        if fmt in ["csv", "json"]:
            return fmt
        print("Vale valik. Sisesta csv või json.")


def _list_devices(manager: DeviceManager) -> None:
    devices = manager.list_devices()
    if not devices:
        print("Seadmete loend on tühi.")
        return

    print("\n--- Seadmed ---")
    for i, device in enumerate(devices, start=1):
        print(f"{i}) {device}")


def _add_device_flow(manager: DeviceManager) -> None:
    name = _ask_non_empty("Sisesta seadme nimi: ")
    device_type = _ask_non_empty("Sisesta seadme tüüp: ")
    status = _ask_status()
    location = _ask_non_empty("Sisesta seadme asukoht: ")

    try:
        manager.add_device(Device(name, device_type, status, location))
        print("Seade lisatud.")
    except ValueError as e:
        print(f"Viga: {e}")


def _update_status_flow(manager: DeviceManager) -> None:
    _list_devices(manager)
    if not manager.list_devices():
        return

    number = _ask_int("Sisesta seadme number (1..n): ")
    index = number - 1
    new_status = _ask_status()

    try:
        manager.update_device_status(index, new_status)
        print("Seisund muudetud.")
    except (IndexError, ValueError) as e:
        print(f"Viga: {e}")


def _delete_device_flow(manager: DeviceManager) -> None:
   _list_devices(manager)
    if not manager.list_devices():
        return

    number = _ask_int("Sisesta seadme number (1..n): ")
    index = number - 1

    try:
        manager.delete_device(index)
        print("Seade kustutatud.")
    except IndexError as e:
        print(f"Viga: {e}")


def _save_flow(manager: DeviceManager) -> None:
    fmt = _ask_format()
    if fmt == "csv":
        manager.save_to_csv("data/devices.csv")
        print("Salvestatud faili: data/devices.csv")
    else:
        manager.save_to_json("data/devices.json")
        print("Salvestatud faili: data/devices.json")


def _load_flow(manager: DeviceManager) -> None:
    fmt = _ask_format()
    try:
        if fmt == "csv":
            manager.load_from_csv("data/devices.csv")
            print("Laaditud failist: data/devices.csv")
        else:
            manager.load_from_json("data/devices.json")
            print("Laaditud failist: data/devices.json")
    except FileNotFoundError:
        print("Faili ei leitud. Salvesta enne vähemalt üks kord.")
    except Exception as e:
        print(f"Viga laadimisel: {e}")
