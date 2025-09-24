# squeek 🐿️

**AI-powered squirrel classifier project**

---

## Motivation

This project started as a fun way to explore deep learning while also building something educational and unique: a "Pokedex-style" app for mamals. 
Unfortunately that scoup might be a little bit too big for me right now so atm it'll be just for squirrels.
The idea is to train a model to classify different squirrel (and related species) images, and eventually use it to help people learn more about them.

---

## Current Status

- ✅ **Image scraper built** (using Selenium + BeautifulSoup + Requests).  
- ✅ **Dataset structure created** (images organized by species).  
- 🚧 **Data cleaning in progress** (removing junk/incorrect images).  
- 🚧 **Initial CNN model drafted** (TensorFlow/Keras).  
- ⏳ Training & evaluation planned once dataset is cleaned.  

---

## Tech Stack

- **Python**  
- **TensorFlow / Keras** (for CNN model)  
- **Selenium, BeautifulSoup, Requests** (for scraping)  
- **Pandas / NumPy / Matplotlib / Seaborn** (for analysis & visualization)  

---

## Project Structure

```
squeek/
├── Data/                # folders of species → images
├── DataDownload.py      # scraper script
├── model.py             # CNN architecture + training logic (draft)
└── README.md
```

---

## Getting Started

1. Clone the repo:  
   ```bash
   git clone https://github.com/Nameless0612/squeek.git
   cd squeek
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have **ChromeDriver** installed and update the path in `DataDownload.py`.

4. Run the scraper:  
   ```bash
   python DataDownload.py
   ```

5. Clean the dataset manually (remove bad/duplicate images).

6. (Soon) Train the model:  
   ```bash
   python model.py
   ```

---

## Next Steps

- Finish dataset cleaning.  
- Train and evaluate the CNN.  
- Improve dataset quality and balance.  
- Expand into an interactive app in the future.  

---


## Data Disclaimer
The dataset of squirrel images is **not included** in this repository due to copyright restrictions.  
Images were collected using a custom scraper from Google Search for research and educational purposes only.  
If you wish to replicate the dataset, please use the provided scraper script to gather your own copy.

