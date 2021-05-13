import React, { Component } from 'react';

class PizzeriaDetail extends Component{
  render(){
    const p = this.props.p
    return(
      <div>
          <h4>{p.id}</h4>
          <h4>{p.pizzeria_name}</h4>
          <h4>{p.city}</h4>
          <h4>{p.zip_code}</h4>
      </div>
    );
  }
}

export default PizzeriaDetail
