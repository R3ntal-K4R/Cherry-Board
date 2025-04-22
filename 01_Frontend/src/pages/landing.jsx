import React from 'react';
import styles from '../Landing.module.css';

export default function Landing() {
  return (
    <div className={styles.landingPage}>
      <header className={styles.header}>
        <div className={styles.logo}>Our Logo</div>
        <div className={styles.authButtons}>
          <button className={styles.signin}>Sign In</button>
          <button className={styles.signup}>Sign Up</button>
        </div>
      </header>

      <main className={styles.main}>
        <section className={styles.hero}>
          <h1>
            Keyboards Designed For <span className={styles.highlight}>You</span>
          </h1>
          <button className={styles.getStarted}>Get started</button>
        </section>

        <section className={styles.keyboardImage}>
          <img src="keyboard_picture.webp" alt="Custom Keyboard" />
        </section>
      </main>
    </div>
  );
}
