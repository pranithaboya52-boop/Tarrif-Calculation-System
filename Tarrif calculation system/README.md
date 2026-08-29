# Tariff Calculation System

## Description
A Python-based electricity tariff calculation system that calculates the electricity bill based on energy consumption using predefined slab rates.

## Features
- Calculates energy consumption
- Slab-based tariff calculation
- Fixed charge calculation
- Total electricity bill calculation
- Python testbench using unittest
- Simulation output

## Software Requirements
- Python 3.x
- VS Code

## Tariff Slabs

| Consumption | Rate |
|------------|------|
| 0–100 units | ₹2/unit |
| 101–200 units | ₹3/unit |
| 201–500 units | ₹5/unit |
| Above 500 units | ₹7/unit |

Fixed Charge = ₹50

## Project Files
- `tariff_calculation.py` - Main program
- `test_tariff_calculation.py` - Testbench
- `expected_output.txt` - Expected results
- `simulation/simulation_output.txt` - Simulation results

## How to Run

Run the main program:

```bash
python tariff_calculation.py