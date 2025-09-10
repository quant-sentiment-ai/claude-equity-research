# Claude Equity Research

Professional equity research and trading analysis powered by Claude AI, delivering institutional-grade investment insights with Goldman Sachs-style formatting and comprehensive risk assessment.

## What It Does

- **Institutional-Grade Analysis**: Generates professional equity research reports matching Wall Street standards
- **AI-Powered Intelligence**: Leverages Claude AI for comprehensive fundamental and technical analysis
- **Real-Time Data Integration**: Pulls live market data, earnings reports, and analyst coverage
- **Risk-Adjusted Recommendations**: Provides buy/sell/hold ratings with specific price targets and position sizing
- **Advanced Market Intelligence**: Includes options flow analysis, insider trading activity, and sector positioning

## Key Features

### Core Analysis Framework
- **Executive Summary**: Investment thesis with price target and 12-month timeframe
- **Fundamental Analysis**: Revenue growth, margins, peer comparisons, and forward estimates
- **Catalyst Analysis**: Near-term and medium-term market drivers with specific dates
- **Valuation Models**: Bull/base/bear scenarios with probability weighting
- **Risk Assessment**: Company-specific and macro risks with position sizing guidance (1-5%)
- **Technical Context**: Support/resistance levels, momentum indicators, and volume analysis

### Enhanced Intelligence Features
- **Options Flow Analysis**: Unusual activity, put/call ratios, implied volatility trends
- **Insider Activity Monitoring**: Executive buying/selling patterns with dollar amounts
- **Sector Positioning**: Rotation trends and relative strength vs market indices
- **ESG & Governance**: Sustainability scores and regulatory compliance assessment

### Professional Standards
- **Institutional Terminology**: EBITDA, P/E ratios, EV/Sales, conviction levels
- **Probability Weighting**: Bull/base/bear scenarios with percentage allocations
- **Legal Protection**: Comprehensive disclaimers for educational use
- **Data Sourcing**: Real-time web search with analyst firm citations

## Installation & Setup

### Prerequisites
- Claude Code CLI (latest version)
- Internet connection for real-time data retrieval
- Basic familiarity with equity research concepts

### Quick Start

1. **Install the /trading-ideas command** (system-wide):
```bash
mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md
```

2. **Basic usage**:
```bash
/trading-ideas AAPL
```

3. **Enhanced analysis**:
```bash
/trading-ideas HOOD --detailed
```

### Manual Setup

1. **Clone the repository**:
```bash
git clone https://github.com/quant-sentiment-ai/claude-equity-research.git
cd claude-equity-research
```

2. **Copy command to Claude Code**:
```bash
cp commands/trading-ideas.md ~/.claude/commands/
```

## Usage Examples

### Basic Equity Analysis
```bash
/trading-ideas AAPL
```
**Output**: Comprehensive institutional research report with BUY/SELL/HOLD recommendation

### Technology Sector Analysis
```bash
/trading-ideas NVDA
```
**Features**: AI/semiconductor sector positioning, relative valuation vs peers

### Financial Services Analysis
```bash
/trading-ideas JPM
```
**Includes**: Interest rate sensitivity, regulatory environment, book value analysis

### Growth Stock Analysis
```bash
/trading-ideas TSLA
```
**Focus**: Growth metrics, competitive positioning, volatility assessment

## Sample Output Format

```
# APPLE INC (AAPL) - ENHANCED EQUITY RESEARCH

## EXECUTIVE SUMMARY
BUY with $250 price target (9% upside) over 12 months. Strong Q4 2024 
results driven by iPhone 16 launch and AI integration provide foundation 
for premium product cycle. Balanced risk-reward with established ecosystem moat.

## FUNDAMENTAL ANALYSIS
Q4 2024: Revenue $94.9B (+6% YoY), EPS $1.64 (+12% YoY). iPhone revenue 
$46.2B (~49% of total), Services +12% to $25B with recurring characteristics.

## VALUATION & PRICE TARGETS
Consensus: $242 (range $200-$280)
Bull case: $280 | Base case: $250 | Bear case: $200
Probability weighting: 25%/55%/20%

## RECOMMENDATION: BUY | Conviction: High | Price Target: $250
```

## Command Reference

| Command | Description | Output |
|---------|-------------|---------|
| `/trading-ideas <TICKER>` | Standard institutional analysis | 8-section comprehensive report |
| `/trading-ideas <TICKER> --detailed` | Enhanced analysis with options flow | Extended technical and insider analysis |
| `/trading-ideas --help` | Show usage information | Command documentation |

## Repository Structure

```
claude-equity-research/
├── README.md                     # This file
├── LICENSE                       # MIT License
├── commands/
│   ├── trading-ideas.md          # Main Claude Code command
│   └── README.md                 # Command documentation
├── config/
│   ├── config.example.json       # Template configuration
│   └── prompts/                  # Analysis prompt templates
├── examples/
│   └── sample_reports/           # Example analyses (AAPL, HOOD, etc.)
├── docs/
│   ├── methodology.md            # Detailed analysis framework
│   ├── installation.md           # Setup instructions
│   └── customization.md          # Customization guide
├── utils/
│   ├── data_sources.md           # Data source documentation
│   └── validation.py             # Analysis validation tools
└── tests/
    └── test_command.py           # Command functionality tests
```

## Analysis Methodology

Our research framework combines:

### Quantitative Analysis
- **Financial Statements**: Revenue, margins, cash flow analysis
- **Valuation Models**: Multiple approaches (DCF, comparable company, precedent transaction)
- **Technical Indicators**: Support/resistance, momentum, relative strength
- **Options Analytics**: Implied volatility, unusual activity, sentiment indicators

### Qualitative Assessment
- **Competitive Positioning**: Market share, competitive advantages, moat analysis
- **Management Quality**: Track record, capital allocation, strategic vision
- **Regulatory Environment**: Industry-specific risks, compliance issues
- **ESG Factors**: Environmental, social, governance considerations

### Risk Management
- **Scenario Analysis**: Bull/base/bear cases with probability weighting
- **Position Sizing**: Risk-adjusted allocation recommendations (1-5% typical)
- **Stop-Loss Guidance**: Downside protection levels
- **Correlation Analysis**: Portfolio diversification considerations

## Data Sources

- **Financial Data**: SEC filings, earnings reports, company guidance
- **Market Data**: Real-time pricing, volume, technical indicators
- **Analyst Coverage**: Wall Street research, price target updates
- **News & Sentiment**: Financial media, regulatory announcements
- **Options Data**: Unusual activity, implied volatility, positioning
- **Insider Activity**: Form 4 filings, executive transactions

## Professional Disclaimers

### ⚠️ Important Legal Notice

This tool is designed for **educational and research purposes only**. All analysis and recommendations are:

- **Not financial advice** - For informational purposes only
- **Not personalized** - Does not consider individual circumstances
- **Historical data based** - Past performance doesn't guarantee future results
- **Requiring due diligence** - Users must conduct independent research
- **Risk warning included** - All investments carry risk of loss

### Risk Warnings
- Stock prices are volatile and unpredictable
- AI analysis may contain errors or biases
- Market conditions change rapidly
- Regulatory and company-specific risks may not be fully captured
- Position sizing recommendations are general guidelines only

### Professional Consultation
Always consult with qualified financial professionals before making investment decisions. This tool does not replace professional financial advice.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md):

### Development Areas
- Enhanced data source integration
- Improved technical analysis algorithms
- Additional sector-specific metrics
- ESG scoring improvements
- Risk model enhancements

### Code Contributions
```bash
# Fork the repository
git fork https://github.com/quant-sentiment-ai/claude-equity-research

# Create feature branch
git checkout -b feature/your-enhancement

# Submit pull request with detailed description
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support & Community

- 📖 [Documentation](docs/)
- 🐛 [Report Issues](https://github.com/quant-sentiment-ai/claude-equity-research/issues)
- 💬 [Discussions](https://github.com/quant-sentiment-ai/claude-equity-research/discussions)
- 🔄 [Changelog](CHANGELOG.md)

## Acknowledgments

- Built for [Claude Code](https://claude.ai/code) - Anthropic's official CLI
- Inspired by institutional equity research standards
- Community-driven development and feedback

---

**Remember**: This tool provides educational insights only. Always conduct your own due diligence and consult qualified financial professionals before making investment decisions. Past performance does not guarantee future results.