import React from 'react';

class Login extends React.Component {
  state = {
    email: null,
    password: null
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    });
    console.log(this.state)
  }

  handleClick = (e) => {
    e.preventDefault();
  }

  render(){
    return (
      <div className="container">
        <form>
          <div className="form-group">
            <label htmlFor="email"> Email </label>
            <input type="email" className="form-control" name="email" id="email" onChange={this.handleChange}/>
          </div>
          <div className="form-group">
            <label htmlFor="password"> Password </label>
            <input type="password" className="form-control" name="password" id="password" onChange={this.handleChange}/>
          </div>
          <button type="submit" className="btn btn-primary btn-block" onClick={this.handleClick}>Login</button>
        </form>
      </div>

    )
  }
}

export default Login;