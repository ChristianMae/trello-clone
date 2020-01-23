import React from 'react';

class Boards extends React.Component {
    state = {
        boards: [
            {id: 1, name: "Test Board"},
            {id: 2, name: "Test Board"}
        ]
    }

    render() {
        const boards = this.state.boards;
        const boardList = boards.map(board => {
            return (
                <div className="card">
                    <div className="card-body">
                        <div className="card-title">{board.name}</div>
                    </div>
                </div>
            )
        })
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