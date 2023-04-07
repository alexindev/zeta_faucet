import requests
from loguru import logger
from time import sleep
from random import randint


def tor_proxy():
    proxy_auth = str(randint(1, 0x7fffffff)) + ':' + str(randint(1, 0x7fffffff))
    return {
        'http': f'socks5://{proxy_auth}@localhost:9150',
        'https': f'socks5://{proxy_auth}@localhost:9150'
    }


def main(info: str):

    proxy = None
    if proxys == 'y' or 'Y':
        proxy = tor_proxy()

    address = info.split(':')[0]
    token = info.split(':')[1]

    headers = {
        'authorization': f'{token}'
    }

    payload = {
        'content': f'zeta faucet drip {address}',
        'tts': False
    }

    try:
        r = requests.post(
            f'https://discord.com/api/v9/channels/922357353423175680/messages',
            headers=headers,
            json=payload,
            proxies=proxy
        ).json()

        if r.get('id') is None:
            logger.error(f'Fail send message for: {address}')
        else:
            logger.success(f'Success send message for: {address}')
    except Exception as e:
        logger.error(f'{address} some error {e}')

if __name__ == '__main__':
    with open('data.txt') as file:
        data = [row.strip() for row in file]

    proxys = input('Tor proxy (y, n): ')

    for i in data:
        main(i)
        sleep(1)
