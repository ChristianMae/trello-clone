import React from 'react';
import axios from 'axios';

class Login extends React.Component {
  state = {
    email: null,
    password: null,
    email_errMsg: null,
    password_errMsg: null,
    detail_errMsg: null,
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/token/', this.state)
      .then(res =>{
        localStorage.removeItem('access_token');
        localStorage.setItem('access_token', res.data.access);
        localStorage.setItem('refresh_token', res.data.refresh);

      })
      .catch(error => {
        const { email, password, detail} = error.response.data;
        this.setState({
          email_errorMsg: email ? email[0] : null,
          detail_errMsg: detail ? detail: null,
          password_errorMsg: password ? password[0]: null
        });
      });
  }

  render(){
    return (
      <div className="container">
        <form onSubmit={this.handleSubmit} noValidate>
          <span>{this.state.detail_errMsg}</span>
          <div className="form-group">
            <label htmlFor="email"> Email </label>
            <input
              required
              type="email"
              className="form-control"
              name="email"
              id="email"
              onChange={this.handleChange}
            />
            <span>{this.state.password_errorMsg}</span>
          </div>
          <div className="form-group">
            <label htmlFor="password"> Password </label>
            <input
              type="password"
              className="form-control"
              name="password"
              id="password"
              onChange={this.handleChange}
            />
            <span>{this.state.email_errorMsg}</span>
          </div>
          <button type="submit" className="btn btn-primary btn-block">Login</button>
        </form>
      </div>
    )
  }
}

export default Login;