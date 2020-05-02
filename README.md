```
     _ ___  ___  _  _   _         __  __ ___ ___  ___  _    
  _ | / __|/ _ \| \| | | |_ ___  |  \/  / __/ __|/ _ \| |   
 | || \__ \ (_) | .` | |  _/ _ \ | |\/| \__ \__ \ (_) | |__ 
  \__/|___/\___/|_|\_|  \__\___/ |_|  |_|___/___/\__\_\____|
                                                                                                                        
```

### About
Simple tool for convert your **JSON** file into **MSSQL** table

**IMPORTANT**: in this project you can convert JSON file from [Scrapy](https://docs.scrapy.org/en/latest/) output

### Usage
```
[-t] [<DB table name>]: insert JSON file name from scrapy output

python main.py -t Colors.json
```

## Example
From this:
```json
[{
   "color": "red",
   "colorValue": "#f00"
}, {
   "color": "green",
   "colorValue": "#0f0"
}, {
   "color": "blue",
   "colorValue": "#00f"
}, {
   "color": "cyan",
   "colorValue": "#0ff"
}, {
   "color": "magenta",
   "colorValue": "#f0f"
}, {
   "color": "yellow",
   "colorValue": "#ff0"
}, {
   "color": "black",
   "colorValue": "#000"
}]
```
to this:
```sql
INSERT INTO [dbo].[Colors](
	color,
	colorValue
)
VALUES
('red','#f00'),
('green','#0f0'),
('blue','#00f'),
('cyan','#0ff'),
('magenta','#f0f'),
('yellow','#ff0'),
('black','#000');
```
