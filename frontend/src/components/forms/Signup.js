import React from 'react';
import axios from 'axios';

class Signup extends React.Component {
    state = {
      name: null,
      email: null,
      password: null,
      email_errorMsg: null,
      name_errorMsg: null,
      password_errorMsg: null
    }

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    });
  }

  handleSubmit = (e) => {
    e.preventDefault()
    axios.post('/register/', this.state)
      .then(res => console.log(res))
      .catch((error) => {
        const { email, name, password} = error.repsonse.data;
        this.setState({
          email_errorMsg: email ? email[0] : null,
          name_errorMsg: name ? name[0]: null,
          password_errorMsg: password ? password[0]: null
        });
      });
  }

  render(){
    return (
      <div className="container">
        <h3>Sign up Form</h3>
        <form noValidate onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label htmlFor="name"> Name </label>
            <input
              type="text"
              className="form-control"
              name="name"
              id="name"
              onChange={this.handleChange}
              required
            />
            <div>{this.state.name_errorMsg}</div>
          </div>
          <div className="form-group">
            <label htmlFor="email"> Email </label>
            <input
              type="email"
              className="form-control"
              name="email"
              id="email"
              onChange={this.handleChange}
              required
              />
             <div>{this.state.email_errorMsg}</div>
          </div>
          <div className="form-group">
            <label htmlFor="password"> Password </label>
            <input
              type="password"
              className="form-control"
              name="password"
              id="password"
              onChange={this.handleChange}
              required
            />
            <div>{this.state.password_errorMsg}</div>
          </div>
          <button type="submit" className="btn btn-primary btn-block">Login</button>
        </form>
      </div>
    )
  }
}

export default Signup;