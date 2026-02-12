# SoftCable  
A modern USB‑C cable diagnostic suite with a clean CustomTkinter GUI.

SoftCable analyzes USB‑C ports, cables, power delivery, data speeds, lane mapping, and cable identity to give you a complete picture of your cable’s capabilities and stability.  
Version 2.0 introduces a fully redesigned interface with a modern tabbed layout and real‑time power monitoring dashboard.

---

## 🚀 Features

### 🔌 USB‑C Port & Cable Detection
SoftCable detects:
- USB‑C port identity
- Partner device
- Power Delivery support
- PD profiles
- Voltage, current, and wattage

---

### 🧠 Smart Diagnostics
SoftCable includes:
- Data speed testing (write/read)
- Stability testing with variance scoring
- Live power monitoring dashboard
- USB‑C lane visualization (Phase 8)
- Raw system data from `/sys/class/typec`
- Cable identity & e‑marker decoding

---

## 🎨 Modern CustomTkinter GUI (v2.0.0)
Version 2.0 introduces a complete UI overhaul:

- Modern tabbed interface  
- Dark/Light mode toggle  
- Read‑only scrollable textboxes  
- Clean vertical power dashboard  
- Improved spacing and typography  
- Consistent design with DistroMatch v2.0  

Tabs include:
- Overview  
- Lanes  
- Data Test  
- Power Test  
- Stability Test  
- Raw Data  
- Cable Identity  
- Export  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SoftCable.git
cd SoftCable
