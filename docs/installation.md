# Installation Guide

Complete setup instructions for Claude Equity Research integration with Claude Code.

## Quick Installation

### Option 1: Direct Download (Recommended)
```bash
# Install the trading-ideas command system-wide
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md

# Verify installation
ls ~/.claude/commands/trading-ideas.md

# Test the command
# (Open new Claude Code session and try: /trading-ideas AAPL)
```

### Option 2: Repository Clone
```bash
# Clone the full repository
git clone https://github.com/quant-sentiment-ai/claude-equity-research.git
cd claude-equity-research

# Copy command to Claude Code
cp commands/trading-ideas.md ~/.claude/commands/

# Optional: Set up development environment
cp config/config.example.json config/config.json
```

## Prerequisites

### Required
- **Claude Code CLI**: Latest version from [claude.ai/code](https://claude.ai/code)
- **Internet Connection**: For real-time data retrieval
- **Terminal Access**: Command-line interface

### Optional
- **Git**: For repository cloning and updates
- **Text Editor**: For command customization

## Verification

### Test Basic Functionality
```bash
# Start Claude Code session
claude-code

# Test the command
/trading-ideas AAPL
```

**Expected Output**: Comprehensive equity research report with:
- Executive Summary with BUY/SELL/HOLD recommendation
- Fundamental analysis with specific metrics
- Price target and upside/downside calculation
- Risk assessment and position sizing

### Verify Command Features
```bash
# Test enhanced analysis
/trading-ideas HOOD --detailed

# Test different sectors
/trading-ideas JPM    # Financial services
/trading-ideas NVDA   # Technology/AI
/trading-ideas TSLA   # Growth/automotive
```

## Directory Structure

After installation, your Claude Code setup should include:

```
~/.claude/
├── commands/
│   └── trading-ideas.md     # ✓ Main analysis command
├── settings.local.json      # Your Claude Code settings
└── [other directories...]

# Optional: Full repository structure
claude-equity-research/
├── README.md
├── LICENSE
├── commands/
│   ├── trading-ideas.md
│   └── README.md
├── config/
├── docs/
├── examples/
└── utils/
```

## Configuration

### Default Settings
The command works out-of-the-box with default settings:
- 12-month analysis timeframe
- Moderate risk assessment
- Institutional-grade formatting
- Comprehensive disclaimer inclusion

### Custom Configuration (Optional)
```bash
# Create custom config
mkdir -p ~/.claude/equity-research
cp claude-equity-research/config/config.example.json ~/.claude/equity-research/config.json

# Edit configuration
vim ~/.claude/equity-research/config.json
```

**Configuration Options**:
- Analysis timeframes (1m, 3m, 6m, 12m)
- Risk levels (conservative, moderate, aggressive)
- Output formats (terminal, markdown, detailed)
- Position sizing parameters

## Troubleshooting

### Command Not Found
```bash
# Check if file exists
ls -la ~/.claude/commands/trading-ideas.md

# If missing, reinstall
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md

# Check file permissions
chmod 644 ~/.claude/commands/trading-ideas.md

# Restart Claude Code session
```

### Incomplete Analysis
**Symptoms**: Missing sections or error messages

**Solutions**:
1. **Check Internet Connection**: Command requires web access
2. **Verify Ticker Symbol**: Use valid stock tickers (1-5 letters)
3. **Try Different Ticker**: Some stocks may have limited data
4. **Check Claude Code Version**: Ensure latest version

```bash
# Test with known-good ticker
/trading-ideas AAPL

# Check Claude Code version
claude-code --version
```

### Format Issues
**Symptoms**: Inconsistent output formatting

**Solutions**:
1. **Verify Command File**: Ensure clean installation
2. **Check for Customizations**: Reset to default if modified
3. **Restart Session**: Commands reload on new sessions

```bash
# Restore default command
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md

# Start fresh session
exit  # Exit current Claude Code session
claude-code  # Start new session
```

## Updates

### Manual Update
```bash
# Download latest version
curl -o ~/.claude/commands/trading-ideas.md https://raw.githubusercontent.com/quant-sentiment-ai/claude-equity-research/main/commands/trading-ideas.md

# Verify update
head -10 ~/.claude/commands/trading-ideas.md
```

### Git-based Update (if using repository)
```bash
cd claude-equity-research
git pull origin main
cp commands/trading-ideas.md ~/.claude/commands/
```

### Version Check
```bash
# Check command version (look for version info in file header)
grep -i "version\|updated" ~/.claude/commands/trading-ideas.md
```

## Advanced Setup

### Multiple Environments
```bash
# Development setup
cp commands/trading-ideas.md ~/.claude/commands/trading-ideas-dev.md
# Edit development version...

# Production setup  
cp commands/trading-ideas.md ~/.claude/commands/trading-ideas.md
```

### Custom Analysis Templates
```bash
# Create custom sector-specific commands
cp commands/trading-ideas.md ~/.claude/commands/tech-analysis.md
cp commands/trading-ideas.md ~/.claude/commands/biotech-analysis.md

# Customize each for sector-specific metrics
```

### Integration with Workflows
```bash
# Batch analysis script
#!/bin/bash
tickers=("AAPL" "GOOGL" "MSFT" "TSLA")
for ticker in "${tickers[@]}"; do
    echo "Analyzing $ticker..."
    echo "/trading-ideas $ticker" | claude-code
done
```

## Support

### Getting Help
- 📖 [Documentation](https://github.com/quant-sentiment-ai/claude-equity-research/tree/main/docs)
- 🐛 [Report Issues](https://github.com/quant-sentiment-ai/claude-equity-research/issues)
- 💬 [Discussions](https://github.com/quant-sentiment-ai/claude-equity-research/discussions)

### Common Issues
1. **Permission Denied**: Run `chmod 644 ~/.claude/commands/trading-ideas.md`
2. **Network Errors**: Check internet connection and try again
3. **Invalid Ticker**: Use proper stock ticker symbols (AAPL, not Apple)
4. **Missing Data**: Some newer/smaller companies may have limited coverage

### Debug Mode
```bash
# Enable verbose output for troubleshooting
export CLAUDE_DEBUG=1
/trading-ideas AAPL
```

---

**Next Steps**: 
- Try your first analysis: `/trading-ideas AAPL`
- Review [Usage Examples](../examples/)
- Read [Methodology](methodology.md) for analysis framework details
- Explore [Customization Guide](customization.md) for advanced features