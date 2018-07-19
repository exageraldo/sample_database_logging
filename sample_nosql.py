from log.nosqlog import logger as nosqlog


extra = {
    'usuario': 'usuario um',
    'clinica': 'clinica um'
    }

for stress in range(1000):
    # NoSQL
    nosqlog.info(
        'Sample One: Testando o log NoSQL #Info',
        extra=extra
        ) # debug
    nosqlog.debug(
        'Sample One: Testando o log NoSQL #Debug',
        extra=extra
        )  # debug
    nosqlog.warn(
        'Sample One: Testando o log NoSQL #Warn', 
        extra=extra
        )
    nosqlog.error(
        'Sample One: Testando o log NoSQL #Error',
        extra=extra
        )
    nosqlog.critical(
        'Sample One: Testando o log NoSQL #Critical',
        extra=extra
        )
    nosqlog.fatal(
        'Sample One: Testando o log NoSQL #Fatal',
        extra=extra
        )
    nosqlog.exception(
        'Sample One: Testando o log NoSQL #Exception',
        extra=extra
        )
