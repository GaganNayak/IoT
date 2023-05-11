
try:
    import os
    import sys
    import datetime
    import time
    import boto3
   # import Adafruit_DHT
    #import threading
    print("All Modules Loaded ...... ")
except Exception as e:
    print("Error {}".format(e))


class MyDb(object):

    def __init__(self, Table_Name='tester'):
        self.Table_Name=Table_Name

        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)

        self.client = boto3.client('dynamodb')

    @property
    def get(self):
        response = self.table.get_item(
            Key={
                'Battery_Id':"1"
            }
        )

        return response

    def put(self, Battery_Id='' , Battery_Voltage=''):
        self.table.put_item(
            Item={
                'Battery_Id':Battery_Id,
                'Battery_Voltage':Battery_Voltage,
                
            }
        )


    def describe_table(self):
        response = self.client.describe_table(
            TableName='Battery'
        )
        return response

    # @staticmethod
    # def sensor_value():

    #     pin = 23
    #     sensor = Adafruit_DHT.DHT11

    #     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    #     if humidity is not None and temperature is not None:
    #         print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    #     else:
    #         print('Failed to get reading. Try again!')
    #     return temperature, humidity

def main():
    global counter

    obj = MyDb()
    Battery_Id = 'AC-01-08'
    Battery_Voltage = 11.4
    obj.put(Battery_Id=str(Battery_Id), Battery_Voltage=str(Battery_Voltage))
    #counter = counter + 1
    print("Uploaded Sample on Cloud T:{},H{} ".format(Battery_Id, Battery_Voltage))


if __name__ == "__main__":
    main()



