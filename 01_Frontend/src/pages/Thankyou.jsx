import React from 'react';

export default function ThankYouPage() {
  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-r from-purple-500 to-pink-500 text-white">
      <div className="text-center p-8 bg-white bg-opacity-10 backdrop-blur-md rounded-2xl shadow-2xl">
        <h1 className="text-4xl font-bold mb-4">Thank You!</h1>
        <p className="text-lg">We appreciate your feedback and will get back to you shortly.</p>
        <button className="mt-6 px-6 py-2 bg-white text-purple-600 font-semibold rounded-full shadow hover:shadow-lg transition">Go Home</button>
      </div>
    </div>
  );
}
