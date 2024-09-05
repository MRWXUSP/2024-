import serial
import time

from . import DataDown as trans
from . import GUI_Back as GUI

class Communication:
    Port= 'string'
    Baudrate=None
    ser=None
    def __init__(self):
        self.Port='COM3'
        self.Baudrate=9600
        self.ser=None

    def open_port(self, port, baudrate):
        self.Port=port
        self.Baudrate=baudrate
        try:
            # 打开串口
            self.ser = serial.Serial(self.Port, self.Baudrate, timeout=1)
            print(f"Connected to {self.Port} at {self.Baudrate} baud.")
            time.sleep(2)
            return 'OPEN'
        except serial.SerialException as e:
            print(f"Serial exception: {e}")
            return 'CLOSE'

    def close_port(self):
        if self.ser and self.ser.is_open:
            try:
                self.ser.close()
                print("Serial port closed.")
                return 'CLOSE'
            except Exception as e:
                print(f"Failed to close serial port: {e}")
                return 'OPEN'
        else:
            print("Serial port is not open.")
            return 'CLOSE'

    def send_data_to_microcontroller(self,type=0,data=None):
        #发送指令到单片机
        #回传是否失败
        #type 0:读取所有 1:更改时间 2:清空时间 3:添加代办 4:删除代办 5:更改代办
        command=[[0xA1, 0xAF], [0xB1, 0xBF], [0xC1, 0xCF], [0xD1, 0xDF], [0xE1, 0xEF], [0xF1, 0xFF]]
        empty=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]#12字节
        if self.ser is None:
            print("Serial port is not initialized.")
            return False
        if not self.ser.is_open:
            print("Serial port is not open.")
            return False
        
        if data==None:
            send_data=bytearray(command[type])+bytearray(empty)
            print(send_data)
        else:
            send_data=bytearray(command[type])+bytearray(data)
            while True:
                if len(send_data)<14:
                    send_data.append(0x00)
                else:
                    break

        try:
            self.ser.write(send_data)
            print(f"Sent: {send_data}")
            #self.ser.write(send_data)
            #print("Sent: f'{send_data}'")
            return True
        except Exception as e:
            print(f"Failed to send data: {e}")
            return False

    def receive_data_from_microcontroller(self,type=0):
        #接收单片机数据
        receive_list = [
    [[0xBF, 0xB1], [0xBB, 0xBB]],
    [[0xCF, 0xC1], [0xCC, 0xCC]],
    [[0xDF, 0xD1], [0xDD, 0xDD]],
    [[0xEF, 0xE1], [0xEE, 0xEE]],
    [[0xFF, 0xF1], [0xFF, 0xFF]]
                        ]
        if type==0:
            try:
                buffer = bytearray()
                hex_list=[]
                flag=True
                # data=False
                # while not data:
                #     data=self.ser.read(1)
                #     print(data)
                
                while flag:
                    #time.sleep(2)
                    # 每次读取1个字节
                    print("start receiving\n")
                    data = self.ser.read(1)
                    print(f"Received: {data}")
                    if data and data == b'\xAF':
                        print("received 0xAF beginning\n")
                        continue
                    elif data and data == b'\xA1':
                        print("received 0xA1\n")
                        continue
                    elif data and data == b'\xFF':
                        print("received 0xFF end\n")
                        flag=False
                        buffer.clear()#清空缓冲区
                        return hex_list
                    elif data:
                        buffer.extend(data)
                        # 将字节数据逐字节转换为16进制表示
                        print_data = ' '.join(f'{byte:02X}' for byte in data)
                        hex_data = f'{data[0]:02X}'
                        hex_list.append(hex_data)
                        print(f"Received (hex): {print_data}")    
            
            except Exception as e:
                print(f"Failed to receive data: {e}")
            
            except serial.SerialException as e:
                print(f"Serial exception: {e}")
            
            except KeyboardInterrupt:
                print("Exiting program.")
                exit(1)
        else:
            while True:
                # 每次读取2个字节
                data = self.ser.read(2)
                if data and data == bytes(receive_list[type-1][0]):
                    print(f"received {receive_list[type-1][0]} \n")
                    return 'TRUE'
                elif data and data == bytes(receive_list[type-1][1]):
                    print(f"received {receive_list[type-1][1]} \n")
                    return "FALSE" 
                
    def string_to_hex(self,text):
        try:
            number = int(text,16)
            # hex_str = hex(number)
            # return hex_str
            return number
        except ValueError:
            # 如果转换失败，返回一个错误信息或处理方式
            return "Invalid input"
        
    def read_all(self):
        # self.close_port()
        # self.open_port(self.Port, self.Baudrate)
        self.send_data_to_microcontroller()
        hex_list_all=self.receive_data_from_microcontroller()
        print(hex_list_all)
        i=0
        j=0
        k=0
        DataList=[]
        while True:
            if i+12<=len(hex_list_all):
                hex_list=hex_list_all[i:i+12]
                i+=12
            else:
                return DataList
            TempName=hex_list[0:5]
            HumanName=[0,0,0,0,0]
            for k in range(0,5):
                HumanName[k]=int(TempName[k],16)
            print(HumanName)
            HumanName=trans.DataToChar(HumanName)
            HumanName=trans.HtoChar(HumanName)
            print(HumanName)
            time=hex_list[5:11]
            Time='-'.join(time)
            print(Time)
            DataList.append(GUI.DataType())
            DataList[j].Name=HumanName
            DataList[j].Time=Time
            DataList[j].Ptr=hex_list[11]
            j+=1

    def time_set(self, set_list):
        #设置时间
        data=[]
        for i in range(0,6):
            data.append(self.string_to_hex(set_list[i]))
        self.send_data_to_microcontroller(1,data)
        if  self.receive_data_from_microcontroller(1):
            print("Set time successfully")
            return "TRUE"
        else:
            print("Set time failed")
            return "FALSE"

    def time_clear(self):
        self.send_data_to_microcontroller(2)
        if  self.receive_data_from_microcontroller(2):
            print("Set time successfully")
            return "TRUE"
        else:
            print("Set time failed")
            return "FALSE"
    
    def add_data(self, data):
        #添加代办
        data.ConvertData(0)
        self.send_data_to_microcontroller(3,data.merge)
        return self.receive_data_from_microcontroller(3)
    
    def delete_data(self, data):
        #删除代办
        self.send_data_to_microcontroller(4,bytes.fromhex(data.Ptr))
        return self.receive_data_from_microcontroller(4)
    
    def change_data(self, data):
        #更改代办
        data.ConvertData(1)
        self.send_data_to_microcontroller(5,data.merge)
        return self.receive_data_from_microcontroller(5)


#finally:
#    if ser.is_open:
#        ser.close()
#        print("Serial port closed.")


      
#        finally:
#            if ser.is_open:
#                ser.close()
#                print("Serial port closed.")

#if __name__ == "__main__":
#    main()