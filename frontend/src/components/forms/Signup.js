import React from 'react';
import axios from 'axios';

class Signup extends React.Component {
    state = {
      name: null,
      email: null,
      password: null,
      errors: {
        email_errorMsg: null,
        name_errorMsg: null,
        password_errorMsg: null
      }

    }

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value
    });
  }

  handleSubmit = (e) => {
    e.preventDefault()
    axios.post('http://127.0.0.1:8000/register/', this.state)
      .then(res => console.log(res))
      .catch((error) => {
        let response = {
          email: null,
          name: null,
          password: null
        }
        const { email, name, password} = JSON.parse(error.response.request.response);
        let emailss = email ? response.setState({...response.email, email})  : null;
        response.name = name ? name[0] : null;
        this.state.errors.password_errorMsg = password ? password[0] : null;
        console.log(response)
      });
  }

  render(){
    return (
      <div className="container">
        <h3>Sign up Form</h3>
        <form noValidate onSubmit={this.handleSubmit} >
          <div className="form-group">
            <label htmlFor="name"> Name </label>
            <input
              type="text"
              className="form-control is-invalid"
              name="name"
              id="name"
              onChange={this.handleChange}
              required
            />
            <div className="invalid-feedback"></div>
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
            <div className="invalid-feedback">Invalid Email Address</div>
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
            <div className="invalid-feedback"></div>
          </div>
          <button type="submit" className="btn btn-primary btn-block">Login</button>
        </form>
      </div>
    )
  }
}

export default Signup;