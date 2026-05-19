# Clone the repository
git clone https://github.com/ClutchClimberJinx/didvlktr.git
cd didvlktr

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Edit .env with your API keys
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