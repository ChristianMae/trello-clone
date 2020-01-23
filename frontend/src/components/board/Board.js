import React from 'react';
import BoardActionsPanel from './BoardActionsPanel.js';
import Lists from '../list/Lists.js';

class Board extends React.Component {
    render() {
        return (
            <div>
                <BoardActionsPanel />
                <Lists />
            </div>
        )

    }
}

export default Board;