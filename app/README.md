# E-Commerce Market Basket Analysis - Production Application

A production-ready web application that demonstrates advanced data science skills through comprehensive market basket analysis, customer segmentation, and sales forecasting.

## 🚀 Features

### Core Analytics
- **Market Basket Analysis**: Apriori algorithm implementation for finding frequent item sets and association rules
- **Customer Segmentation**: K-means clustering for customer behavior analysis
- **Sales Forecasting**: Random Forest regression for predicting future sales trends
- **Interactive Dashboard**: Real-time visualizations with Plotly.js

### Technical Stack
- **Backend**: Flask (Python)
- **Database**: PostgreSQL with your existing MBA database
- **ML Libraries**: scikit-learn, mlxtend, pandas, numpy
- **Frontend**: Bootstrap 5, JavaScript, Plotly.js
- **Visualization**: Interactive charts and graphs

## 📊 Project Structure

```
app/
├── app.py                 # Main Flask application
├── run.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── models/                # ML model implementations
│   ├── market_basket_analyzer.py
│   ├── customer_segmentation.py
│   └── sales_predictor.py
├── database/              # Database management
│   └── db_manager.py
└── templates/             # HTML templates
    ├── landing.html       # Professional landing page
    └── dashboard.html     # Interactive analytics dashboard
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (your existing MBA database)
- pip or conda

### Installation Steps

1. **Clone/Download the project**
   ```bash
   cd /path/to/your/project
   ```

2. **Install Python dependencies**
   ```bash
   cd app
   pip install -r requirements.txt
   ```

3. **Configure Database Connection**
   - The application is pre-configured to use your existing PostgreSQL database
   - Database: `mba_db`
   - User: `matth`
   - Password: `Delaune.7467`
   - Host: `localhost`
   - Port: `5432`

4. **Start the Application**
   ```bash
   python run.py
   ```

5. **Access the Application**
   - Landing Page: http://localhost:5000
   - Dashboard: http://localhost:5000/dashboard

## 🎯 API Endpoints

### Core Analytics
- `GET /api/stats` - Overall statistics and metrics
- `GET /api/market-basket?min_support=0.01&min_confidence=0.3` - Market basket analysis
- `GET /api/customer-segments` - Customer segmentation results
- `GET /api/sales-forecast?months=3` - Sales forecasting predictions

### Data Analysis
- `GET /api/top-products?limit=20` - Top performing products
- `GET /api/sales-trends` - Sales trends over time
- `GET /api/recommendations/<customer_id>` - Product recommendations

## 📈 Dashboard Features

### Landing Page
- Professional portfolio presentation
- Project overview and technical stack
- Interactive statistics and animations
- Responsive design for all devices

### Analytics Dashboard
- **Real-time Statistics**: Total orders, revenue, products, average order value
- **Sales Trends**: Monthly revenue trends with interactive charts
- **Category Analysis**: Product category performance pie charts
- **Market Basket Analysis**: Association rules with configurable parameters
- **Customer Segmentation**: K-means clustering visualization
- **Sales Forecasting**: ML-powered revenue predictions
- **Top Products**: Best performing products table

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the app directory:
```env
DB_HOST=localhost
DB_NAME=mba_db
DB_USER=matth
DB_PASSWORD=Delaune.7467
DB_PORT=5432
FLASK_DEBUG=True
```

### ML Model Parameters
- **Market Basket Analysis**: Adjustable support and confidence thresholds
- **Customer Segmentation**: 4-cluster K-means with PCA visualization
- **Sales Forecasting**: Random Forest with 100 estimators

## 🎨 Customization

### Styling
- Bootstrap 5 framework with custom CSS variables
- Responsive design with mobile-first approach
- Professional color scheme and typography
- Interactive hover effects and animations

### Charts
- Plotly.js for interactive visualizations
- Real-time data updates
- Responsive chart layouts
- Custom color schemes

## 📊 Business Insights

The application provides actionable business insights:

### Market Basket Analysis
- **Product Associations**: Items frequently bought together
- **Cross-selling Opportunities**: High-confidence association rules
- **Bundle Recommendations**: Strategic product combinations

### Customer Segmentation
- **High-Value Loyal Customers**: Premium retention strategies
- **Regular High AOV Customers**: Frequency improvement campaigns
- **Growing Customers**: Onboarding and engagement
- **New/Infrequent Customers**: Re-engagement campaigns

### Sales Forecasting
- **Revenue Predictions**: ML-powered future sales estimates
- **Trend Analysis**: Seasonal patterns and growth trajectories
- **Performance Metrics**: Model accuracy and confidence intervals

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
1. Set `FLASK_DEBUG=False` in environment
2. Use a production WSGI server like Gunicorn
3. Configure reverse proxy with Nginx
4. Set up SSL certificates for HTTPS

### Example Gunicorn Command
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📱 Responsive Design

- **Mobile-First**: Optimized for all screen sizes
- **Touch-Friendly**: Interactive elements for mobile devices
- **Fast Loading**: Optimized assets and lazy loading
- **Cross-Browser**: Compatible with modern browsers

## 🔒 Security Features

- **Input Validation**: Parameter sanitization and validation
- **Error Handling**: Graceful error management
- **Database Security**: Parameterized queries
- **CORS Configuration**: Cross-origin request handling

## 📈 Performance Optimization

- **Efficient Queries**: Optimized database queries
- **Caching**: Model result caching for better performance
- **Lazy Loading**: On-demand data loading
- **Responsive Charts**: Efficient Plotly.js rendering

## 🎓 Portfolio Value

This project demonstrates:
- **Advanced Data Science**: ML algorithms and statistical analysis
- **Full-Stack Development**: Backend API and frontend dashboard
- **Database Management**: Complex PostgreSQL queries and optimization
- **Business Intelligence**: Actionable insights and recommendations
- **Production Deployment**: Scalable and maintainable code architecture

## 📞 Contact

**Developer**: Kapil Sharma  
**Email**: kapilsharma.24011@gmail.com  
**Project**: E-Commerce Market Basket Analysis  
**Portfolio**: Data Science & Analytics Specialist

---

*This application showcases advanced data science skills through a comprehensive market basket analysis implementation with modern web technologies and production-ready deployment.*

