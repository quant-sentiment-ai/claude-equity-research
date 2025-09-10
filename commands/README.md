# Claude Code Commands

This directory contains the core `/trading-ideas` command for Claude Code integration.

## Installation

### Quick Installation (Recommended)
```bash
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md
```

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/quant-sentiment-ai/claude-equity-research.git

# Copy command to Claude Code
cp claude-equity-research/commands/trading-ideas.md ~/.claude/commands/
```

## Usage

Once installed, the command is available system-wide in any Claude Code session:

```bash
/trading-ideas AAPL          # Apple Inc. analysis
/trading-ideas HOOD --detailed   # Enhanced Robinhood analysis
/trading-ideas TSLA          # Tesla comprehensive research
```

## Command Features

### Core Analysis Sections
1. **Executive Summary** - BUY/SELL/HOLD with price target
2. **Fundamental Analysis** - Financial metrics and peer comparison
3. **Catalyst Analysis** - Near-term and medium-term drivers
4. **Valuation & Price Targets** - Bull/base/bear scenarios
5. **Risk Assessment** - Company and macro risks with position sizing
6. **Technical Context** - Support/resistance and options flow
7. **Market Positioning** - Sector rotation and relative strength
8. **Insider Signals** - Executive trading and institutional activity

### Professional Standards
- Institutional-grade formatting
- Specific financial metrics with percentages
- Price targets with upside/downside calculations
- Position sizing recommendations (1-5% typical)
- Comprehensive legal disclaimers

### Data Requirements
- Real-time web search integration
- Parallel search strategy for comprehensive coverage
- Analyst firm citations and price target sources
- Specific dollar amounts for insider trading
- Technical levels with exact support/resistance prices

## Customization

To modify the command:

1. Edit `~/.claude/commands/trading-ideas.md`
2. Adjust analysis sections or add new metrics
3. Modify risk assessment criteria
4. Update disclaimer language if needed

The command will automatically reload in new Claude Code sessions.

## Troubleshooting

### Command Not Found
- Verify file exists: `ls ~/.claude/commands/trading-ideas.md`
- Check file permissions: `chmod 644 ~/.claude/commands/trading-ideas.md`
- Restart Claude Code session

### Incomplete Analysis
- Ensure internet connectivity for web searches
- Verify ticker symbol format (1-5 letters)
- Check that WebSearch and WebFetch tools are available

### Format Issues
- Command template enforces consistent formatting
- Review frontmatter configuration if customized
- Ensure YAML syntax is valid in frontmatter

## Updates

To update the command with latest improvements:

```bash
# Download latest version
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md

# Verify update
head -10 ~/.claude/commands/trading-ideas.md
```

## Support

For issues or feature requests:
- [GitHub Issues](https://github.com/quant-sentiment-ai/claude-equity-research/issues)
- [Discussions](https://github.com/quant-sentiment-ai/claude-equity-research/discussions)
- [Documentation](../docs/)

---

**Legal Notice**: This command generates educational content only. Not financial advice. Always consult qualified professionals before making investment decisions.