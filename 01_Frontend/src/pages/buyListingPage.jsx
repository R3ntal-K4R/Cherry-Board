import React from 'react';
import { useNavigate } from 'react-router-dom'; // <-- import this
import styles from '../BuyListingPage.module.css';

export default function BuyListingPage() {
  const navigate = useNavigate(); // <-- create the navigate function
  const dummyItems = new Array(12).fill({
    name: "Name Of Keyboard",
    price: "Price",
  });

  return (
    <div className={styles.buyListingPage}>
      <header className={styles.header}>
        <div className={styles.logo}>Our Logo</div>
        <div className={styles.authButtons}>
          <button className={styles.btn}>View Cart</button>
          <button className={styles.btn}>Sign Out</button>
        </div>
      </header>

      <h1 className={styles.title}>Active Listings -</h1>

      <div className={styles.listingGrid}>
        {dummyItems.map((item, index) => (
          <div key={index} className={styles.card}>
            <div className={styles.imagePlaceholder}>
              <img src="https://via.placeholder.com/100" alt="keyboard preview" />
            </div>
            <div className={styles.details}>
              <span>{item.name}</span>
              <span className={styles.price}>{item.price}</span>
            </div>
            <button 
             className={styles.addButton} 
             onClick={() => navigate('/checkout')}
             >
              Purchase
             
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}