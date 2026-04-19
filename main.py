import os


def main():
    service_name = os.getenv("SERVICE_NAME", "default")
    print(f"Hello world from {service_name}")


if __name__ == "__main__":
    main()
