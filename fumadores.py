import random
import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaforoAgente = threading.Semaphore(0)
semaforoFumadorConPapel = threading.Semaphore(0)
semaforoFumadorConTabaco = threading.Semaphore(0)
semaforoFumadorConFosforos = threading.Semaphore(0)

def agente():
    while True:
        caso = random.choice([0,1,2]) #al azar pone dos cosas en la mesa
        if caso == 0:
            logging.info('Pongo tabaco y fosforos sobre la mesa')
            time.sleep(2)
            semaforoFumadorConPapel.release()
        if caso == 1:
            logging.info('Pongo papel y fosforos sobre la mesa')
            time.sleep(2)
            semaforoFumadorConTabaco.release()
        if caso == 2:
            logging.info('Pongo papel y tabaco sobre la mesa')
            time.sleep(2)
            semaforoFumadorConFosforos.release()
        semaforoAgente.acquire()
        # esperar a reponer las cosas una vez que alguien haya tomado las dos anteriores

def fumadorConPapel():
    while True:
        semaforoFumadorConPapel.acquire()
        logging.info('Armo cigarrillo')
        time.sleep(1)
        logging.info('Fumo cigarrillo')
        time.sleep(1)
        semaforoAgente.release()

def fumadorConTabaco():
    while True:
        semaforoFumadorConTabaco.acquire()
        logging.info('Armo cigarrillo')
        time.sleep(1)
        logging.info('Fumo cigarrillo')
        time.sleep(1)
        semaforoAgente.release()

def fumadorConFosforos():
    while True:
        semaforoFumadorConFosforos.acquire()
        logging.info('Armo cigarrillo')
        time.sleep(1)
        logging.info('Fumo cigarrillo')
        time.sleep(1)
        semaforoAgente.release()


agenteHilo = threading.Thread(target=agente)
fumadorConPapelHilo = threading.Thread(target=fumadorConPapel)
fumadorConTabacoHilo = threading.Thread(target=fumadorConTabaco)
fumadorConFosforosHilo = threading.Thread(target=fumadorConFosforos)

agenteHilo.start()
fumadorConPapelHilo.start()
fumadorConFosforosHilo.start()
fumadorConTabacoHilo.start()

