import time
from log.nosqlog import logger as nosqlog


extra = {
    'usuario': 'usuario nosql',
    'clinica': 'clinica nosql'
    }


def run_nosql(number):
    start_nosql = time.time()
    for stress in range(number):
        # NoSQL
        nosqlog.info(
            'Sample NoSQL: Testando o log NoSQL #Info',
            extra=extra
            ) # debug
        nosqlog.debug(
            'Sample NoSQL: Testando o log NoSQL #Debug',
            extra=extra
            )  # debug
        nosqlog.warn(
            'Sample NoSQL: Testando o log NoSQL #Warn', 
            extra=extra
            )
        nosqlog.error(
            'Sample NoSQL: Testando o log NoSQL #Error',
            extra=extra
            )
        nosqlog.critical(
            'Sample NoSQL: Testando o log NoSQL #Critical',
            extra=extra
            )
        nosqlog.fatal(
            'Sample NoSQL: Testando o log NoSQL #Fatal',
            extra=extra
            )
        nosqlog.exception(
            'Sample NoSQL: Testando o log NoSQL #Exception',
            extra=extra
            )
    time_nosql = time.time() - start_nosql
    print(f"Resultado dos logs salvos em um banco não relacional: {time_nosql} segundos")




if __name__ == '__main__':
    run_nosql(1000)
