import time
from log.sqlog import logger as sqlog


extra = {
    'usuario': 'usuario sql',
    'clinica': 'clinica sql'
}


def run_sql(number):
    start_sql = time.time()
    for stress in range(1000):
        # SQL
        sqlog.info(
            'Sample SQL: Testando o log SQL #Info',
            extra={'extra': extra}
        )  # debug
        sqlog.debug(
            'Sample SQL: Testando o log SQL #Debug',
            extra={'extra': extra}
        )  # debug
        sqlog.warn(
            'Sample SQL: Testando o log SQL #Warn',
            extra={'extra': extra}
        )
        sqlog.error(
            'Sample SQL: Testando o log SQL #Error',
            extra={'extra': extra}
        )
        sqlog.critical(
            'Sample SQL: Testando o log SQL #Critical',
            extra={'extra': extra}
        )
        sqlog.fatal(
            'Sample SQL: Testando o log SQL #Fatal',
            extra={'extra': extra}
        )
        # sqlog.exception(
        #     'Sample SQL: Testando o log SQL #Exception',
        #     extra={'extra': extra}
        # )
    time_sql = time.time() - start_sql
    print(f"Resultado dos logs salvos em um banco relacional: {time_sql} segundos")


if __name__ == '__main__':
    run_sql(1000)
