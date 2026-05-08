import csv
import random

years = [2023, 2024, 2025, 2026]
markets = {
    'forex': {'base': 3000, 'win': 80, 'setups': 20, 'badge': 'Pips'},
    'stocks': {'base': 130, 'win': 72, 'setups': 17, 'badge': 'Ideas'},
    'crypto': {'base': 12, 'win': 70, 'setups': 19, 'badge': '% Gain'},
    'commodity': {'base': 270, 'win': 78, 'setups': 14, 'badge': 'Points'}
}
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

with open('Performance_Data_Master.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'Market', 'Month', 'Value', 'WinRate', 'Setups', 'Badge'])
    
    for y in years:
        for mkt, data in markets.items():
            # Add some slight variation year over year
            y_factor = 1.0 + (y - 2023) * 0.05
            for i, month in enumerate(months):
                # We'll use the hardcoded 2025 data from the JS file for 2025 to match the defaults
                if y == 2025 and mkt == 'forex':
                    val = [3200,2900,3800,2700,3500,3100,4000,2800,3600,3300,3900,3100][i]
                    win = [82,78,85,75,83,80,88,76,84,81,86,80][i]
                    setup = [22,20,24,19,21,23,26,20,23,22,25,21][i]
                elif y == 2025 and mkt == 'stocks':
                    val = [140,125,160,110,145,132,172,118,155,138,168,130][i]
                    win = [75,70,78,68,76,72,80,69,77,73,79,71][i]
                    setup = [18,16,20,14,17,19,22,15,18,17,21,16][i]
                elif y == 2025 and mkt == 'crypto':
                    val = [12,9,15,8,13,11,17,9,14,12,16,10][i]
                    win = [72,68,76,65,73,70,78,66,74,71,77,69][i]
                    setup = [20,18,22,16,19,21,24,17,20,19,23,18][i]
                elif y == 2025 and mkt == 'commodity':
                    val = [280,240,320,210,295,265,345,225,305,270,330,255][i]
                    win = [79,74,82,71,80,77,84,72,81,78,83,75][i]
                    setup = [14,12,16,10,13,15,18,11,14,13,17,12][i]
                else:
                    # Randomize slightly around the base for other years
                    val = int(data['base'] * y_factor * random.uniform(0.85, 1.15))
                    win = int(data['win'] * random.uniform(0.9, 1.05))
                    setup = int(data['setups'] * random.uniform(0.8, 1.2))
                    
                writer.writerow([y, mkt, month, val, win, setup, data['badge']])

print("Generated Performance_Data_Master.csv successfully.")
