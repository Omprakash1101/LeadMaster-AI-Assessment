import React, { useEffect, useMemo, useState } from 'react'
import { useAuth } from '../auth'
import { api } from '../api'
import { useNavigate } from 'react-router-dom'
import Timer from '../components/Timer'

export default function Exam() {
  const { user } = useAuth()
  const nav = useNavigate()
  const saved = useMemo(() => JSON.parse(sessionStorage.getItem('exam') || 'null'), [])
  const [idx, setIdx] = useState(0)
  const [answers, setAnswers] = useState({})
  const [err, setErr] = useState('')

  useEffect(() => { if (!saved) nav('/start') }, [saved, nav])
  if (!saved) return null

  const { exam, questions } = saved
  const q = questions[idx]
  const duration = exam.duration_seconds || 1800

  function setAns(qid, val) {
    setAnswers(a => ({ ...a, [qid]: val }))
  }

  async function submit() {
    try {
      const data = await api(`/exam/${exam.id}/submit/`, {
        method: 'POST',
        token: user.token,
        body: { answers }
      })
      sessionStorage.removeItem('exam')
      sessionStorage.setItem('result', JSON.stringify(data))
      nav('/result')
    } catch (e) {
      setErr(e.message)
    }
  }

  function onExpire() {
    submit()
  }

  return (
    <div className="container">
      <div className="exam-header">
        <h2>Exam</h2>
        <Timer seconds={duration} onExpire={onExpire} />
      </div>

      {err && <div style={{color:'red'}}>{String(err)}</div>}

      <div className="question-card card">
        <div className="question-heading">Q{idx + 1}. {q.text}</div>
        <div className="options">
          {[['A', q.option_a], ['B', q.option_b], ['C', q.option_c], ['D', q.option_d]].map(([key, label]) => (
            <label key={key} className="option">
              <input
                type="radio"
                name={`q-${q.id}`}
                checked={(answers[q.id] || '') === key}
                onChange={() => setAns(q.id, key)}
              />
              <span><strong>{key}.</strong> {label}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="controls">
        <div className="left">
          <button className="btn btn-ghost" disabled={idx === 0} onClick={() => setIdx(i => i - 1)}>Previous</button>
        </div>
        <div className="right">
          <button className="btn btn-ghost" disabled={idx === questions.length - 1} onClick={() => setIdx(i => i + 1)}>Next</button>
          <button className="btn btn-primary" onClick={submit}>Submit</button>
        </div>
      </div>
    </div>
  )
}
