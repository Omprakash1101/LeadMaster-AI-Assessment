import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Navbar from './components/Navbar'
import Register from './pages/Register'
import Login from './pages/Login'
import StartExam from './pages/StartExam'
import Exam from './pages/Exam'
import Result from './pages/Result'

function Home() {
  return (
    <div className="container" style={{ maxWidth: 720, margin: '24px auto' }}>
    <div className="card" style={{ padding: 24, textAlign: 'center' }}>
      <h2>Omi Student Exam</h2>
      <div style={{padding:12}}>Register or Login to start your exam.</div>
      <div style={{marginTop:12}}>
      <Link to="/start" className="btn btn-primary">Start Exam</Link>
      </div>
    </div>
    </div>
  )
}

export default function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/start" element={<StartExam />} />
        <Route path="/exam" element={<Exam />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </>
  )
}
