from port_scanner import port_scanning
from banner_grabber import banner_grabbing

def main():
    # hardcoded for now
    target_ip = "127.0.0.1"
    start_port = 9990
    end_port = 9999

    # port scanning
    open_ports = port_scanning(target_ip, start_port, end_port)
    print(f"Found {len(open_ports)} open ports")

    # banner grabbing
    result = []
    for port in open_ports:
        banner = banner_grabbing(target_ip, port)
        result.append({"port" : port, "banner" : banner}) # dict for key-value pair
        print(f"{port}: {banner}")

if __name__ == "__main__":
    main()


