import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

import asyncio
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

browser = Browser(
	config=BrowserConfig(
		headless=False,
		cdp_url="http://localhost:9222",
        extra_chromium_args=['--window-size=1000,1000'],
	)
)




async def run_search() :
    agent = Agent(
        task="Look up options for buying LG G4 TV 55 inch. "
             "Find online retailers that can deliver to 400001 "
             " TV must be G4 Model from LG, 55 inch. "
             " Include Amazon, Flipkart, Vijay Sales, Croma, and Reliance Digital in retailers "
             "Print name, delivery date, number of reviews and price for each retailer found. "
             "Need the TV by 25h Jan ",
        browser=browser,
        llm=ChatOpenAI(model='gpt-4o-mini'),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())