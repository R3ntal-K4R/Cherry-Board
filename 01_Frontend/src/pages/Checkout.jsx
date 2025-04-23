import React from "react";
import { useNavigate } from 'react-router-dom';


export default function CheckoutPage() {
  const navigate = useNavigate();

  return (
    <div style={{ minHeight: "100vh", backgroundColor: "#fef2f2", display: "flex", justifyContent: "center", alignItems: "center", padding: "2rem" }}>
      <div style={{ width: "100%", maxWidth: "600px", backgroundColor: "#fff", borderRadius: "1rem", boxShadow: "0 10px 20px rgba(0,0,0,0.1)", padding: "2rem" }}>
        <h1 style={{ fontSize: "1.75rem", fontWeight: "bold", color: "#b91c1c", textAlign: "center", marginBottom: "1.5rem" }}>
          Cherry Board Checkout
        </h1>
        <form className="checkout-form" style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          <div>
            <label htmlFor="name">Full Name</label>
            <input id="name" placeholder="Jane Doe" style={inputStyle} />
          </div>
          <div>
            <label htmlFor="email">Email</label>
            <input id="email" type="email" placeholder="jane@example.com" style={inputStyle} />
          </div>
          <div>
            <label htmlFor="address">Shipping Address</label>
            <input id="address" placeholder="123 Cherry Lane" style={inputStyle} />
          </div>
          <div>
            <label htmlFor="card">Card Number</label>
            <input id="card" type="text" placeholder="1234 5678 9012 3456" style={inputStyle} />
          </div>
          <div style={{ display: "flex", gap: "1rem" }}>
            <div style={{ flex: 1 }}>
              <label htmlFor="exp">Exp Date</label>
              <input id="exp" placeholder="MM/YY" style={inputStyle} />
            </div>
            <div style={{ flex: 1 }}>
              <label htmlFor="cvc">CVC</label>
              <input id="cvc" type="text" placeholder="123" style={inputStyle} />
            </div>
          </div>
          <button type="button"
           onClick={() => navigate('/thankyou')} 
           style={{ backgroundColor: "#dc2626", color: "white", padding: "0.75rem", border: "none", borderRadius: "0.5rem", fontWeight: "bold", cursor: "pointer" }}>
            Place Order
          </button>
        </form>
      </div>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "0.5rem",
  marginTop: "0.25rem",
  border: "1px solid #d1d5db",
  borderRadius: "0.5rem",
  fontSize: "1rem"
};
