from log.sqlog import logger as sqlog


extra = {
    'usuario': 'usuario doos',
    'clinica': 'clinica doos'
}

for stress in range(1000):
    # SQL
    sqlog.info(
        'Sample Two: Testando o log SQL #Info',
        extra={'extra': extra}
    )  # debug
    sqlog.debug(
        'Sample Two: Testando o log SQL #Debug',
        extra={'extra': extra}
    )  # debug
    sqlog.warn(
        'Sample Two: Testando o log SQL #Warn',
        extra={'extra': extra}
    )
    sqlog.error(
        'Sample Two: Testando o log SQL #Error',
        extra={'extra': extra}
    )
    sqlog.critical(
        'Sample Two: Testando o log SQL #Critical',
        extra={'extra': extra}
    )
    sqlog.fatal(
        'Sample Two: Testando o log SQL #Fatal',
        extra={'extra': extra}
    )
    # sqlog.exception(
    #     'Sample Two: Testando o log SQL #Exception',
    #     extra={'extra': extra}
    # )
