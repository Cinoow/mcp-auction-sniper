from mcp.server.fastmcp import FastMCP
from googlesearch import search
import re

# Initialisation du serveur FastMCP
mcp = FastMCP("AuctionSniper")

@mcp.tool()
def find_auctions(city: str = "Courbevoie"):
    """
    Search for upcoming judicial liquidations and auctions in a specific city.
    Useful for finding office equipment or retail stock liquidations.
    """
    # On cible spécifiquement les liquidations judiciaires
    query = f'site:interencheres.com "liquidation judiciaire" {city}'
    
    results = []
    try:
        # On récupère les 5 meilleurs liens
        for url in search(query, num=5, stop=5, pause=2):
            results.append(url)
        
        if not results:
            return f"No auctions found for {city} via Interencheres. Try broadening the search to 'Hauts-de-Seine'."
            
        return "Upcoming Auctions Found:\n" + "\n".join(results)
    except Exception as e:
        return f"Error during search: {str(e)}"

@mcp.tool()
def analyze_deal(buy_price: float, estimated_resale: float):
    """
    Calculate the net profit after French judicial auction fees (14.28%).
    """
    JUDICIAL_FEES = 1.1428
    total_cost = buy_price * JUDICIAL_FEES
    net_profit = estimated_resale - total_cost
    roi = (net_profit / total_cost) * 100
    
    # Détermination du score d'opportunité
    if roi > 40:
        signal = "🚀 STRONG BUY - High margin"
    elif roi > 15:
        signal = "⚖️ INTERESTING - Fair deal"
    else:
        signal = "❌ AVOID - Too risky or low margin"
        
    return {
        "Signal": signal,
        "Total Purchase Cost (incl. fees)": f"{round(total_cost, 2)}€",
        "Net Profit": f"{round(net_profit, 2)}€",
        "ROI": f"{round(roi, 1)}%"
    }

@mcp.tool()
def extract_lot_info(catalog_text: str):
    """
    Helps Claude parse raw catalog text to identify high-value items 
    like 'MacBook', 'iPhone', 'Herman Miller', etc.
    """
    # Liste de mots-clés "High Resale Value"
    keywords = ["MacBook", "iPhone", "iPad", "Ecran", "Serveur", "Stock", "Velo", "Montre"]
    found_items = []
    
    for word in keywords:
        if word.lower() in catalog_text.lower():
            found_items.append(word)
            
    if not found_items:
        return "No high-value tech/furniture keywords detected in the provided text."
        
    return f"Potential high-value lots detected: {', '.join(found_items)}"

if __name__ == "__main__":
    mcp.run()