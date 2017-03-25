/**
 * Created by azuer88 on 3/24/17.
 */
"use strict";

var React = require('react');
var ReactDOM = require('react-dom');
var $ = require('jquery');

var LoginModal = React.createClass({
    render: function() {
        return (
            <div className="modal fade" tabIndex="-1" role="dialog">
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                            <h4 className="modal-title">Title</h4>
                        </div>

                        <div className="modal-body">
                            <p>Modal content</p>
                        </div>

                        <div className="modal-footer">
                            <button type="button" className="btn btn-default" data-dismiss="modal">Cancel</button>
                            <button type="button" className="btn btn-primary">OK</button>
                        </div>

                    </div>
                </div>
            </div>
        );
   }
});

var LoginButton = React.createClass({
    handleShowModal: function() {
        var modal = React.cloneElement(<LoginModal></LoginModal>);
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
