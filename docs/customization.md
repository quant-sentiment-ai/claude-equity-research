# Customization Guide

Complete guide for customizing Claude Equity Research to meet specific analysis needs and preferences.

## Overview

Claude Equity Research is designed to be highly customizable while maintaining professional standards. This guide covers command modifications, sector-specific adaptations, and advanced configuration options.

## Command Customization

### Basic Modifications

#### Editing the Core Command
```bash
# Backup original command
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/trading-ideas-backup.md

# Edit the command
vim ~/.claude/commands/trading-ideas.md
```

#### Key Customizable Sections

**1. Frontmatter Configuration**
```yaml
---
description: Your custom description
argument-hint: [TICKER] [--custom-flag]
allowed-tools: WebSearch, WebFetch, Grep, Read
timeout: 300
---
```

**2. Analysis Framework**
Modify the "OUTPUT FORMAT" section to add/remove sections:
```markdown
## ENHANCED ANALYSIS SECTIONS
- **Dividend Analysis**: [For income-focused strategies]
- **ESG Deep Dive**: [For sustainable investing]
- **International Exposure**: [For global considerations]
```

**3. Risk Parameters**
Adjust position sizing recommendations:
```markdown
**Position sizing**: [X]%-[Y]% allocation based on [custom criteria]
- Conservative: 1-2% max position
- Moderate: 2-4% max position  
- Aggressive: 3-7% max position
```

### Sector-Specific Customizations

#### Technology Sector Command
```bash
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/tech-analysis.md
```

**Add Tech-Specific Metrics**:
```markdown
### Technology Analysis Additions:
- **R&D Intensity**: R&D spend as % of revenue vs peers
- **Patent Portfolio**: IP strength and protection
- **Platform Metrics**: MAU, DAU, engagement rates
- **SaaS Metrics**: ARR, churn rate, NPS scores
- **AI/Cloud Exposure**: Revenue from emerging technologies
```

#### Financial Services Command
```bash
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/financial-analysis.md
```

**Add Financial-Specific Metrics**:
```markdown
### Financial Services Analysis:
- **Net Interest Margin**: Spread analysis and sensitivity
- **Credit Quality**: NPL ratios, provision coverage
- **Capital Ratios**: Tier 1, Basel III compliance
- **Fee Income**: Non-interest revenue diversification
- **Book Value**: Tangible book value and ROE analysis
```

#### Healthcare/Biotech Command
```bash
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/biotech-analysis.md
```

**Add Healthcare-Specific Metrics**:
```markdown
### Healthcare/Biotech Analysis:
- **Pipeline Value**: Phase breakdown and probability-adjusted NPV
- **Patent Cliff**: Drug expirations and generic threats
- **Regulatory Timeline**: FDA approvals and milestones
- **Market Access**: Payer coverage and pricing pressure
- **R&D Productivity**: Success rates and ROI metrics
```

## Advanced Configuration

### Custom Risk Models

#### Conservative Risk Profile
```markdown
### Conservative Analysis Parameters:
- **Maximum Position Size**: 2% of portfolio
- **Stop Loss**: 5% below entry
- **Minimum Conviction**: High only
- **Dividend Requirement**: Yield > 2%
- **Quality Filters**: Investment grade credit only
```

#### Growth-Focused Profile
```markdown
### Growth Analysis Parameters:
- **Growth Threshold**: Revenue growth > 15% YoY
- **Market Cap Focus**: $10B+ only
- **Innovation Metrics**: R&D/Revenue > industry average
- **Market Leadership**: Top 3 market position required
```

#### Value-Oriented Profile
```markdown
### Value Analysis Parameters:
- **Valuation Metrics**: P/E < 15x, P/B < 2x
- **Financial Health**: Debt/EBITDA < 3x
- **Dividend History**: 10+ years of payments
- **FCF Yield**: > 5% free cash flow yield
```

### Custom Output Formats

#### Executive Summary Only
Create a minimal command for quick decisions:
```bash
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/quick-analysis.md
```

Modify to focus on essentials:
```markdown
## QUICK ANALYSIS OUTPUT

### INVESTMENT DECISION
**[BUY/SELL/HOLD]** - **$[TARGET]** - **[%] upside/downside**

### KEY POINTS
- Revenue: [Latest quarter performance]
- Valuation: [P/E vs peers]
- Catalyst: [Primary driver]
- Risk: [Main concern]

### RECOMMENDATION
Position Size: [%] | Timeframe: [months] | Conviction: [High/Med/Low]
```

#### Detailed Technical Focus
Create a technical analysis focused command:
```bash
cp ~/.claude/commands/trading-ideas.md ~/.claude/commands/technical-analysis.md
```

Enhance technical sections:
```markdown
## ENHANCED TECHNICAL ANALYSIS

### CHART PATTERNS
- **Primary Pattern**: [Trend, consolidation, reversal]
- **Key Levels**: Support [$X], Resistance [$Y]
- **Volume Profile**: [Accumulation/Distribution analysis]

### MOMENTUM INDICATORS
- **RSI**: [Current reading and divergences]
- **MACD**: [Signal line crossovers]
- **Moving Averages**: [20/50/200 day relationships]

### OPTIONS INTELLIGENCE
- **Put/Call Ratio**: [Current vs historical average]
- **Implied Volatility**: [IV rank and percentile]
- **Unusual Activity**: [Large trades and positioning]
- **Gamma Exposure**: [Key strike levels]
```

## Configuration Files

### Creating Custom Config
```bash
mkdir -p ~/.claude/equity-research
```

**Basic Configuration** (`~/.claude/equity-research/config.json`):
```json
{
  "analysis_settings": {
    "default_timeframe": "12m",
    "risk_tolerance": "moderate",
    "focus_areas": ["fundamental", "technical", "risk"],
    "output_style": "institutional"
  },
  "sector_preferences": {
    "technology": {
      "weight_multiplier": 1.2,
      "metrics": ["user_growth", "recurring_revenue", "innovation"]
    },
    "financials": {
      "weight_multiplier": 0.8,
      "metrics": ["nim", "credit_quality", "book_value"]
    }
  },
  "risk_parameters": {
    "max_position_size": 0.05,
    "stop_loss_threshold": 0.08,
    "min_conviction_score": 0.7
  }
}
```

### Environment-Specific Configs

#### Development Configuration
```json
{
  "analysis_settings": {
    "debug_mode": true,
    "verbose_output": true,
    "include_data_sources": true
  },
  "data_sources": {
    "enable_caching": false,
    "rate_limit": 30
  }
}
```

#### Production Configuration
```json
{
  "analysis_settings": {
    "debug_mode": false,
    "optimize_performance": true,
    "include_disclaimers": true
  },
  "data_sources": {
    "enable_caching": true,
    "cache_duration": 900,
    "rate_limit": 60
  }
}
```

## Custom Analysis Templates

### ESG-Focused Analysis
```markdown
### ESG ANALYSIS FRAMEWORK

#### Environmental Assessment
- **Carbon Footprint**: Scope 1, 2, 3 emissions
- **Climate Targets**: Net-zero commitments and progress
- **Resource Efficiency**: Water, waste, energy metrics
- **Green Revenue**: % from sustainable products/services

#### Social Impact
- **Diversity Metrics**: Board and workforce diversity
- **Employee Satisfaction**: Glassdoor ratings, turnover
- **Community Investment**: Local economic impact
- **Product Safety**: Quality standards and recalls

#### Governance Quality
- **Board Independence**: % independent directors
- **Executive Compensation**: Pay for performance alignment
- **Transparency**: ESG reporting quality and frequency
- **Risk Management**: Oversight and control frameworks
```

### Dividend-Focused Analysis
```markdown
### DIVIDEND ANALYSIS FRAMEWORK

#### Dividend Sustainability
- **Payout Ratio**: Earnings and FCF coverage
- **Dividend History**: Years of consecutive payments/increases
- **Yield Analysis**: Current vs historical vs peers
- **Growth Rate**: 3/5/10 year CAGR

#### Quality Metrics
- **FCF Coverage**: Free cash flow vs dividend payments
- **Debt Impact**: Interest coverage and covenant compliance
- **Cyclicality**: Earnings stability through cycles
- **Capital Allocation**: Balance between growth and income

#### Forward Outlook
- **Management Guidance**: Dividend policy statements
- **Earnings Growth**: Sustainability of payout growth
- **Sector Trends**: Industry-specific dividend patterns
```

## Workflow Automation

### Batch Analysis Scripts

#### Portfolio Monitoring Script
```bash
#!/bin/bash
# portfolio-analysis.sh

TICKERS=("AAPL" "GOOGL" "MSFT" "TSLA" "JPM")
OUTPUT_DIR="~/equity-reports/$(date +%Y%m%d)"

mkdir -p "$OUTPUT_DIR"

for ticker in "${TICKERS[@]}"; do
    echo "Analyzing $ticker..."
    echo "/trading-ideas $ticker" | claude-code > "$OUTPUT_DIR/${ticker}_analysis.md"
    sleep 5  # Rate limiting
done

echo "Analysis complete. Reports saved to $OUTPUT_DIR"
```

#### Sector Rotation Analysis
```bash
#!/bin/bash
# sector-analysis.sh

SECTORS=(
    "XLK:Technology"
    "XLF:Financials" 
    "XLV:Healthcare"
    "XLE:Energy"
    "XLI:Industrials"
)

for sector in "${SECTORS[@]}"; do
    ticker="${sector%%:*}"
    name="${sector##*:}"
    echo "Analyzing $name sector ($ticker)..."
    echo "/trading-ideas $ticker" | claude-code
    echo "---"
done
```

### Integration with Other Tools

#### Python Integration
```python
import subprocess
import json
from datetime import datetime

def run_equity_analysis(ticker, detailed=False):
    """Run Claude equity analysis and return structured data."""
    
    cmd = ["claude-code"]
    analysis_cmd = f"/trading-ideas {ticker}"
    if detailed:
        analysis_cmd += " --detailed"
    
    result = subprocess.run(
        cmd, 
        input=analysis_cmd,
        text=True, 
        capture_output=True
    )
    
    return {
        'ticker': ticker,
        'timestamp': datetime.now().isoformat(),
        'analysis': result.stdout,
        'success': result.returncode == 0
    }

# Usage
analysis = run_equity_analysis("AAPL", detailed=True)
print(f"Analysis for {analysis['ticker']} completed at {analysis['timestamp']}")
```

## Testing and Validation

### Command Testing
```bash
# Test basic functionality
echo "/trading-ideas AAPL" | claude-code

# Test error handling
echo "/trading-ideas INVALID" | claude-code

# Test custom command
echo "/tech-analysis NVDA" | claude-code
```

### Performance Monitoring
```bash
# Timing analysis
time (echo "/trading-ideas AAPL" | claude-code)

# Memory usage
/usr/bin/time -v (echo "/trading-ideas AAPL" | claude-code)
```

## Best Practices

### Command Development
1. **Always Backup**: Save original before modifications
2. **Test Thoroughly**: Validate with multiple tickers
3. **Document Changes**: Comment custom modifications
4. **Version Control**: Track command iterations

### Customization Guidelines
1. **Maintain Disclaimers**: Always include risk warnings
2. **Preserve Structure**: Keep core analysis framework
3. **Test Edge Cases**: Validate with different market conditions
4. **Monitor Performance**: Ensure customizations don't slow analysis

### Deployment Strategy
1. **Staged Rollout**: Test in development environment first
2. **User Training**: Document new features and workflows
3. **Feedback Loop**: Collect user feedback and iterate
4. **Maintenance Plan**: Regular updates and improvements

## Support and Troubleshooting

### Common Customization Issues
1. **YAML Syntax Errors**: Validate frontmatter format
2. **Tool Permissions**: Ensure allowed-tools are correct
3. **Markdown Formatting**: Check for proper section headers
4. **Performance Issues**: Monitor analysis execution time

### Getting Help
- Review [installation guide](installation.md) for setup issues
- Check [methodology](methodology.md) for analysis framework
- Submit issues to [GitHub repository](https://github.com/quant-sentiment-ai/claude-equity-research/issues)
- Join community discussions for best practices sharing

This customization guide enables you to tailor Claude Equity Research to your specific investment process while maintaining professional analysis standards.