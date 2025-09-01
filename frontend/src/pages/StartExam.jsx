import React, { useState } from 'react'
import { useAuth } from '../auth'
import { api } from '../api'
import { useNavigate } from 'react-router-dom'

export default function StartExam() {
  const { user } = useAuth()
  const [count, setCount] = useState(5)
  const [err, setErr] = useState('')
  const nav = useNavigate()

  async function start() {
    try {
      const data = await api('/exam/start/', {
        method: 'POST',
        token: user.token,
        body: { count }
      })
      sessionStorage.setItem('exam', JSON.stringify(data))
      nav('/exam')
    } catch (e) {
      setErr(e.message)
    }
  }

  return (
    <div className="container">
      <div className="card" style={{maxWidth:640, margin:'12px auto'}}>
        <h2>Start Exam</h2>
        {err && <div style={{color:'red'}}>{String(err)}</div>}
        <label>
          Number of Questions:
          <input className="input" type="number" min="1" value={count} onChange={e => setCount(parseInt(e.target.value || '1'))} />
        </label>
        <div style={{marginTop:12}}>
          <button className="btn btn-primary" onClick={start}>Start</button>
        </div>
      </div>
    </div>
  )
}
