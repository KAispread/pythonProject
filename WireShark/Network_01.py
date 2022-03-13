import dpkt
import socket

with open('imgtest1.pcap', 'rb') as f:
    pcap = dpkt.pcap.Reader(f)
    var = 110
    dic = {}

    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        var = var - 1

        if var == 0:
            break
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue
        if ip.p != dpkt.ip.IP_PROTO_TCP:
            continue
        print('Timestamp: ', timestamp)
        print('IP: %s -> %s len=%d' % (socket.inet_ntoa(ip.src), socket.inet_ntoa(ip.dst), ip.len))
        print('Port : %d -> %d ack=%d seq=%d' % (tcp.sport, tcp.dport, tcp.ack, tcp.seq))
        print('Payload: ', str(tcp.data))

        streamIndex = socket.inet_ntoa(ip.src) + str(tcp.sport) + socket.inet_ntoa(ip.dst) + str(tcp.dport) + str(tcp.ack)
        print('StreamIndex: ', streamIndex)

        if streamIndex in dic:
            streamIndexValue = dic[streamIndex]
            streamIndexValue += ':' + str(tcp.seq) + ',' + str(tcp.data)
            del dic[streamIndex]
            dic[streamIndex] = streamIndexValue
        else:
            dic[streamIndex] = str(tcp.seq) + ',' + str(tcp.data)
