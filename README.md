# Tasktronic
## Automates web tasks

It can automate a sequence of tasks. For example : 

        task="Look up options for buying LG G4 TV 55 inch. "
             "Find online retailers that can deliver to 400001 "
             " TV must be G4 Model from LG, 55 inch. "
             " Include Amazon, Flipkart, Vijay Sales, Croma, and Reliance Digital in retailers "
             "Print name, delivery date, number of reviews and price for each retailer found. "
             "Need the TV by 25h Jan ",

![Sample Run](docs/images/agent_history.gif)

## Output
```
Result: Found the LG G4 TV 55 inch at multiple retailers:

1. **Reliance Digital**
   - **Price**: ₹1,82,990.00  
   - **Delivery**: Free 1–6 day delivery  
   - **Reviews**: Not specified  

2. **Croma**
   - **Price**: ₹1,99,990.00  
   - **Delivery**: In stock  
   - **Reviews**: Not specified  

3. **Amazon**, **Flipkart**, and **Vijay Sales**: Information not yet retrieved but searches were performed. ```
```

## How 

Tasktronic operates through a systematic process:

1. **Task Comprehension:** Interprets the specified task.
2. **Strategic Planning:** Develops an execution plan.
3. **Action Sequence Generation:** Creates a series of actions to accomplish the task.
4. **Execution Phase:**
   - Generates Playwright scripts tailored for each target webpage.
   - Executes these scripts.
   - Transmits the Document Object Model (DOM) and screenshots to a Vision LLM (OpenAI or Local like Qwen 2.5).
   - Analyzes the received data.
   - Iteratively generates additional actions as necessary.
5. **Result Summarization:** Compiles and presents the final output.


## Notes 

To set up playwright components, run the following command:

```
playwright install    
```

To start Chrome with remote debugging enabled, run the following command:

### Windows
```
start chrome  --remote-debugging-port=9222

OR

"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```
### Mac
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

### Linux
```
google-chrome --remote-debugging-port=9222
```
