import pika, sys, os
import numpy as np
# Const variables
G = 9.807
ACC_RANGE = 8.0
RAW_SCALLING = 32768.0
accScale = G / (RAW_SCALLING / ACC_RANGE)
PI = 3.14159
D2R = PI / 180.0
gyroScale = 1000.0 / RAW_SCALLING * D2R
magScale = 4912.0 / RAW_SCALLING
TEMP_OFFSET = 21
TEMP_SCALE = 333.87


def main():
    credentials = pika.PlainCredentials("admin", "admin")
    host = '192.168.1.158'
    parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()


    def callback(ch, method, properties, data):
         ###### IMU ########

        acc_x = np.frombuffer(data[23:25], dtype=np.uint16) * accScale
        acc_y = np.frombuffer(data[25:27], dtype=np.uint16) * accScale
        acc_z = np.frombuffer(data[27:29], dtype=np.uint16) * accScale
        gyro_x = np.frombuffer(data[29:31], dtype=np.uint16) * gyroScale
        gyro_y = np.frombuffer(data[31:33], dtype=np.uint16) * gyroScale
        gyro_z = np.frombuffer(data[33:35], dtype=np.uint16) * gyroScale
        temp =  ( ( np.frombuffer(data[35:37], dtype=np.uint16) - TEMP_OFFSET ) / TEMP_SCALE ) + TEMP_OFFSET
        mag_x = np.frombuffer(data[37:39], dtype=np.uint16) * magScale
        mag_y = np.frombuffer(data[39:41], dtype=np.uint16) * magScale
        mag_z = np.frombuffer(data[41:43], dtype=np.uint16) * magScale

        ###### SOLE ########
        # channel.queue_declare(queue='sole')

        hallux = np.frombuffer(data[7:9], dtype=np.uint16)
        toes = np.frombuffer(data[9:11], dtype=np.uint16)
        met1 = np.frombuffer(data[11:13], dtype=np.uint16)
        met3 = np.frombuffer(data[13:15], dtype=np.uint16)
        met5 = np.frombuffer(data[15:17], dtype=np.uint16)
        arch = np.frombuffer(data[17:19], dtype=np.uint16)
        heelL = np.frombuffer(data[19:21], dtype=np.uint16)
        heelR = np.frombuffer(data[21:23], dtype=np.uint16)
        print("Hallux: ", hallux)
        print("Toes: ", toes)
        print("Met 1: ", met1)
        print("Met 3: ", met3)
        print("Met 5: ", met5)
        print("arch: ", arch)
        print("Heel L: ", heelL)
        print("Heel R: ", heelR)
        
    channel.basic_consume(queue='packet4_left', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)