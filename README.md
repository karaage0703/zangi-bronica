# zangi-bronica
Digital Bag system for ZENZA BRONICA by using Raspberry Pi

# Dependency
- Python3 and Python2(Python3 is recommended)
- picamera
- pygame
- pigpio

# Setup

## Clone
```sh
$ cd && git clone https://github.com/karaage0703/zangi-bronica
```

## Auto Boot
Execute following commands for auto boot of zangi-bronica:
```sh
$ sudo cp ~/zangi-bronica/service/*.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable pigpio.service
$ sudo systemctl enable zangi.service
```

If you want to stop auto boot, execute following commands:

```sh
$ sudo systemctl disable pigpio.service
$ sudo systemctl disable zangi.service
```

# Usage
Execute following commands for manual booting zangi-bronica:
```sh
$ sudo pigpiod
$ cd ~/zangi-bronica
$ python3 zangi.py
```

# License
This software is released under the MIT License, see LICENSE.

# Authors
karaage0703

# References
