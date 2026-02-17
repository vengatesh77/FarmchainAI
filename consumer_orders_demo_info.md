# Consumer Orders Dashboard - Demo & Technical Info

This document provide the necessary data and information to demo the new "My Orders" feature.

## 🗄️ MySQL Table Structure & Sample Data

Run these queries in your MySQL database to set up the tables and add sample data.

```sql
-- 1. Create orders table (Spring Data JPA will auto-create this, but here is the manual SQL for reference)
CREATE TABLE IF NOT EXISTS orders (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    consumer_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    retailer_id BIGINT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    delivery_status VARCHAR(50) DEFAULT 'PENDING',
    quantity DOUBLE DEFAULT 1.0,
    total_price DOUBLE DEFAULT 0.0,
    FOREIGN KEY (consumer_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (retailer_id) REFERENCES users(id)
);

-- 2. Insert Sample Data
-- Note: Replace consumer_id (2), product_id (1), and retailer_id (3) with actual IDs from your database if they differ.
INSERT INTO orders (consumer_id, product_id, retailer_id, order_date, delivery_status, quantity, totalPrice)
VALUES 
(2, 1, 3, NOW(), 'DELIVERED', 10.0, 500.0),
(2, 1, 3, DATE_SUB(NOW(), INTERVAL 2 DAY), 'IN_TRANSIT', 5.0, 250.0),
(2, 1, 3, DATE_SUB(NOW(), INTERVAL 5 DAY), 'PENDING', 2.0, 100.0);
```

## 🌐 Sample JSON Response (GET /api/orders/my-orders)

```json
[
  {
    "id": 1,
    "consumer": {
      "id": 2,
      "username": "consumer_user",
      "fullName": "Jane Doe",
      "role": "CONSUMER"
    },
    "product": {
      "id": 1,
      "name": "Organic Tomatoes",
      "type": "CROP",
      "qualityGrade": "A",
      "imageUrl": "https://example.com/tomatoes.jpg",
      "farmer": {
        "fullName": "John Farmer"
      }
    },
    "retailer": {
      "id": 3,
      "fullName": "Green Grocers",
      "role": "RETAILER"
    },
    "orderDate": "2026-02-16T12:00:00",
    "deliveryStatus": "DELIVERED",
    "quantity": 10.0,
    "totalPrice": 500.0
  }
]
```

## 🎤 Viva Explanation (Short & Concise)

**1. How does the dashboard load orders automatically?**
"The system uses **Spring Security** to extract the logged-in user's identity from the **JWT token**. When the consumer visits the dashboard, the Angular frontend calls the `/api/orders/my-orders` endpoint without passing any ID. The backend identifies the user server-side, ensuring security and a seamless UX."

**2. How is the data structured?**
"We implemented a **Relational Mapping (ORM)** using Hibernate. The `Order` entity joins the `Product`, `User` (Farmer/Consumer/Retailer) tables using `@ManyToOne` relationships. This allows us to display full journey details, like farmer name and AI quality, directly in the order card."

**3. How is the UI optimized?**
"We used a **Card-Based Layout** with dynamic CSS classes for status badges. Summary cards provide an instant overview of order statistics using Angular's reactive data binding (`*ngIf` and `*ngFor`)."

## 🚀 How to Run the Demo
1. Restart the Backend (`mvn spring-boot:run`).
2. Login as a user with the **CONSUMER** role.
3. You will be automatically redirected to `/consumer/my-orders`.
4. Click **"View Journey Details"** on any card to see the full transparency timeline!
