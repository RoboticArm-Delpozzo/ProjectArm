import threading
import time
from random import randint
from faceDetection import *
from motorRotation import rotate
# Definizione del lock
threadLock = threading.Lock()
class MyThread (threading.Thread):
   def __init__(self, threadNumber):
      threading.Thread.__init__(self)
      self.threadNumber = threadNumber
      
   def run(self):
      print ("Thread '" + str(self.threadNumber) + "' started")
      # Acquisizione del lock
      #threadLock.acquire()
      if self.threadNumber == 0:
          faceDetection()
      elif self.threadNumber == 1:
          #rotate()
          pass
      print ("Thread '" + str(self.threadNumber) + "' ended")
      # Rilascio del lock
      #threadLock.release()
      
def main():
    # Creazione dei thread
    thread1 = MyThread(0)
    thread2 = MyThread(1)
    # Avvio dei thread
    thread1.start()
    thread2.start()

    # Join
    thread1.join()
    thread2.join()

    # Fine dello script
    print("end")

if __name__ == "__main__":
    main()
