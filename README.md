# Rug-Pull-Scam-Token-Early-Warning-System

<div align="center">

<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Web3.py-6.0%2B-orange?style=for-the-badge&logo=ethereum&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Chains-ETH%20%7C%20BSC%20%7C%20Polygon%20%7C%20Arb-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Tests-pytest-yellow?style=for-the-badge&logo=pytest"/>

<br/>
<br/>

```
 ██████╗ ██╗   ██╗ ██████╗     ██████╗ ██╗   ██╗██╗     ██╗
 ██╔══██╗██║   ██║██╔════╝     ██╔══██╗██║   ██║██║     ██║
 ██████╔╝██║   ██║██║  ███╗    ██████╔╝██║   ██║██║     ██║
 ██╔══██╗██║   ██║██║   ██║    ██╔═══╝ ██║   ██║██║     ██║
 ██║  ██║╚██████╔╝╚██████╔╝    ██║     ╚██████╔╝███████╗███████╗
 ╚═╝  ╚═╝ ╚═════╝  ╚═════╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝
```

# RugPull Detector

### Smart Contract Risk Analyzer & Scam Token Early Warning System

**Protect your crypto investments from rug pulls, honeypots, and fraudulent token projects.**  
Open-source on-chain analysis + social signal intelligence — no middlemen, no subscriptions.

[📥 Download Latest Release](https://github.com/ClutchClimberJinx/didvlktr/releases) · [📖 Documentation](#documentation) · [🚀 Quick Start](#quick-start) · [🤝 Contributing](#contributing)

</div>

---

## 🛡️ What Is RugPull Detector?

**RugPull Detector** is an open-source Python tool for automated smart contract security analysis and social signal monitoring. It helps crypto investors, DeFi researchers, and security analysts identify high-risk token projects before they lose funds to rug pulls, honeypot contracts, and coordinated pump-and-dump schemes.

Unlike browser extensions or paid SaaS tools, RugPull Detector runs **entirely on your machine** — your wallet addresses and API keys never leave your system.

---

## ⚠️ Problem We Solve

Every day, hundreds of fraudulent crypto tokens are deployed across Ethereum, BNB Chain, Polygon, and Arbitrum. Common attack vectors include:

| Threat | Description |
|--------|-------------|
| **Rug Pull** | Developers drain liquidity after attracting investors |
| **Honeypot Contract** | Buy is possible, sell is blocked by code |
| **Mint Function Abuse** | Owner mints unlimited tokens to dilute holders |
| **Ownership Backdoor** | Hidden admin functions allow fund extraction |
| **Coordinated Pump** | Fake social media hype inflates price before dump |
| **Fake Liquidity Lock** | LP tokens appear locked but bypass is coded in |

**RugPull Detector flags all of these automatically.**

---

## ✅ Features

### 🔍 On-Chain Contract Analysis
- **Bytecode inspection** — scans for `SELFDESTRUCT`, dangerous 4-byte selectors, proxy patterns
- **Source code verification** — checks Etherscan/BSCScan for unverified contracts
- **Honeypot pattern detection** — regex analysis of Solidity source for sell-blocking code
- **Ownership status** — detects active owner vs renounced (burned to dead address)
- **Liquidity heuristics** — estimates contract liquidity from on-chain balance
- **Holder distribution** — flags top-heavy token supply concentration
- **Contract age** — warns on newly deployed contracts with low transaction history
- **EIP-1967 proxy detection** — identifies upgradeable contracts with hidden logic

### 📡 Social Signal Intelligence
- **Twitter/X analysis** — detects coordinated pump language, urgency tactics, bot-like activity
- **CoinGecko integration** — checks market cap rank, listing status, community trust signals
- **Telegram monitoring** — member velocity and transparency checks (bot token required)
- **Text pattern scoring** — standalone scorer for whitepaper/website copy analysis

### 📊 Risk Scoring Engine
- Weighted 0–100 risk score across 13 independent risk factors
- 4-tier risk levels: `LOW` / `MEDIUM` / `HIGH` / `CRITICAL`
- Combined contract (70%) + social (30%) weighting
- Actionable recommendation per analysis run

### 🖥️ Output Options
- Colorized terminal report with ASCII risk bar
- Machine-readable JSON output
- File export for CI/CD integration or batch processing
- Exit codes for scripting (`0` = low/medium, `1` = high, `2` = critical)

---

## 🚀 Quick Start

### Requirements
- Python 3.10+
- Access to an EVM RPC endpoint (free options available)
- Optional: Etherscan API key, Twitter Bearer token

### Installation

```bash
# Clone the repository
git clone https://github.com/ClutchClimberJinx/didvlktr.git
cd didvlktr

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Basic Usage

```bash
# Analyze a contract (minimum — just RPC, no API keys needed)
python -m src.main 0xContractAddressHere

# Full analysis with social signals
python -m src.main 0xContractAddressHere --token PEPE --etherscan-key YOUR_KEY

# Output as JSON
python -m src.main 0xContractAddressHere --output json

# Save report to file
python -m src.main 0xContractAddressHere --save report.json

# Analyze BNB Chain contract
python -m src.main 0xContractAddressHere --chain bsc --rpc https://bsc-dataseed.binance.org

# Skip social analysis (faster)
python -m src.main 0xContractAddressHere --no-social
```

### Example Terminal Output

```
 ────────────────────────────────────────────────────────────
  RISK ASSESSMENT REPORT  ·  2024-11-15T14:32:01Z
 ────────────────────────────────────────────────────────────

  💀  Overall Risk  CRITICAL  [████████████████░░░░]  82/100

  CONTRACT ANALYSIS  0x742d35Cc6634C0532925a3b8D4C9C3
  Score: 82/100   Level: CRITICAL

  Flags:
    ⚠  mint_function         → Dangerous function detected: mint(address,uint256)
    ⚠  honeypot_pattern      → Suspicious pattern: _isBlacklisted[
    ⚠  blacklist_function    → Address blacklisting mechanism found
    ⚠  ownership_not_renounced
    ⚠  no_source_code        → Contract source not verified on Etherscan

  Details:
    owner: 0x1a2b3c4d...
    contract_balance_eth: 0.021

 ────────────────────────────────────────────────────────────

  RECOMMENDATION:
  CRITICAL RISK — Multiple severe red flags detected.
  Do NOT interact with this contract. High probability of malicious intent.

 ────────────────────────────────────────────────────────────
```

---

## 📖 Documentation

### Risk Factors & Weights

| Risk Factor | Weight | Description |
|-------------|--------|-------------|
| `no_source_code` | +30 | Contract not verified on Etherscan |
| `self_destruct` | +25 | `SELFDESTRUCT` opcode in bytecode |
| `honeypot_pattern` | +25 | Sell-blocking code patterns found |
| `mint_function` | +20 | Unrestricted mint capability detected |
| `high_owner_supply` | +20 | Top holder owns >20% of supply |
| `no_liquidity_lock` | +20 | No LP token lock detected |
| `blacklist_function` | +20 | Address blacklisting in contract |
| `ownership_not_renounced` | +15 | Active owner with admin rights |
| `fee_manipulation` | +15 | Dynamic fee setter with high values |
| `low_liquidity` | +15 | Contract holds <0.5 ETH |
| `proxy_contract` | +10 | EIP-1967 upgradeable proxy detected |
| `young_contract` | +10 | Very new contract, <10 transactions |
| `few_holders` | +10 | Fewer than 50 unique token holders |

### Risk Levels

| Level | Score Range | Meaning |
|-------|-------------|---------|
| 🟢 `LOW` | 0–29 | No critical flags — standard due diligence applies |
| 🟡 `MEDIUM` | 30–59 | Some suspicious patterns — proceed with caution |
| 🔴 `HIGH` | 60–79 | Significant red flags — extreme caution required |
| 💀 `CRITICAL` | 80–100 | Multiple severe indicators — do not interact |

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `RPC_URL` | Yes | EVM JSON-RPC endpoint URL |
| `ETHERSCAN_API_KEY` | Recommended | Enables source code checks |
| `TWITTER_BEARER_TOKEN` | Optional | Enables Twitter/X social analysis |
| `BSCSCAN_API_KEY` | Optional | BNB Chain source verification |

### Supported Chains

| Chain | Flag | Default RPC |
|-------|------|-------------|
| Ethereum Mainnet | `--chain eth` | https://eth.llamarpc.com |
| BNB Smart Chain | `--chain bsc` | https://bsc-dataseed.binance.org |
| Polygon | `--chain polygon` | https://polygon-rpc.com |
| Arbitrum One | `--chain arb` | https://arb1.arbitrum.io/rpc |

---

## 🏗️ Project Structure

```
rugpull-detector/
├── src/
│   ├── main.py                    # CLI entry point
│   ├── analyzers/
│   │   └── contract_analyzer.py   # On-chain contract analysis engine
│   ├── collectors/
│   │   └── social_collector.py    # Twitter, Telegram, CoinGecko collector
│   └── utils/
│       └── report.py              # Report generator & terminal formatter
├── tests/
│   └── test_analyzer.py           # pytest unit tests
├── .env.example                   # Environment config template
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests

```bash
pip install pytest
pytest tests/ -v
```

---

## 🛣️ Roadmap

- [ ] **v1.1** — GoPlus Security API integration for cross-validated honeypot detection
- [ ] **v1.2** — DEX Screener LP lock verification (PinkSale, Unicrypt)
- [ ] **v1.3** — Batch analysis mode (CSV input of multiple contracts)
- [ ] **v1.4** — Telegram bot interface for real-time monitoring
- [ ] **v2.0** — Web dashboard with historical scan database
- [ ] **v2.1** — Webhook alerts for watched contracts / wallets

---

## 🤝 Contributing

Contributions are welcome. To add a new risk check:

1. Fork the repository
2. Add your check method to `ContractAnalyzer` or `SocialCollector`
3. Register the weight in `RISK_WEIGHTS`
4. Write a corresponding test in `tests/test_analyzer.py`
5. Submit a pull request with a clear description

Please keep all additions **defensive** — the goal is to protect users from fraud, not to enable it.

---

## ⚖️ Legal Disclaimer

RugPull Detector is provided for **educational and informational purposes only**. Analysis results are heuristic-based and do not constitute financial or legal advice. No tool can guarantee the detection of all fraudulent contracts. Always conduct independent research before making investment decisions. The authors accept no liability for losses incurred based on tool output.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">

**RugPull Detector** — Open-source smart contract security analysis  
Built by the community, for the community.

⭐ Star this repo if it helped you avoid a scam token ⭐

</div>
 406