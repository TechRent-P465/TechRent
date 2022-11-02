import axios from 'axios'

const path = 'http://127.0.0.1:5000'

export function postNewItem(item, jwt) {
  return axios.post(`${path}/items`, item, {
    headers: { Authorization: `Bearer: ${jwt}` }
  })
}

export function authenticate(userData) {
  return axios.post(`${path}/login`, userData)
}

export function register(userData) {
  return axios.post(`${path}/register`, userData)
}
