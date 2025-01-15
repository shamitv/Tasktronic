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
        task="Open Amazon.in and search for OLED TV 55 Inch. "
             "Filter for at least 4 start rating. "
             "Sort by price, high to low. "
             "If item is sponsored, skip it."
             "Open Product page for first item that is not sponsored. "
             "Print name, number of reviews and price of first item",
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