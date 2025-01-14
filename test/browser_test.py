import os

# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

import asyncio
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_ollama import ChatOllama

browser = Browser(
	config=BrowserConfig(
		headless=False,
		cdp_url="http://localhost:9222",
	)
)


async def run_search() -> str:
    agent = Agent(
        task="Open Amazon.in and search for a 32-inch TV. Sort by rating and print price of first item",
        browser=browser,
        llm=ChatOllama(
            model="qwen2.5:14b",
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())