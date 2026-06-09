from pywebio.input import input, input_group
from pywebio import start_server

import config


def main():
    data = input_group(
        label="Запит на поточну погоду",
        inputs=[
            input('Місто', name='city', required=True),
            input('Ваше і\'мя', name='name', required=True),
            input('EMAIL', name='email', required=True),
        ]
    )
    print(data)


start_server(
    main,
    host='0.0.0.0',
    port=8001,
    debug=config.DEBUG,
)
