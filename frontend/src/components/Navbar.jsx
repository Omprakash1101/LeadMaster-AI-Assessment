import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../auth'

export default function Navbar() {
  const { user, logout } = useAuth()
  return (
    <header className="navbar">
      <div className="container" style={{display:'flex', alignItems:'center', justifyContent:'space-between', gap:12}}>
        <div style={{display:'flex', alignItems:'center', gap:12}}>
          <div className="brand">Omi</div>
          <nav className="nav-links" aria-label="Main navigation">
            <Link to="/">Home</Link>
            {!user && <>
              <Link to="/register">Register</Link>
              <Link to="/login">Login</Link>
            </>}
            {user && <>
              <Link to="/start">Start Exam</Link>
            </>}
          </nav>
        </div>

        <div>
          {user ? <button className="btn btn-ghost" onClick={logout}>Logout ({user.username})</button>
               : null}
        </div>
      </div>
    </header>
  )
}
