# Claude Code Plugin Documentation

## Overview

The **Claude Equity Research** plugin brings institutional-grade equity analysis directly into your Claude Code workflow. Generate comprehensive research reports with a single slash command - no configuration, API keys, or manual setup required.

### Why Use This Plugin?

- **Professional Analysis**: Wall Street-quality research reports with BUY/SELL/HOLD ratings
- **Real-Time Data**: Live market data, earnings reports, analyst coverage, and insider activity
- **Comprehensive Framework**: 8-section analysis covering fundamentals, technicals, risks, and catalysts
- **Risk Management**: Position sizing guidance and probability-weighted scenarios
- **Zero Configuration**: Works immediately after installation

### Who Is This For?

- **Individual Investors**: Research stocks before making investment decisions
- **Financial Analysts**: Generate preliminary research reports to accelerate workflow
- **Portfolio Managers**: Quick due diligence on potential positions
- **Students**: Learn equity research methodology with real examples
- **Developers**: Integrate financial analysis into AI-powered trading tools

---

## Installation

### Method 1: Interactive Menu (Recommended)

```bash
# Step 1: Add the marketplace
/plugin marketplace add quant-sentiment-ai/claude-equity-research

# Step 2: Open the plugin menu
/plugin

# Step 3: Browse and install
# - Select "Browse Plugins"
# - Find "claude-equity-research"
# - Choose "Install now"
```

### Method 2: Direct Command

```bash
# Add marketplace and install in one flow
/plugin marketplace add quant-sentiment-ai/claude-equity-research
/plugin install claude-equity-research@quant-sentiment-ai
```

### Verify Installation

```bash
# Check that the command is available
/help

# You should see "/trading-ideas" in the command list

# Test the plugin
/trading-ideas AAPL
```

### Post-Installation

Restart Claude Code for optimal performance (recommended but not required).

---

## Commands

### `/trading-ideas [TICKER]`

Generate a comprehensive institutional-grade equity research report for any publicly traded stock.

**Syntax:**
```bash
/trading-ideas <TICKER> [--detailed]
```

**Parameters:**
- `TICKER` (required): Stock ticker symbol (e.g., AAPL, MSFT, TSLA, NVDA)
- `--detailed` (optional): Include enhanced technical analysis and options flow data

**Output Sections:**
1. **Executive Summary**: Investment rating, price target, upside/downside potential
2. **Fundamental Analysis**: Revenue, margins, peer comparison, forward outlook
3. **Catalyst Analysis**: Near-term and medium-term market drivers
4. **Valuation & Price Targets**: Bull/base/bear scenarios with probability weighting
5. **Risk Assessment**: Company-specific and macro risks with position sizing
6. **Technical Context**: Support/resistance levels, momentum indicators, volume
7. **Market Positioning**: Sector performance and relative strength analysis
8. **Insider Signals**: Insider trading activity and institutional ownership

**Output Format:**
- Professional markdown formatting
- Data-driven analysis with specific numbers and percentages
- Investment recommendation table
- Legal disclaimers for educational use

---

## Usage Examples

### Technology Stock Analysis
```bash
/trading-ideas NVDA
```
**Use Case**: Analyze NVIDIA's AI chip business, competitive positioning vs AMD/Intel, and valuation relative to growth prospects.

### Financial Services Analysis
```bash
/trading-ideas JPM
```
**Use Case**: Evaluate J.P. Morgan's earnings power, interest rate sensitivity, book value, and regulatory environment.

### Growth Stock Evaluation
```bash
/trading-ideas TSLA
```
**Use Case**: Assess Tesla's automotive and energy businesses, execution risks, valuation premium, and competitive threats.

### Biotech/Pharma Research
```bash
/trading-ideas PFE
```
**Use Case**: Review pipeline, patent cliffs, R&D productivity, and regulatory risks for Pfizer.

### Detailed Analysis with Options Flow
```bash
/trading-ideas AAPL --detailed
```
**Use Case**: Enhanced report with options market sentiment, unusual activity, and institutional positioning signals.

---

## Sample Output

```markdown
# APPLE INC (AAPL) - ENHANCED EQUITY RESEARCH

## EXECUTIVE SUMMARY
BUY with $250 price target (9% upside) over 12 months. Strong Q4 2024
results driven by iPhone 16 launch and AI integration provide foundation
for premium product cycle. Balanced risk-reward with established ecosystem moat.

## FUNDAMENTAL ANALYSIS
Q4 2024: Revenue $94.9B (+6% YoY), EPS $1.64 (+12% YoY). iPhone revenue
$46.2B (~49% of total), Services +12% to $25B with recurring characteristics.
Gross margin 46.2%, up 100bps YoY driven by favorable mix shift.

## VALUATION & PRICE TARGETS
Consensus: $242 (range $200-$280)
Bull case: $280 | Base case: $250 | Bear case: $200
Probability weighting: 25%/55%/20%

## RECOMMENDATION SUMMARY
| Metric           | Value  |
|------------------|--------|
| Rating           | BUY    |
| Conviction       | High   |
| Price Target     | $250   |
| Upside/Downside  | +9%    |
| Position Size    | 3-5%   |
```

---

## Data Sources

The plugin aggregates data from multiple sources in real-time:

- **Financial Statements**: SEC filings, earnings releases, company guidance
- **Market Data**: Real-time pricing, volume, 52-week ranges, market capitalization
- **Analyst Coverage**: Wall Street research, price target updates, rating changes
- **Technical Indicators**: Moving averages, RSI, MACD, support/resistance levels
- **Options Data**: Implied volatility, put/call ratios, unusual activity (when available)
- **Insider Activity**: Form 4 filings, executive transactions, share buybacks
- **News & Sentiment**: Financial media, regulatory announcements, industry trends
- **Peer Data**: Competitive positioning, valuation multiples, market share

### Data Refresh Rate
All data is fetched live when you run the command, ensuring up-to-date analysis.

---

## Supported Markets

### Primary Support
- **NYSE** (New York Stock Exchange)
- **NASDAQ** (NASDAQ Stock Market)
- **US Over-the-Counter** (major OTC stocks)

### Coverage
- Large-cap stocks (>$10B market cap): Comprehensive data availability
- Mid-cap stocks ($2B-$10B): Good data coverage
- Small-cap stocks (<$2B): Basic coverage, limited analyst data

### Geographic Markets
Currently optimized for US-listed equities. International stocks with ADRs (American Depositary Receipts) are supported using their US ticker symbols.

**Examples:**
- Alibaba: `BABA` (not `9988.HK`)
- Toyota: `TM` (not `7203.T`)
- TSMC: `TSM` (not `2330.TW`)

---

## Requirements

### System Requirements
- **Claude Code**: Version 2.0.11 or higher
- **Claude Subscription**: Paid subscription required (Pro, Team, or Enterprise)
- **Internet Connection**: Active connection for real-time data retrieval
- **Operating System**: macOS, Linux, or Windows with Claude Code installed

### No Additional Setup Required
- No API keys needed
- No environment variables to configure
- No external dependencies to install
- Works immediately after plugin installation

---

## Configuration

This plugin requires **zero configuration** and works out-of-the-box. However, you can customize behavior through Claude Code settings if desired.

### Team Configuration (Optional)

To automatically install this plugin for all team members who trust your repository:

**Add to `.claude/settings.json`:**
```json
{
  "extraKnownMarketplaces": [
    {
      "url": "https://github.com/quant-sentiment-ai/claude-equity-research"
    }
  ],
  "extraKnownPlugins": [
    {
      "name": "claude-equity-research",
      "marketplace": "quant-sentiment-ai/claude-equity-research"
    }
  ]
}
```

When team members trust the repository folder, Claude Code will automatically prompt them to install the marketplace and plugin.

---

## Troubleshooting

### Plugin Not Found After Installation

**Problem**: `/trading-ideas` command not recognized after installation.

**Solutions:**
1. Restart Claude Code (recommended)
2. Verify installation: `/plugin marketplace list`
3. Check plugin is enabled: `/plugin`
4. Reinstall: `/plugin uninstall claude-equity-research@quant-sentiment-ai` then `/plugin install claude-equity-research@quant-sentiment-ai`

### Limited Data for Small-Cap Stocks

**Problem**: Analysis is sparse for smaller stocks.

**Reason**: Small-cap stocks have limited analyst coverage and fewer public data sources.

**Suggestion**: Use the plugin for preliminary research, supplement with company filings and industry reports.

### Outdated Price Targets

**Problem**: Analyst price targets seem stale.

**Reason**: Some stocks have infrequent analyst updates.

**Note**: The plugin fetches the most recent available data. Check the dates in the output to assess freshness.

### "Too Many Requests" Error

**Problem**: Error message when running multiple analyses rapidly.

**Reason**: Rate limiting from data sources.

**Solution**: Wait 30-60 seconds between queries. The plugin fetches data from multiple sources simultaneously.

### Wrong Ticker Symbol

**Problem**: No data returned or wrong company analyzed.

**Solution**: Verify ticker symbol on Yahoo Finance or company website. Use US ticker for ADRs.

---

## Plugin Management Commands

### View Installed Plugins
```bash
/plugin
```

### List Known Marketplaces
```bash
/plugin marketplace list
```

### Enable/Disable Plugin
```bash
/plugin enable claude-equity-research@quant-sentiment-ai
/plugin disable claude-equity-research@quant-sentiment-ai
```

### Uninstall Plugin
```bash
/plugin uninstall claude-equity-research@quant-sentiment-ai
```

### Update Plugin
```bash
# Uninstall old version
/plugin uninstall claude-equity-research@quant-sentiment-ai

# Reinstall latest version
/plugin install claude-equity-research@quant-sentiment-ai
```

---

## Methodology

### Analytical Framework

The plugin follows institutional equity research standards:

**Quantitative Analysis:**
- Financial statement analysis (income, balance sheet, cash flow)
- Valuation modeling (DCF, comparable company, precedent transaction)
- Technical analysis (chart patterns, momentum indicators)
- Statistical metrics (volatility, beta, correlation)

**Qualitative Assessment:**
- Competitive positioning and moat analysis
- Management quality and capital allocation
- Industry dynamics and regulatory environment
- ESG factors and governance considerations

**Risk Management:**
- Scenario analysis with probability weighting
- Position sizing recommendations (typically 1-5% of portfolio)
- Downside protection levels
- Portfolio diversification considerations

### Quality Standards

All reports include:
- Specific financial metrics with numbers and percentages
- Timeframes for all data points (YoY, QoQ, etc.)
- Analyst firm names and price targets
- Conviction levels (High/Medium/Low)
- Risk-adjusted position sizing
- Professional disclaimers

---

## Legal & Risk Disclaimers

### Important Notice

This plugin is designed for **educational and research purposes only**. All analysis and recommendations are:

- **Not Financial Advice**: Information provided is for educational purposes only
- **Not Personalized**: Does not consider individual financial circumstances, risk tolerance, or investment objectives
- **Historical Data Based**: Past performance does not guarantee future results
- **Requiring Due Diligence**: Users must conduct independent research and verification
- **Risk Warning Included**: All investments carry risk of loss, including complete loss of principal

### Risk Warnings

- Stock prices are volatile and unpredictable
- AI-generated analysis may contain errors, biases, or outdated information
- Market conditions change rapidly; analysis may become outdated quickly
- Regulatory and company-specific risks may not be fully captured
- Position sizing recommendations are general guidelines only

### Professional Consultation

Always consult with qualified financial professionals (licensed financial advisors, CPAs, attorneys) before making investment decisions. This tool does not replace professional financial, tax, or legal advice.

### No Liability

The creators, maintainers, and distributors of this plugin assume no liability for investment losses, missed opportunities, or damages resulting from use of this tool.

---

## Support & Community

### Documentation
- **Main README**: [Repository README](https://github.com/quant-sentiment-ai/claude-equity-research/blob/main/README.md)
- **Methodology Guide**: [docs/methodology.md](https://github.com/quant-sentiment-ai/claude-equity-research/blob/main/docs/methodology.md)
- **Customization Guide**: [docs/customization.md](https://github.com/quant-sentiment-ai/claude-equity-research/blob/main/docs/customization.md)

### Get Help
- **Report Issues**: [GitHub Issues](https://github.com/quant-sentiment-ai/claude-equity-research/issues)
- **Discussions**: [GitHub Discussions](https://github.com/quant-sentiment-ai/claude-equity-research/discussions)
- **Feature Requests**: Submit via GitHub Issues with "enhancement" label

### Contributing
We welcome contributions! See [Contributing Guidelines](https://github.com/quant-sentiment-ai/claude-equity-research/blob/main/CONTRIBUTING.md) for details.

---

## Version History

### 1.0.0 (Current)
- Initial public release
- `/trading-ideas` command with standard and `--detailed` modes
- 8-section institutional research framework
- Real-time data integration
- Zero-configuration installation

---

## License

This plugin is licensed under the MIT License. See [LICENSE](https://github.com/quant-sentiment-ai/claude-equity-research/blob/main/LICENSE) for details.

---

**Built for Claude Code** | [Report Issues](https://github.com/quant-sentiment-ai/claude-equity-research/issues) | [View Source](https://github.com/quant-sentiment-ai/claude-equity-research)
