/**
 * Created by azuer88 on 2/24/17.
 */

var React = require('react');

class MenuItem extends React.Component {
   render() {
     return (
        <li>
           <a href={this.props.href}>::  {this.props.children}  ::</a>
        </li>
     );
   }
}

module.exports = MenuItem ;


