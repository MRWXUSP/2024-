import sys

def CharToData(char):
	# name[8]每个字节有效位只有后五位
	# 取char0全位与char1前三位
    #8->5
    #传入num，传出bytes
    data=[0,0,0,0,0]
    data[0] = (char[0] << 3) + (char[1] >> 2)
	# 取char1剩余两位与char2全位与char3前一位
    data[1] = (char[1] << 6) + (char[2] << 1) + (char[3] >> 4)
	# 取char3剩余四位与char4前四位
    data[2] = (char[3] << 4) + (char[4] >> 1)
	# 取char4剩余一位与char5全位与char6前两位
    data[3] = (char[4] << 7) + (char[5] << 2) + (char[6] >> 3)
	# 取char6剩余三位与char7全位
    data[4] = (char[6] << 5) + char[7]
    return bytes(data)
    
def DataToChar(data):
	# name[i]最多五位
    # 取data[0]前五位
    char=[0,0,0,0,0,0,0,0]
    char[0] = data[0] >> 3
    # 取data[0]后三位与data[1]前二位
    char[1] = ((data[0] << 2) & 0x1C) + ((data[1] >> 6) & 0x03)
    # 取data[1]第3-7位
    char[2] = ((data[1] >> 1) & 0x1F)
    # 取data[1]最后一位与data[2]前四位
    char[3] = ((data[1] << 4) & 0x10) + ((data[2] >> 4) & 0x0F)
    # 取data[2]最后四位与data[3]前一位
    char[4] = ((data[2] << 1) & 0x1E) + ((data[3] >> 7) & 0x01)
    # 取data[3]第2-6位
    char[5] = ((data[3] >> 2) & 0x1F)
    # 取data[3]最后两位与data[4]前三位
    char[6] = ((data[3] << 3) & 0x18) + ((data[4] >> 5) & 0x07)
    # 取data[4]最后五位
    char[7] = data[4] & 0x1F
    return bytes(char)

#input byte
#output string
def HtoChar(hex_list):
    result = ''
    for hex_value in hex_list:
        if hex_value == 0x00:
            char = '_'
        else:
            # 将十六进制值转换为对应的字母
            char = chr(hex_value + ord('a') - 1)
        result += char
    return result
    