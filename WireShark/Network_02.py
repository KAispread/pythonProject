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

        tcp = ip.data

        if len(str(tcp.data)) <10:
            continue
        else:
            http = dpkt.http.Request(tcp.data)

        #print('Timestamp: ', timestamp)
        #print('IP: %s -> %s len=%d' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len))
        #print('Port : %d -> %d ack=%d seq=%d' % (tcp.sport, tcp.dport, tcp.ack, tcp.seq))
        #print('Payload: ', str(tcp.data))
        streamIndex = socket.inet_ntoa(ip.src) + ':' + str(tcp.sport) + ':'
        streamIndex += socket.inet_ntoa(ip.dst) + ':' + str(tcp.dport) + ':' + str(tcp.ack)
        #print('StreamIndex: %s, Payload: %s' % (streamIndex, str(tcp.data)))

        #streamIndex = socket.inet_ntoa(ip.src) + str(tcp.sport) + socket.inet_ntoa(ip.dst) + str(tcp.dport) + str(tcp.ack)

        if streamIndex in dic:
            streamIndexValue = dic[streamIndex]
            streamIndexValue += '放送' + str(tcp.seq) + '新聞' + str(http.data)
            del dic[streamIndex]
            dic[streamIndex] = streamIndexValue
        else:
            dic[streamIndex] = str(tcp.seq) + '新聞' + str(http.data)

    ####### src : 101.79.241.17    dst : 203.232.131.77
    for key in dic:
        streamValue1 = dic[key]
        arr1 = streamValue1.split('放送')

        if len(arr1) >= 10:
            strSeq = []
            strData = []
            for val in arr1:
                arr2 = val.split('新聞')
                #print('Size: ', str(len(arr2)))
                strSeq.append(arr2[0])
                strData.append(arr2[1])

            for i in range(len(strSeq)):
                for j in range(len(strSeq) - 1):
                    sseq = int(strSeq[j])
                    sdata = strData[j]
                    if int(strSeq[j]) > int(strSeq[j + 1]):
                        strSeq[i] = strSeq[j + 1]
                        strSeq[j + 1] = str(sseq)
                        strData[i] = strData[j + 1]
                        strData[j + 1] = sdata

            with open('test\\' + key.replace(':','.') + '.txt', 'w') as file:
                file.write(key + '\n')
                for content in strData:
                    file.write(content + '\n')




