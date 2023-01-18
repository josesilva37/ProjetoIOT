import pika, sys, os
import numpy as np
import pandas as pd

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

    def callbackHeader(ch, method, properties, data):
        battery = np.frombuffer(data[16])
        side = np.frombuffer(data[17])
    def callbackPacket(ch, method, properties, data):
        df = pd.read_csv('./Dashboard/dataset.csv', sep=',')
         ###### IMU ########
        df.set_index('index', inplace=True)
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
        
        df.loc[len(df)+1] =[acc_x, acc_y, acc_z,gyro_x, gyro_y, gyro_z, mag_x, mag_y, mag_z, hallux, toes, met1, met3, met5, arch, heelL, heelR]
        print(df)
        df.to_csv('./Dashboard/dataset.csv')
        

        
    channel.basic_consume(queue='packet4_right', on_message_callback=callbackPacket, auto_ack=True)
    # channel.basic_consume(queue='header_left', on_message_callback=callbackHeader, auto_ack=True)
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