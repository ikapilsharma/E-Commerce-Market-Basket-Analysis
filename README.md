# E-Commerce Market Basket Analysis

A comprehensive E-Commerce analytics platform with Market Basket Analysis, Customer Segmentation, RFM Analysis, and Sales Forecasting.

## 🚀 Quick Start

### Deploy to Render (Recommended)

1. **Fork this repository**
2. **Connect to Render**
3. **Create Web Service**
4. **Set Start Command:** `python standalone_demo.py`
5. **Deploy!**

**Live Demo:** [https://e-commerce-market-basket-analysis.onrender.com](https://e-commerce-market-basket-analysis.onrender.com)

## 📊 Features

- **Market Basket Analysis** - Product association rules and frequent itemsets
- **Customer Segmentation** - RFM analysis and clustering
- **Sales Forecasting** - Predictive analytics for revenue and orders
- **Cohort Analysis** - Customer retention tracking
- **Executive Dashboard** - Business intelligence insights

## 🛠️ Technologies

- **Backend:** Flask, Python
- **Analytics:** Pandas, NumPy, Scikit-learn
- **Visualization:** Plotly, Matplotlib
- **Database:** PostgreSQL (optional)
- **Deployment:** Render

## 📁 Project Structure

```
├── standalone_demo.py          # Main demo application (no database required)
├── app/                        # Core application files
│   ├── app.py                 # Main Flask application
│   ├── run.py                 # Application runner
│   ├── config.py              # Configuration
│   ├── database/              # Database management
│   ├── models/                # Analytics models
│   └── templates/             # HTML templates
├── data/                      # Sample data and results
├── scripts/                   # Database setup scripts
├── notebooks/                 # Jupyter notebooks for analysis
└── requirements.txt           # Python dependencies
```

## 🎯 Usage

### Demo Mode (No Database Required)
```bash
python standalone_demo.py
```

### Full Mode (With Database)
```bash
python app/run.py
```

## 📈 Sample Data

The demo includes realistic e-commerce data:
- **119,764 orders** across multiple channels
- **$77.5M revenue** with detailed analytics
- **9,443 customers** with segmentation
- **Product associations** and recommendations

## 🔗 API Endpoints

- `/api/stats` - Overall statistics
- `/api/market-basket` - Association rules and itemsets
- `/api/customer-segments` - Customer clustering results
- `/api/sales-forecast` - Revenue and order predictions
- `/api/top-products` - Best performing products
- `/api/rfm-analysis` - RFM customer segmentation
- `/api/cohort-analysis` - Customer retention analysis

## 📊 Dashboards

- **Landing Page** - Executive overview
- **Analytics Dashboard** - Interactive visualizations
- **Advanced Dashboard** - Comprehensive business intelligence

## 🚀 Deployment

### Render (Recommended)
1. Connect GitHub repository
2. Set Start Command: `python standalone_demo.py`
3. Deploy automatically

### Local Development
```bash
pip install -r requirements.txt
python standalone_demo.py
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Built with ❤️ for E-Commerce Analytics**