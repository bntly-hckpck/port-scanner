import json

def report_writing(data, filename="recon_report.json"):

    with open (filename, "w") as file:
        json.dump(data, file, indent=3)

    print(f"report written to {filename}")

