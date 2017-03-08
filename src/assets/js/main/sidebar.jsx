/**
 * Created by azuer88 on 2/24/17.
 */
var React = require('react');

function mainmenu_click() {
   alert('please select an item below');
}

module.exports = React.createClass({
    render: function() {
        return (
            <div id="sidebar-wrapper">
               <ul className="sidebar-nav">
                   <li className="sidebar-brand">
                      <a href="#" onClick={mainmenu_click}>
                      Main Menu
                      </a>
                   </li>
                   {this.props.children}
               </ul>
           </div>
        )
    }
});
