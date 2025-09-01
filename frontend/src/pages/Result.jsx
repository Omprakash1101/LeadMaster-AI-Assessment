import React, { useMemo } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Result() {
  const nav = useNavigate()
  const result = useMemo(() => JSON.parse(sessionStorage.getItem('result') || 'null'), [])

  if (!result) return (
    <div className="container">
      <div className="card" style={{maxWidth:480, margin:'12px auto'}}>
        <p>No result found.</p>
        <button className="btn btn-primary" onClick={() => nav('/start')}>Go to Start</button>
      </div>
    </div>
  )

  return (
    <div className="container">
      <div className="card result-box" style={{maxWidth:640, margin:'12px auto'}}>
        <h2>Result</h2>
        <div className="result-score">Score: {result.score}</div>
        <div style={{marginTop:12}}>
          <button className="btn btn-primary" onClick={() => nav('/start')}>Take Another Exam</button>
        </div>
      </div>
    </div>
  )
}
