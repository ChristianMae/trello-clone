import React from 'react';

class Cards extends React.Component {
    state = {
        cards : [
            {id: 1, name: "Test Board"},
            {id: 2, name: "Test Board"}
        ]
    }
    render(){
        const cards = this.state.cards.map(card => {
            return(
                <li class="list-group-item">{ card.name }</li>
            )
        })
        return(
           <ul class="list-group">
               { cards }
           </ul>
        )
    }
}

export default Cards;