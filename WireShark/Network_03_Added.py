import dpkt
import socket

with open('imgtest1.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    dic = {}

    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue
        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue
        if socket.inet_ntoa(ip.src) != '101.79.241.17' or socket.inet_ntoa(ip.dst) != '203.232.131.77':
            continue

        tcp = ip.data

        if len(str(tcp.data.hex())) < 10:
            continue

        #print('Timestamp: ', timestamp)
        #print('IP: %s -> %s len=%d' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len))
        #print('Port : %d -> %d ack=%d seq=%d' % (tcp.sport, tcp.dport, tcp.ack, tcp.seq))
        #print('Payload: ', str(tcp.data))
        streamIndex = socket.inet_ntoa(ip.src) + ':' + str(tcp.sport) + ':'
        streamIndex += socket.inet_ntoa(ip.dst) + ':' + str(tcp.dport) + ':' + str(tcp.ack)
        #print('StreamIndex: %s, Payload: %s' % (streamIndex, str(tcp.data)))

        if streamIndex in dic:
            streamIndexValue = dic[streamIndex]
            streamIndexValue += '放送' + str(tcp.seq) + '新聞' + str(tcp.data.hex())
            del dic[streamIndex]
            dic[streamIndex] = streamIndexValue
            print(str(tcp.seq) + '新聞' + str(tcp.data.hex()))
        else:
            dic[streamIndex] = str(tcp.seq) + '新聞' + str(tcp.data.hex())
            print(str(tcp.seq) + '新聞' + str(tcp.data.hex()))

    ####### src : 101.79.241.17    dst : 203.232.131.77
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

        result1 = allpacket.find('ffd8ffe0')
        result2 = allpacket.find('ffd9')

        imgString = ''
        if result1 > -1 and result2 > -1:
            imgString = allpacket[result1:result2+4]
            print(imgString)