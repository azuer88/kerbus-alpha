var React = require('react');
var $ = require('jquery');
var Login = require('./login');

module.exports = React.createClass({
    render: function() {
        return (
            <div>
                <div id="page-content-wrapper">
                    <Login csrfToken={this.props.csrfToken}/>
               </div>
            </div>
        );
    }
});

