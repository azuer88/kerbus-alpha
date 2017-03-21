/**
 * Created by azuer88 on 2/24/17.
 */

var React = require('react');

module.exports = React.createClass({

   handleClick: function(ev) {
        if (this.props.load) {
            if (this.props.loader) {
                this.props.loader(this.props.load);
                ev.preventDefault();
            }
        } 
   },
   render: function() {
        return (
        <li>
           <a href={this.props.href} onClick={this.handleClick}>
           ::  {this.props.children}  ::
           </a>
        </li>
        );
  }
});
