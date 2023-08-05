import re


def is_valid_ipv4(ip):
    # Регулярное выражение для проверки на валидность IPv4-адреса
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, ip) is not None


def parse_ipv4(ip):
    if not is_valid_ipv4(ip):
        raise ValueError("Неверный формат IPv4-адреса")

    # Разбиваем IPv4-адрес на октеты и преобразуем их в целые числа
    octets = ip.split('.')
    parsed_octets = [int(octet) for octet in octets]

    return parsed_octets


def ips_between(ip1, ip2):
    # Парсим IPv4-адреса и получаем их октеты
    octets1 = parse_ipv4(ip1)
    octets2 = parse_ipv4(ip2)

    # Вычисляем количество адресов между двумя IPv4-адресами
    address_count = 0
    for i in range(4):
        address_count = address_count * 256 + (octets2[i] - octets1[i])

    return address_count


# Пример использования
try:
    ip1 = "192.168.0.1"
    ip2 = "192.168.1.5"
    result = ips_between(ip1, ip2)
    print("Количество адресов между", ip1, "и", ip2, ":", result)
except ValueError as e:
    print("Ошибка:", e)
