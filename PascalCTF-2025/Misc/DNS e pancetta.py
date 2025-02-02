import pyshark

cap = pyshark.FileCapture('pancetta.pcapng', display_filter='udp')


for packet in cap:
    if hasattr(packet.dns, "qry_name"):
        domain = packet.dns.qry_name
        hex_part = domain.split(".attacker.com")[0]  # Prendi solo la parte esadecimale

        try:
            decoded_text = bytes.fromhex(hex_part).decode("utf-8")
            print(decoded_text)  # Stampa solo la decodifica
        except ValueError:
            continue  # Se non è un valore esadecimale valido, ignora
