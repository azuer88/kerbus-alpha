/**
 * Created by azuer88 on 2/24/17.
 */
var React = require('react');

module.exports = React.createClass({
    handleMenuClick: function(e) {
        this.props.onTitleClick(e);
    },
    render: function() {
        return (
            <div id="sidebar-wrapper">
               <ul className="sidebar-nav">
                   <li className="sidebar-brand">
                      <a href="#" onClick={this.handleMenuClick}>
                      {this.props.title}
                      </a>
                   </li>
                   {this.props.children}
               </ul>
           </div>
        )
    }
});
