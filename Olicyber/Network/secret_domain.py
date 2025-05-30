import pyshark

cap = pyshark.FileCapture('capture.pcap', display_filter='dns')

for packet in cap:
    if hasattr(packet.dns, "qry_name"):
        domain = packet.dns.qry_name
        if domain == 'mores3cret.ctf': 
            print(packet)  # Print the full packet content
