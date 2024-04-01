### **Problem Statement:**

You are tasked with building a Django application that aggregates information from two different e-commerce platforms: one platform provides information about electronic devices, including product name, brand, price, and warranty period, while the other platform provides information about clothing items, including product name, brand, price, size, and color. Your task is to create a Django application that normalizes this data into a unified model and provides a feature-rich web interface to view, search, and manage the aggregated product information.

<strong>
💡 Please use Django MVT stack with Django’s Jinja based templates. If you would like to use Django REST with a React.js frontend component, you may do so as well.

</strong>

### **Features:**

- **Django Model Creation**: Define and create your necessary models to unify and normalize the data at your own discretion
- **Data Normalization**: Implement a mechanism to fetch data from the two e-commerce platforms and normalize it into your common model. You can use fixtures or create a mock api using the json data structures provided below.
- **Web Interface Development**: Develop a user-friendly web interface to display the aggregated product information. This interface should allow users to view a list of all products along with their attributes.
- **Search Functionality**: Implement search functionality within the web interface to enable users to filter products based on various attributes such as name, brand, price range, warranty period, size, and color. This could involve incorporating Django's built-in filtering capabilities or developing custom search functionality.
- **Product Addition**: Enable users to add new products through the web interface and persist them to the database. This feature should include form validation to ensure data integrity.
- **Scaling**: Implement the necessary measures on the database, backend and frontend to ensure that it could support a system with millions of rows.

### Testing your code

- **Insertion**: Please also add a mechanism to bulk create products of both types. Use this mechansim to generate 50,000 instances of each product type, and test the scalability of the database and application layer

### Submission

- Please submit the following
    - Zip file containing your code (make sure to include the sqllite database file with the data you created to test in the insertion step above)
    - A 5 minute video demonstrating the code working. Make sure to explain the decisions you made when designing your models and views, and demo the searching functionality as well as adding a product to the system.

### **Example Datasets:**

**Example Dataset for Electronic Devices:**

```jsx
[
  {
    "name": "Smartphone X",
    "brand": "Brand A",
    "price": 599.99,
    "warranty_period": 12
  },
  {
    "name": "Laptop Y",
    "brand": "Brand B",
    "price": 1299.99,
    "warranty_period": 24
  },
  {
    "name": "Tablet Z",
    "brand": "Brand C",
    "price": 349.99,
    "warranty_period": 12
  }
]

```

**Example Dataset for Clothing Items:**
```jsx

[
  {
    "name": "T-Shirt A",
    "brand": "Brand X",
    "price": 19.99,
    "size": "M",
    "color": "Blue"
  },
  {
    "name": "Jeans B",
    "brand": "Brand Y",
    "price": 39.99,
    "size": "32",
    "color": "Black"
  },
  {
    "name": "Dress C",
    "brand": "Brand Z",
    "price": 49.99,
    "size": "S",
    "color": "Red"
  }
]

```
