import React from 'react';

class BoardActionsPanel extends React.Component {
    render() {
        return(
            <nav className="nav">
                <div className="nav-item">
                    <a className="nav-link">Board Name</a>
                </div>
                <div className="nav-item">
                    <a className="nav-link">Members</a>
                </div>
                <div className="nav-item">
                   <button className="btn btn-info">Invite</button>
                </div>
            </nav>
        )
    }
}

export default BoardActionsPanel;