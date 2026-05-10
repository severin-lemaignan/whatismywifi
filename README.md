# whatismywifi

A small Linux command-line tool that summarizes the Wi-Fi capabilities of the
local adapter and the characteristics of the currently active link, by parsing
the output of `iw phy` and `iw dev <iface> link / station dump`.

Inspired by [wiisfi.com](https://www.wiisfi.com/) — it doesn't just dump the
numbers, it explains what they *mean*.

## Requirements

- Linux
- Python 3.7+
- `iw` (from `iproute2` / `iw` package)

## Installation

```sh
pip install .
```

Or just run the script directly — it's a single file with no third-party
dependencies:

```sh
./whatismywifi
```

## Usage

```sh
whatismywifi                # auto-detect the wireless interface
whatismywifi -i wlan0       # specify an interface
whatismywifi --no-color     # disable ANSI colors
```

## License

Public Domain.

## Author

Claude (Opus 4.7).
