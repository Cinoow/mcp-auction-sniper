# MCP Auction Sniper 🎯

A lightweight Model Context Protocol (MCP) server designed to identify and analyze distressed asset opportunities (judicial liquidations and auctions) in the Hauts-de-Seine (92) area, France.

## 🚀 Overview

This tool empowers AI agents (like Claude Desktop) to act as a local investment scout. It bridges the gap between public legal announcements and real-time profitability analysis.

- **Target Areas:** Courbevoie, Levallois-Perret, Nanterre
- **Goal:** Rapidly identify high-margin resale opportunities (IT equipment, furniture, luxury goods) from business liquidations

## 🛠 Features

* **Live Sourcing:** Programmatic search of liquidation catalogs via `interencheres` and legal announcement portals
* **Yield Engine:** Instant ROI calculation including mandatory French judicial fees (14.28%)
* **Risk Assessment:** Automated status flagging (TOP DEAL vs. NOT PROFITABLE)

## 📂 Structure

* `servers/` : Core MCP Python logic
* `config/` : Configuration templates for MCP clients
* `data/` : Local storage for scraped catalogs and lead lists (gitignored)

## ⚡️ Quick Start

### Prerequisites
- Python 3.10+
- [Claude Desktop](https://claude.ai/download)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp-auction-sniper.git
   cd mcp-auction-sniper
   ```

2. Install dependencies:
   ```bash
   pip install mcp googlesearch-python
   ```

### Configuration

Add to your Claude Desktop configuration file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "auction-sniper": {
      "command": "python",
      "args": ["/YOUR_ABSOLUTE_PATH/servers/auction_server.py"]
    }
  }
}
```

**Note:** Replace `/YOUR_ABSOLUTE_PATH/` with the absolute path to your project folder.

## 📋 Usage

Once configured, launch Claude Desktop. The MCP server will be automatically available and you can ask Claude to analyze auctions in your target area.

Example query:
> "Search for current judicial liquidations in Courbevoie and calculate their potential profitability"

## ⚠️ Disclaimer

This tool is for educational and data aggregation purposes only. Always verify auction terms, VAT status, and physical asset condition before bidding.

## 📝 License

This project is licensed under [MIT/Apache-2.0/other] (to be specified).

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

*Built with ❤️ to optimize local investment opportunity scouting*