import React from 'react';
import axios from 'axios';

class Boards extends React.Component {
  state = {
    boards: [
      {id: 1, title: "psadasdgadsg", archived: false}
    ]
  }

  componentDidMount(){
    const url = '/boards/';
    const token = localStorage.getItem('access_token');
    const headers = {
      Authorization: "Bearer  " + token
    }

    axios.get(url, {headers})
    .then(res =>{
      let response = res.data;
      console.log(response[0])
      let boards = [...this.state.boards, response[0]];
      this.setState({
        boards: boards
      });
      console.log(this.state)
    })
    .catch(res => console.log(res));
  }

  render() {
    const boards = this.state.boards;
    const boardList = boards.map(board => {
      console.log(boards)
      return (
        <div className="card" key={board.slug}>
          <div className="card-body">
            <div className="card-title">{board.title}</div>
          </div>
        </div>
      )
    });
    return (
      <div className="container">
        {boardList}
        <div className="card">
          <div className="card-body">
            <div className="card-title">Create Board</div>
          </div>
        </div>
      </div>
    )
  }
}

export default Boards;