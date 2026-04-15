# Stablecoin Peg Tracker
Built as an independent project focused on stablecoin monitoring and market structure.

Tracks real-time deviations from the $1 peg across major stablecoins (USDC, USDT, DAI) to surface market stress and pricing inefficiencies.

## Overview

Stablecoins are increasingly used as core settlement infrastructure in digital asset markets. Maintaining a stable peg is critical for liquidity, trust, and system stability.

This tool pulls live market data and computes peg deviations in real time, highlighting potential dislocations across assets.

## Features

- Real time price tracking via CoinGecko API  
- Peg deviation calculation relative to $1  
- Simple CLI output for quick monitoring  

## Tech Stack

- Python  
- requests (API calls)  

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/WBoutz/stablecoin-peg-tracker.git
cd stablecoin-peg-tracker

```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python peg_tracker.py
```

## Example Output

```
USDC | Price: $0.9987 | 24h: -0.13% | Deviation: -0.13% | Status: Stable
USDT | Price: $1.0012 | 24h: +0.12% | Deviation: +0.12% | Status: Stable
DAI  | Price: $0.9995 | 24h: -0.05% | Deviation: -0.05% | Status: Stable
```
