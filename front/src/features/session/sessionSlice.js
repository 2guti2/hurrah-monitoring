import { createSlice } from '@reduxjs/toolkit';
import socketIOClient from "socket.io-client";
import axios from 'axios';


const localStorageSessionKey = 'session';

export const sessionSlice = createSlice({
  name: 'session',
  initialState: JSON.parse(localStorage.getItem(localStorageSessionKey)),
  reducers: {
    login: (state, action) => {
      return {
        ...state,
        ...action.payload
      };
    },
    destroySession: () => {
      localStorage.removeItem(localStorageSessionKey);
      return null;
    }
  },
});

export const { login, destroySession } = sessionSlice.actions;

export const initSession = () => dispatch => {
  // const socket = socketIOClient('https://localhost:5000');
  // const clientId = guid();
  //
  // socket.on('connect', function () {
  //   socket.emit('client::user::connected', {id: clientId});
  //
  //   socket.on(`server::redirect::${clientId}`, function (redirectUrl) {
  //     window.open(redirectUrl);
  //   });
  //
  //   socket.on(`server::user::logged_in::${clientId}`, (payload) => {
  //     localStorage.setItem(localStorageSessionKey, JSON.stringify(payload));
  //     dispatch(login(payload));
  //     socket.close();
  //   })
  // });
  axios.post(`http://localhost:5000/api/sessions`, {username: 'admin', password: 'Passw0rd!'}).then(res => {
    const user = {
      token: res.data.token,
      name: 'admin'
    };
    localStorage.setItem(localStorageSessionKey, JSON.stringify(user));
    dispatch(login(user))
  })
};

function guid() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,c => {
    const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r && 0x3 | 0x8);
    return v.toString(16);
  });
}

export const selectSession = state => state.session;

export default sessionSlice.reducer;
