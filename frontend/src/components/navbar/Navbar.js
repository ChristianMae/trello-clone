import React from 'react';

class Navbar extends React.Component {
    render(){
        return (
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <a className="navbar-brand">Trello Clone</a>
                <ul className="navbar-nav mr-auto">
                </ul>
                <ul className="navbar-nav">
                    <li className="nav-item">
                        <a className="nav-link">Sign up</a>
                        </li>
                    <li className="nav-item">
                        <a className="nav-link">Sign in</a>
                    </li>
                </ul>
            </nav>
        )
    }

}

export default Navbar;