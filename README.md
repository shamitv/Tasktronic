# Tasktronic
##Automates web tasks

It can automate a sequence of tasks. For example : 

        task="Look up options for buying LG G4 TV 55 inch. "
             "Find online retailers that can deliver to 400001 "
             " TV must be G4 Model from LG, 55 inch. "
             " Include Amazon, Flipkart, Vijay Sales, Croma, and Reliance Digital in retailers "
             "Print name, delivery date, number of reviews and price for each retailer found. "
             "Need the TV by 25h Jan ",


![Sample Run](docs/images/agent_history.gif)

##Output
```
Result: Retailers found for LG G4 TV 55 inch:

1. **LG Electronics**
   - **Price**: ₹180,989
   - **Delivery**: Free, delivery date not specified
   - **Reviews**: 399 Reviews (4.7 out of 5 stars)

2. **Poorvika Mobile**
   - **Price**: ₹179,990
   - **Delivery**: Free, 3–6 days delivery
   - **Reviews**: Not specified

3. **Sathya Agencies**
   - **Price**: ₹164,998
   - **Delivery**: Free, 3–7 days delivery
   - **Reviews**: Not specified

4. **Mahajan Electronics**
   - **Price**: ₹163,490
   - **Delivery**: Free, 4–7 days delivery
   - **Reviews**: Not specified

5. **Kohinoor Electronics**
   - **Price**: ₹250,000
   - **Delivery**: Free, 2-day delivery
   - **Reviews**: Not specified

The LG G4 TV is available from various retailers, with the best price being ₹163,490 from Mahajan Electronics. Ensure to choose a retailer that can deliver by the 25th of January.
```

##Notes 

To set up playwright components, run the following command:

```
playwright install    
```

To start Chrome with remote debugging enabled, run the following command:

#Windows
```
start chrome  --remote-debugging-port=9222

OR

"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```
#Mac
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

#Linux
```
google-chrome --remote-debugging-port=9222
```
