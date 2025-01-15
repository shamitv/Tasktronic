# Tasktronic
##Automates web tasks

It can automate a sequence of tasks. For example : 

        task="Open Amazon.in and search for OLED TV 55 Inch. "
             "Filter for at least 4 start rating. "
             "Sort by price, high to low. "
             "If item is sponsored, skip it."
             "Open Product page for first item that is not sponsored. "
             "Print name, number of reviews and price of first item",

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
