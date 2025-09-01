import React, { useState } from 'react'
import { useAuth } from '../auth'
import { useNavigate } from 'react-router-dom'

export default function Register() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [err, setErr] = useState('')
  const { register } = useAuth()
  const nav = useNavigate()

  async function onSubmit(e) {
    e.preventDefault()
    try {
      await register(username, password)
      nav('/start')
    } catch (e) {
      setErr(e.message)
    }
  }

  return (
    <div className="container">
      <form onSubmit={onSubmit} className="card form" style={{maxWidth:480, margin:'12px auto'}}>
        <h2>Register</h2>
        {err && <div style={{color:'red'}}>{String(err)}</div>}
        <input className="input" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
        <input className="input" placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} required />
        <div style={{display:'flex', gap:8}}>
          <button className="btn btn-primary" type="submit">Create Account</button>
        </div>
      </form>
    </div>
  )
}
