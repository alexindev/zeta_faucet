import requests
from loguru import logger
from time import sleep


def main(info: str, evm: str):

    address = info.split(':')[0]
    token = info.split(':')[1]

    headers = {
        'authorization': f'{token}'
    }

    payload = {
        'content': f'zeta faucet drip {address} {evm}',
        'tts': False
    }

    try:
        r = requests.post(
            f'https://discord.com/api/v9/channels/922357353423175680/messages',
            headers=headers,
            json=payload
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

    chain = None

    while True:
        chain = int(input('Chain: 1 - bcs, 2 - mumbai, 3 - goerli\n>>> '))
        if chain == 1:
            chain = 'bsc'

            break
        elif chain == 2:
            chain = 'mumbai'
            break
        elif chain == 3:
            chain = 'goerly'
            break
        else:
            print('Select (1, 2, 3)')

    for i in data:
        main(i, chain)
        sleep(1)
