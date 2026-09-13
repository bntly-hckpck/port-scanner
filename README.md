# recon-kit

Minimal personal cybersecurity toolkit to explore the fundamentals of TCP reconnaissance.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## Features

- [X] Parallel test servers for local testing
- [X] Single port connectivity check
- [X] Port range scanning
- [X] Banner grabbing from open ports
- [ ] JSON report
- [ ] main.py
- [ ] *TBD*

## Overview

| module | purpose |
|--------|---------|
| [`port_scanner.py`](port_scanner.py) | scan TCP port ranges, return list of open ports |
| [`banner_grabber.py`](banner_grabber.py) | connect to open ports and retrieve service banners |
| [`test_servers.py`](test_servers.py) | parallel test servers for validation |
