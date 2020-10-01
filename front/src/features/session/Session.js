import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  initSession,
  selectSession,
} from './sessionSlice';
import styles from './Session.module.css';
import Button from "@material-ui/core/Button";
import {Redirect} from "react-router-dom";

function loginButton(dispatch) {
  return (
      <Button variant="contained" color="primary"
        className={styles.button}
        onClick={() => dispatch(initSession())}
      >
        Login
      </Button>
  );
}

export function Session() {
  const user = useSelector(selectSession);
  const dispatch = useDispatch();
  return user ? <Redirect to={'/home'} /> : loginButton(dispatch);
}
