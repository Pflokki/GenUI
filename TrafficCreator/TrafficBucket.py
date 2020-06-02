from .ProtocolHandlers.TcpProtocol import TCPProtocol
from .ProtocolHandlers.IPProtocol import IPProtocol
from .ProtocolHandlers.TelnetProtocol import TelnetProtocol
from .ProtocolHandlers.Pop3Protocol import POP3Protocol
from .ProtocolHandlers.UdpProtocol import UDPProtocol
from .ProtocolHandlers.DnsProtocol import DNSProtocol
from .ProtocolHandlers.IcmpProtocol import ICMPProtocol
from .ProtocolHandlers.DefaultProtocol import DefaultProtocol

import random

IP_PERCENTAGE_MIN, ATTACK_IP_PERCENTAGE_MIN = 0, 0
IP_PERCENTAGE_MAX, ATTACK_IP_PERCENTAGE_MAX = 5, 5

TELNET_PERCENTAGE_MIN, ATTACK_TELNET_PERCENTAGE_MIN = 0, 0
TELNET_PERCENTAGE_MAX, ATTACK_TELNET_PERCENTAGE_MAX = 5, 5

POP3_PERCENTAGE_MIN, ATTACK_POP3_PERCENTAGE_MIN = 0, 0
POP3_PERCENTAGE_MAX, ATTACK_POP3_PERCENTAGE_MAX = 5, 5

UDP_PERCENTAGE_MIN, ATTACK_UDP_PERCENTAGE_MIN = 0, 0
UDP_PERCENTAGE_MAX, ATTACK_UDP_PERCENTAGE_MAX = 5, 5

TCP_PERCENTAGE_MIN, ATTACK_TCP_PERCENTAGE_MIN = 0, 0
TCP_PERCENTAGE_MAX, ATTACK_TCP_PERCENTAGE_MAX = 5, 5

DNS_PERCENTAGE_MIN, ATTACK_DNS_PERCENTAGE_MIN = 0, 0
DNS_PERCENTAGE_MAX, ATTACK_DNS_PERCENTAGE_MAX = 5, 5

ICMP_PERCENTAGE_MIN, ATTACK_ICMP_PERCENTAGE_MIN = 0, 0
ICMP_PERCENTAGE_MAX, ATTACK_ICMP_PERCENTAGE_MAX = 5, 5


class TrafficBucket:
    def __init__(self):
        self.tcp_bucket = []

        self.ip_bucket = []
        self.telnet_bucket = []
        self.pop3_bucket = []
        self.udp_bucket = []
        self.dns_bucket = []
        self.icmp_bucket = []
        self.other_bucket = []

    @property
    def bucket_size(self):
        return len(self.ip_bucket) \
               + len(self.tcp_bucket) \
               + len(self.telnet_bucket) \
               + len(self.pop3_bucket) \
               + len(self.udp_bucket) \
               + len(self.dns_bucket) \
               + len(self.icmp_bucket) \
               + len(self.other_bucket)

    @property
    def ip_percentage(self):
        return len(self.ip_bucket) / self.bucket_size

    @property
    def tcp_percentage(self):
        return len(self.tcp_bucket) / self.bucket_size

    @property
    def telnet_percentage(self):
        return len(self.telnet_bucket) / self.bucket_size

    @property
    def pop3_percentage(self):
        return len(self.pop3_bucket) / self.bucket_size

    @property
    def udp_percentage(self):
        return len(self.udp_bucket) / self.bucket_size

    @property
    def dns_percentage(self):
        return len(self.dns_bucket) / self.bucket_size

    @property
    def icmp_percentage(self):
        return len(self.icmp_bucket) / self.bucket_size

    @property
    def other_percentage(self):
        return len(self.other_bucket) / self.bucket_size

    def generate_bucket(self, bucket_size=1000):
        ip_count = int(random.randint(IP_PERCENTAGE_MIN, IP_PERCENTAGE_MAX)
                       / 100 * bucket_size)
        tcp_count = int(random.randint(TCP_PERCENTAGE_MIN, TCP_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        telnet_count = int(random.randint(TELNET_PERCENTAGE_MIN, TELNET_PERCENTAGE_MAX)
                           / 100 * bucket_size)
        pop3_count = int(random.randint(POP3_PERCENTAGE_MIN, POP3_PERCENTAGE_MAX)
                         / 100 * bucket_size)
        udp_count = int(random.randint(UDP_PERCENTAGE_MIN, UDP_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        dns_count = int(random.randint(DNS_PERCENTAGE_MIN, DNS_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        icmp_count = int(random.randint(ICMP_PERCENTAGE_MIN, ICMP_PERCENTAGE_MAX)
                         / 100 * bucket_size)
        other_count = bucket_size - sum([ip_count, tcp_count, telnet_count, pop3_count,
                                         udp_count, dns_count, icmp_count])

        self.fill_bucket(ip_count, tcp_count, telnet_count, pop3_count,
                         udp_count, dns_count, icmp_count, other_count)

    def generate_attack_bucket(self, bucket_size=100000):
        ip_count = int(random.randint(ATTACK_IP_PERCENTAGE_MIN, ATTACK_IP_PERCENTAGE_MAX)
                       / 100 * bucket_size)
        tcp_count = int(random.randint(ATTACK_TCP_PERCENTAGE_MIN, ATTACK_TCP_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        telnet_count = int(random.randint(ATTACK_TELNET_PERCENTAGE_MIN, ATTACK_TELNET_PERCENTAGE_MAX)
                           / 100 * bucket_size)
        pop3_count = int(random.randint(ATTACK_POP3_PERCENTAGE_MIN, ATTACK_POP3_PERCENTAGE_MAX)
                         / 100 * bucket_size)
        udp_count = int(random.randint(ATTACK_UDP_PERCENTAGE_MIN, ATTACK_UDP_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        dns_count = int(random.randint(ATTACK_DNS_PERCENTAGE_MIN, ATTACK_DNS_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        icmp_count = int(random.randint(ATTACK_ICMP_PERCENTAGE_MIN, ATTACK_ICMP_PERCENTAGE_MAX)
                        / 100 * bucket_size)
        other_count = bucket_size - sum([ip_count, tcp_count, telnet_count, pop3_count,
                                         udp_count, dns_count, icmp_count])

        self.fill_bucket(ip_count, tcp_count, telnet_count, pop3_count,
                         udp_count, dns_count, icmp_count, other_count)

    def fill_bucket(self, ip_count, tcp_count, telnet_count, pop3_count,
                    udp_count, dns_count, icmp_count, other_count):
        for _ in range(ip_count):
            self.generate_ip()
        for _ in range(tcp_count):
            self.generate_tcp()
        for _ in range(telnet_count):
            self.generate_telnet()
        for _ in range(pop3_count):
            self.generate_pop3()
        for _ in range(udp_count):
            self.generate_udp()
        for _ in range(dns_count):
            self.generate_dns()
        for _ in range(icmp_count):
            self.generate_icmp()
        for _ in range(other_count):
            self.generate_other()

    def generate_ip(self):
        self.ip_bucket.append(IPProtocol())

    def generate_tcp(self):
        self.ip_bucket.append(TCPProtocol())

    def generate_telnet(self):
        self.ip_bucket.append(TelnetProtocol())

    def generate_pop3(self):
        self.ip_bucket.append(POP3Protocol())

    def generate_udp(self):
        self.ip_bucket.append(UDPProtocol())

    def generate_dns(self):
        self.ip_bucket.append(DNSProtocol())

    def generate_icmp(self):
        self.ip_bucket.append(ICMPProtocol())

    def generate_other(self):
        self.ip_bucket.append(DefaultProtocol())

