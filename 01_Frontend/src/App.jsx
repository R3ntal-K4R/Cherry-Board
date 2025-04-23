import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import BuyListingPage from "./pages/buyListingPage"
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import Landing from './pages/landing'
import Home from './pages/home'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/listing" element={<BuyListingPage />} />
        <Route path="/landing" element={<Landing />} />
      
        
      </Routes>
    </>
  )
}

export default App
