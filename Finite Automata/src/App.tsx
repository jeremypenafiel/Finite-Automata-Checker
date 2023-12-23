import { useState } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import PDA from "./components/PDA/PDA";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<PDA />} />
          <Route path="/PDA" element={<PDA />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
