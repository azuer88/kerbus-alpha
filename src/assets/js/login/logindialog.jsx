/**
 * Created by azuer88 on 3/24/17.
 */
"use strict";

var React = require('react');
var ReactDOM = require('react-dom');
var $ = require('jquery');

var LoginModal = React.createClass({
    handleSubmit: function(ev) {
        ev.preventDefault();
        if (typeof this.props.onSubmit !== 'undefined') {
            this.props.onSubmit();
        } else {
            console.log("onSubmit event was not defined");
        }
    },
    render: function() {
        return (
            <div className="modal fade" tabIndex="-1" role="dialog">
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                            <h4 className="modal-title"></h4>
                        </div>

                        <div className="modal-body">
                            <form className="form-signin" onSubmit={this.handleSubmit}>
                                <h2 className="form-signin-heading">Please login</h2>
                                <input type="text" className="form-control" name="username" placeholder="User name" required="" autoFocus="" />
                                <input type="password" className="form-control" name="password" placeholder="Password" required="" />
                                <button className="btn btn-lg btn-primary btn-block">Login</button>
                            </form>
                        </div>

                        <div className="modal-footer">
                        </div>

                    </div>
                </div>
            </div>
        );
   }
});

var LoginButton = React.createClass({
    handleShowModal: function() {
        var modal = React.cloneElement(<LoginModal onSubmit={this.props.submitHandler}></LoginModal>);
        var modalContainer = document.createElement('div');
        modalContainer.id = this.props.refId;
        document.body.appendChild(modalContainer);
        ReactDOM.render(modal, modalContainer, function() {
            var modalObj = $('#'+this.props.refId+'>.modal');
            modalObj.modal('show');
            modalObj.on('hidden.bs.modal', this.handleHideModal);
        }.bind(this));
    },
    handleHideModal: function() {
        $('#'+this.props.refId).remove();
    },
    render: function() {
        return (
            <div>
                <a href="javascript:;" 
                        onClick={this.handleShowModal}
                        className="btn btn-lg btn-primary">
                    Show Login
                </a>
            </div>
        );
    }
});



module.exports = LoginButton;
