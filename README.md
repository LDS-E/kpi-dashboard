# KPI Dashboard

The KPI Dashboard is a web application designed to provide real-time insights for businesses, specifically within the pharmaceutical industry, and their advisory boards. It offers interactive, data-driven visualizations that help decision-makers efficiently monitor key performance indicators (KPIs) related to sales, market share, and other relevant metrics.

## 🚀 Features

- **Real-time data visualization of KPIs:** Gain immediate insights into sales performance, market share, and other critical metrics.
- **Interactive and user-friendly charts:** Explore data with customizable charts and visualizations to support data-driven decision-making.
- **Customizable dashboard:** Tailor the dashboard to specific user roles and needs, providing relevant information at a glance.
- **JWT-based authentication:** Secure access to sensitive data with robust authentication.
- **Scalable architecture:** Handle large datasets efficiently to accommodate growing data needs.
- **Power BI integration:** Seamlessly integrate with Power BI for advanced analytics and reporting capabilities.

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python) - A high-performance API framework for building modern web applications.
- **Database:** [PostgreSQL](https://www.postgresql.org/) - A robust and scalable relational database to store and manage data.
- **Frontend:** (Planned for future versions) [React](https://reactjs.org/) with [Next.js](https://nextjs.org/) - Frameworks for building dynamic, server-side rendered (SSR) React applications.
- **Authentication:** JWT-based authentication - A token-based authentication system for secure user access and session management.
- **Data Visualization:** (Planned for future versions) [Recharts](https://recharts.org/) or [Chart.js](https://www.chartjs.org/) - Interactive and customizable chart libraries to visualize KPI data.

## ⚙️ Installation

### Prerequisites

- Python 3.12.7
- PostgreSQL
- (For development) A virtual environment is recommended

### Steps

1. Clone the repository.
2. Install the required Python packages: `pip install -r requirements.txt`
3. Configure the database connection in the `.env` file.
4. Run the FastAPI application: `uvicorn main:app --reload`

## 👥 Authors

Developed by: LDS-E
