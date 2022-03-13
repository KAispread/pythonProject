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
