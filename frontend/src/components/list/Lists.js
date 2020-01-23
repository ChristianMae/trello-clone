import React from 'react';
import Cards from '../card/Cards.js';

class Lists extends React.Component {
    state = {
        lists : [
            {id: 1, name: "Test Board"},
            {id: 2, name: "Test Board"}
        ]
    }

    render() {
        const lists = this.state.lists.map(list => {
            return (
                <div className="card">
                    <div className="card-body">{list.name}</div>
                    <div className="card-footer">
                        <Cards />
                    </div>
                </div>
            )
        });

        return(
            <div className="card-group">
                {lists}
                <div className="card">
                    <div className="card-body">
                        <form>
                            <div className="form-group">
                                <input type="text" name="name" id="name" />
                            </div>
                            <button type="button" className="btn btn-primary">Add List</button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default Lists;