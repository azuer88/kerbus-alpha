/**
 * Created by azuer88 on 3/24/17.
 */

var React = require('react');
var Modal = require('react-bootstrap').Modal;
// var Button = require('react').Button;

module.exports = React.createClass({
    getInitialState: function() {
        return { showModal: false };
    },
    close: function() {
        this.setState({ showModal: false });
    },
    open: function() {
        this.setState({ showModal: true });
    },
    closeClick: function(ev) {
        this.close();
        ev.preventDefault();
    },
    saveClick: function(ev) {
        if (this.props.onSave) this.props.onSave(); 
        this.close();
        ev.preventDefault();
    },
    render: function() {
        return (
                <Modal show={this.state.showModal} onHide={this.close}>
                      <Modal.Header closeButton>
                          <Modal.Title>Please login</Modal.Title>
                      </Modal.Header>

                      <Modal.Body>
                      One Fine ....
                      </Modal.Body>

                      <Modal.Footer>
                      No footer around here.
                      </Modal.Footer>

                </Modal>
        );
   }
});
