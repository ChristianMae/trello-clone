import React from 'react';
import Navbar from './components/navbar/Navbar.js';
import Login from './components/forms/Login.js';
import Signup from './components/forms/Signup.js';
import Boards from './components/board/Boards.js';
import Board from './components/board/Board.js';


function App() {
  return (
    <div className="App">
      <Navbar />
      {/* <Login /> */}
      <Signup />
      {/* <Boards /> */}
      {/* <Board /> */}
    </div>
  );
}

export default App;
