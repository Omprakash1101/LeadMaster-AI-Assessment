import React, { createContext, useContext, useState } from 'react'
import { api } from './api'

const AuthCtx = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const token = localStorage.getItem('token')
    const username = localStorage.getItem('username')
    return token ? { username, token } : null
  })

  async function register(username, password) {
    await api('/auth/register/', { method: 'POST', body: { username, password } })
    return login(username, password)
  }

  async function login(username, password) {
    const data = await api('/auth/login/', { method: 'POST', body: { username, password } })
    const token = data.access
    localStorage.setItem('token', token)
    localStorage.setItem('username', username)
    setUser({ username, token })
  }

  function logout() {
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    setUser(null)
  }

  return <AuthCtx.Provider value={{ user, register, login, logout }}>{children}</AuthCtx.Provider>
}

export function useAuth() {
  return useContext(AuthCtx)
}
