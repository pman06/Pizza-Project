import React, { Component } from 'react';

class PizzeriaDetail extends Component{
  render(){
    const obj = this.props.pizzeriaDetail;
    var detailStyle = {
      color:"yellow",
      border: "1px Solid yellow"
    }
    return( 
      <div style={detailStyle}>
          <h4>{obj.pizzeria_name}</h4>
          <h5>  
            Address: {obj.street} {obj.city} {obj.state} {obj.zip_code}
          </h5>
          <h6>Phone: {obj.phone_number} </h6>
          <p>{obj.description} </p>
      </div>
    );
  }
}

export default PizzeriaDetail
