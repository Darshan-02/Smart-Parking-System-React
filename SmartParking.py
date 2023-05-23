#In raspberry by code to send data from ultrasonic sensor to aws cloud.  
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#slot 1 pins
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN)

#slot 2 pins
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

#slot1 
def sl1():
    while True:
        print("distance measured in progress")
        
        print("waiting")
        time.sleep(0.2)
        GPIO.output(23,True)
        time.sleep(0.00001)
        GPIO.output(23,False)
        while GPIO.input(24)==0:
            start_time=time.time()
        while GPIO.input(24)==1:
            stop_time=time.time()
        elapsed_time=stop_time-start_time
        distance=elapsed_time*34300/2
        distance=round(distance,2)
        
        if(distance < 10):
            status = 'BUSY'
        else:
            status = 'FREE'
        
        time.sleep(0.5)
        
        return status
        
 #slot2       
def sl2():
    while True:
        print("distance measured in progress")
        
        print("waiting")
        time.sleep(0.2)
        GPIO.output(11,True)
        time.sleep(0.00001)
        GPIO.output(11,False)
        while GPIO.input(12)==0:
            start_time=time.time()
        while GPIO.input(12)==1:
            stop_time=time.time()
        elapsed_time=stop_time-start_time
        distance=elapsed_time*34300/2
        distance=round(distance,2)
       
        
        if(distance < 10):
            status = 'BUSY'
        else:
            status = 'FREE'
        
        time.sleep(0.5)
        return status
        
        
#cloud part
try:
    import os
    import sys
    import datetime
    import time
    import boto3
    print("All Modules Loaded ...... ")
except Exception as e:
    print("Error {}".format(e))


class MyDb(object):

    def __init__(self, Table_Name='parking'):
        self.Table_Name=Table_Name

        self.db = boto3.resource('dynamodb')
        self.table = self.db.Table(Table_Name)

        self.client = boto3.client('dynamodb')

    @property
    def get(self):
        response = self.table.get_item(
            Key={
                'slot_no':"1"
            }
        )

        return response

    def put(self, slot_no='' , status=''):
        self.table.put_item(
            Item={
                'slot_no':slot_no,
                'status':status
                
            }
        )


def main():
    while True:
        status = sl1()
        time.sleep(0.5)
        slot_no = 1
        print("Slot no: ",slot_no)
        print( "Status: ",status)
        obj = MyDb()
        obj.put(slot_no=str(slot_no), status=str(status))
        print("Uploaded Sample on Cloud slot no:{},status: {} ".format(slot_no, status))
        time.sleep(0.5)
            

        status = sl2()
        time.sleep(0.5)
        slot_no = 2
        print("Slot no: ",slot_no)
        print( "Status: ",status)
        obj = MyDb()
        obj.put(slot_no=str(slot_no), status=str(status))
            
        print("Uploaded Sample on Cloud slot no:{},status: {} ".format(slot_no, status))
        time.sleep(0.5)




if __name__ == "__main__":
    main()

    
