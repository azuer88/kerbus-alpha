/**
 * Created by azuer88 on 3/24/17.
 */
"use strict";

var React = require('react');
var ReactDOM = require('react-dom');
var $ = require('jquery');
var Cookies = require('js-cookie');

var LoginForm = React.createClass({

    render: function() {
        var csrftoken = Cookies.get('csrftoken')
        return (
                <form className="form-signin" method="post">
                    <h2 className="form-signin-heading">
                        Please login
                    </h2>
                    <input type="text" className="form-control"
                        name="username" placeholder="User name"
                        required="" autoFocus="" />
                    <input type="password" className="form-control"
                        name="password" placeholder="Password"
                        required="" />
                    <button className="btn btn-lg btn-primary btn-block"
                        type="submit">Login</button>
                    <input type="hidden" name="csrfmiddlewaretoken"
                        value={csrftoken} />
                </form>
        );
    }
});

module.exports = LoginForm
