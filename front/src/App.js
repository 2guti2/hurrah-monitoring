import React from 'react';
import { Session } from './features/session/Session';
import { Home } from './features/home/Home'
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import {PrivateRoute} from "./PrivateRoute";
import {Profile} from "./features/profile/Profile";

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/login" component={Session} />
          <PrivateRoute path="/profile" component={Profile} />
          <PrivateRoute path="/" component={Home} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
