import dpkt
import socket
import binascii


def in_binary_literal(hex_code):
    try:
        bin_code = binascii.unhexlify(hex_code)  # unhexlify()로 hex값을 바이트 리터럴로 변환
    except binascii.Error:  # 문자열이 홀수 길이일 경우 오류 발생하므로 예외 처리
        hex_even_code = hex_code + '0'
        bin_code = binascii.unhexlify(hex_even_code)

    return bin_code

    # binascii.hexlify(hex_code)
    # encode => 코드화 / decode => 원래 형태로 복호화


with open('ForTest02.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    dic = {}

    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue
        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue

        tcp = ip.data

        streamIndex = socket.inet_ntoa(ip.src) + ':' + str(tcp.sport) + ':'
        streamIndex += socket.inet_ntoa(ip.dst) + ':' + str(tcp.dport) + ':' + str(tcp.ack)

        if streamIndex in dic:
            streamIndexValue = dic[streamIndex]
            streamIndexValue += '放送' + str(tcp.seq) + '新聞' + str(tcp.data.hex())
            del dic[streamIndex]
            dic[streamIndex] = streamIndexValue
        else:
            dic[streamIndex] = str(tcp.seq) + '新聞' + str(tcp.data.hex())

    for key in dic:
        streamValue1 = dic[key]
        arr1 = streamValue1.split('放送')

        strSeq = []
        strData = []
        for val in arr1:
            arr2 = val.split('新聞')
            strSeq.append(arr2[0])
            strData.append(arr2[1])

        for i in range(len(strSeq)):
            for j in range(len(strSeq) - 1):
                sseq = int(strSeq[j + 1])
                sdata = strData[j + 1]
                if int(strSeq[j]) > int(strSeq[j + 1]):
                    del strSeq[j + 1]
                    strSeq.insert(j, sseq)
                    del strData[j + 1]
                    strData.insert(j, sdata)

        allpacket = ''
        for packet in strData:
            allpacket += packet

        result1 = allpacket.find('ffd8ff')
        result2 = allpacket.find('ffd9')

        imgString = ''

        if result1 > -1 and result2 > -1:
            imgString = allpacket[result1:result2 + 4]
            BinaryImg = in_binary_literal(imgString)  # 추출된 JPEG 16진수 값을 바이트 리터럴로 저장.
            with open('sourceImg' + '(' + key.replace(":", ".") + ').jpeg', 'wb') as file:
                file.write(BinaryImg)
